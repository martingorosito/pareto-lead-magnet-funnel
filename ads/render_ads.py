"""Overlays the hook text, wordmark and CTA pill on the raw AI images to make the final ads.

Usage (from the repo root): pip install playwright && playwright install chromium
  FONTS_DIR=path/to/fonts python ads/render_ads.py        # all five
  FONTS_DIR=path/to/fonts python ads/render_ads.py 2 4    # only ads 2 and 4
FONTS_DIR must hold PJS800.ttf (Plus Jakarta Sans ExtraBold) and DMSans500.ttf (DM Sans Medium),
both free from Google Fonts. Output goes to ads/final/adN.png.
"""
import base64, os, sys
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(HERE,'raw')
OUT=os.path.join(HERE,'final')
FONTS=os.environ.get('FONTS_DIR', os.path.join(HERE,'fonts'))
ADS=[
 (1,'ad1-raw.png','You built a company<br>for freedom.','It gave you a job.','center 70%',0.55),
 (2,'ad2-raw.png','You didn’t start an agency','to forward emails.','center 80%',0.8),
 (3,'ad3-raw.png','After the third assistant,','you start to think it’s you.','center 75%',0.55),
 (4,'ad4-raw.png','You’re not disorganized.','You’re the only system.','center 70%',0.6),
 (5,'ad5-raw.png','Offshore hiring is a gamble.','Unless someone else<br>carries the risk.','center 70%',0.8),
]
FF=base64.b64encode(open(os.path.join(FONTS,'PJS800.ttf'),'rb').read()).decode()
FD=base64.b64encode(open(os.path.join(FONTS,'DMSans500.ttf'),'rb').read()).decode()
CSS='''@font-face{font-family:'Plus Jakarta Sans';font-weight:800;src:url(data:font/ttf;base64,FFX)}@font-face{font-family:'DM Sans';font-weight:500;src:url(data:font/ttf;base64,FDX)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#070C10;font-family:'DM Sans',sans-serif}
.ad{position:relative;width:1080px;height:1350px;overflow:hidden}
.ad img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.top{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(7,12,16,VAR) 0%,rgba(7,12,16,calc(VAR*0.75)) 45%,rgba(7,12,16,0) 100%)}
.bot{position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg,rgba(7,12,16,.92) 0%,rgba(7,12,16,0) 100%)}
.txt{position:absolute;left:72px;right:72px;top:84px}
.ad5 .txt{right:180px}.ad5 h1{font-size:60px}
.eyebrow{font-family:'DM Sans';font-weight:500;font-size:24px;letter-spacing:3px;text-transform:uppercase;color:#10B981;margin-bottom:22px;display:flex;align-items:center;gap:12px}
.eyebrow:before{content:'';width:36px;height:3px;background:#10B981;border-radius:2px}
h1{font-family:'Plus Jakarta Sans';font-weight:800;font-size:68px;line-height:1.08;letter-spacing:-1px;color:#fff;text-shadow:0 2px 24px rgba(0,0,0,.45)}
h1 span{color:#10B981;display:block}
b.p{font-weight:inherit;margin-left:-5px}b.a{font-weight:inherit;margin:0 -4px 0 -3px}
.wm i{margin-left:-3px}
.foot{position:absolute;left:72px;right:72px;bottom:64px;display:flex;justify-content:space-between;align-items:center}
.wm{font-family:'Plus Jakarta Sans';font-weight:800;font-size:34px;color:#fff;letter-spacing:-.5px}
.wm i{color:#10B981;font-style:normal}
.pill{background:#10B981;color:#070C10;font-family:'Plus Jakarta Sans';font-weight:800;font-size:26px;padding:16px 30px;border-radius:999px}
'''
def fix(t):
  import re
  t=t.replace('\u2019','<b class="a">\u2019</b>')
  return re.sub(r'([.,])(<br>|$)',r'<b class="p">\1</b>\2',t)
with sync_playwright() as p:
  b=p.chromium.launch()
  pg=b.new_page(viewport={'width':1080,'height':1350})
  for n,f,l1,l2,pos,dark in ADS:
    if len(sys.argv)>1 and str(n) not in sys.argv[1:]: continue
    data=base64.b64encode(open(os.path.join(RAW,f),'rb').read()).decode()
    html=f'''<html><head><style>{CSS.replace('VAR',str(dark)).replace('FFX',FF).replace('FDX',FD)}</style></head><body><div class="ad ad{n}"><img src="data:image/png;base64,{data}" style="object-position:{pos}"><div class="top"></div><div class="bot"></div>
<div class="txt"><div class="eyebrow">The Founder’s Bottleneck Audit</div><h1>{fix(l1)}<span>{fix(l2)}</span></h1></div>
<div class="foot"><div class="wm">Pareto Talent<i>.</i></div><div class="pill">Free audit →</div></div></div></body></html>'''
    pg.set_content(html, wait_until='networkidle'); pg.evaluate('document.fonts.ready')
    pg.screenshot(path=os.path.join(OUT,f'ad{n}.png'))
    print('ok',n)
  b.close()

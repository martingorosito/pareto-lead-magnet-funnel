"""Turns docs/automation/emails.md into paste-ready, branded HTML emails (emails/html/).

Usage: pip install pypandoc_binary, then run `python emails/generate_emails.py` from the repo root.
Link placeholders in the copy become GoHighLevel Custom Values, so the URLs live in one place.
"""
import re, os, pypandoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'docs', 'automation', 'emails.md')
OUT = os.path.join(ROOT, 'emails', 'html')
os.makedirs(OUT, exist_ok=True)

LINKS = {
    'AUDIT_URL': '{{custom_values.fp_mg_audit_url}}',
    'AUDIT_URL_NO_BOOKING': '{{custom_values.fp_mg_audit_url_fit_no}}',
    'BOOKING_URL': '{{custom_values.fp_mg_booking_url}}',
    'GUIDES': 'https://paretotalent.com/guides',
}
LINK_RE = r'\{\{(AUDIT_URL_NO_BOOKING|AUDIT_URL|BOOKING_URL|GUIDES)\}\}'

FONT = "'DM Sans', Arial, Helvetica, sans-serif"
HFONT = "'Plus Jakarta Sans', Arial, Helvetica, sans-serif"
TXT = '#1F2937'
EM = '#10B981'
DARK = '#070C10'

STYLE = {
    'p': f'margin:0 0 16px 0;font-family:{FONT};font-size:16px;line-height:1.6;color:{TXT};',
    'ol': f'margin:0 0 16px 0;padding-left:22px;font-family:{FONT};font-size:16px;line-height:1.6;color:{TXT};',
    'ul': f'margin:0 0 16px 0;padding-left:22px;font-family:{FONT};font-size:16px;line-height:1.6;color:{TXT};',
    'li': 'margin:0 0 8px 0;',
    'blockquote': f'margin:0 0 16px 0;padding:12px 16px;border-left:4px solid {EM};background:#F0FDF8;font-style:italic;',
    'a': f'color:#059669;text-decoration:underline;font-weight:bold;',
    'strong': f'color:{DARK};',
}


def button(text, href):
    return (
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 24px 0;">'
        f'<tr><td align="center" bgcolor="{EM}" style="border-radius:8px;">'
        f'<a href="{href}" target="_blank" style="display:inline-block;padding:14px 28px;font-family:{HFONT};'
        f'font-size:16px;font-weight:bold;color:#FFFFFF;text-decoration:none;border-radius:8px;">{text}</a>'
        '</td></tr></table>'
    )


def wrap(title, preview, inner):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
</head>
<body style="margin:0;padding:0;background:#F3F4F6;">
<!-- {title} -->
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preview}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F3F4F6;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:#FFFFFF;border-radius:12px;overflow:hidden;">
<tr><td style="background:{DARK};padding:22px 32px;">
<span style="font-family:{HFONT};font-size:20px;font-weight:800;color:#FFFFFF;letter-spacing:-0.3px;">Pareto Talent</span><span style="font-family:{HFONT};font-size:20px;font-weight:800;color:{EM};">.</span>
</td></tr>
<tr><td style="height:4px;background:{EM};line-height:4px;font-size:0;">&nbsp;</td></tr>
<tr><td style="padding:32px 32px 16px 32px;">
{inner}
</td></tr>
<tr><td style="padding:20px 32px 28px 32px;border-top:1px solid #E5E7EB;">
<p style="margin:0;font-family:{FONT};font-size:12px;line-height:1.5;color:#6B7280;">You're receiving this because you requested The Founder's Bottleneck Audit from Pareto Talent.<br>Pareto Talent · <a href="https://paretotalent.com" style="color:#6B7280;">paretotalent.com</a></p>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>
'''


def render(body):
    toks = {}
    def tok(val):
        k = f'ZZTOK{len(toks)}ZZ'
        toks[k] = val
        return k
    buttons = {}
    lines = []
    for line in body.split('\n'):
        m = re.match(r'^\*\*\[ (.+?) \]\*\* → (\S+)\s*$', line.strip())
        if m:
            k = f'BTNTOK{len(buttons)}'
            href = m.group(2)
            href = re.sub(LINK_RE, lambda x: LINKS[x.group(1)], href)
            buttons[k] = button(m.group(1), href)
            lines.append('')
            lines.append(k)
            lines.append('')
        else:
            lines.append(line)
    fixed = []
    for ln in lines:
        islist = re.match(r'^(- |\d+\. )', ln)
        if islist and fixed and fixed[-1].strip() and not re.match(r'^(- |\d+\. )', fixed[-1]):
            fixed.append('')
        fixed.append(ln)
    md = '\n'.join(fixed)
    md = re.sub(LINK_RE, lambda x: tok(LINKS[x.group(1)]), md)
    md = re.sub(r'\{\{[^}]+\}\}', lambda x: tok(x.group(0)), md)
    html = pypandoc.convert_text(md, 'html', format='markdown+hard_line_breaks-smart')
    for tag, st in STYLE.items():
        html = re.sub(rf'<{tag}(\s[^>]*)?>', lambda m, tag=tag, st=st: f'<{tag}{m.group(1) or ""} style="{st}">', html)
    for k, v in buttons.items():
        html = re.sub(rf'<p[^>]*>{k}</p>', lambda m, v=v: v, html)
    for k, v in toks.items():
        html = html.replace(k, v)
    # blockquote inner paragraph: keep simple
    return html


src = open(SRC).read()
sections = re.split(r'\n## ', src)[1:]
done = []
for sec in sections:
    head = sec.split('\n', 1)[0]
    m = re.match(r'(\d+) · `([^`]+)`', head)
    if not m:
        continue
    num, name = int(m.group(1)), m.group(2)
    if num == 12:
        continue  # internal notification typed in the workflow
    sec = sec.split('\n---')[0]
    subj = re.search(r'\*\*Subject:\*\* (.+)', sec).group(1).strip()
    prev = re.search(r'\*\*Preview text:\*\* (.+)', sec).group(1).strip()
    body = sec[sec.index('Hi {{contact.first_name}}'):].strip()
    html = wrap(name, prev, render(body))
    fname = f"{num:02d}-" + re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-') + '.html'
    open(os.path.join(OUT, fname), 'w').write(html)
    done.append((num, name, subj, prev, fname))

for d in done:
    print(d)

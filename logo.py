import re, glob

STACK = ('<polygon points="12,3 19.5,7 12,11 4.5,7" fill="currentColor" stroke-width="1.8" stroke-linejoin="round"/>'
         '<path d="M4.5 11.5L12 15.5L19.5 11.5" stroke-width="2.2" opacity=".7"/>'
         '<path d="M4.5 16L12 20L19.5 16" stroke-width="2.2" opacity=".4"/>')
FAV = '<link rel="icon" href="favicon.svg" type="image/svg+xml">'

# favicon
open('favicon.svg', 'w').write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b0b0e"/>'
 '<g transform="translate(8,8) scale(2)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round">' + STACK.replace('currentColor', '#fff') + '</g></svg>\n')

# swap logo mark in every page, add favicon link
for f in glob.glob('*.html'):
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'(<span class="logo"><svg class="i" viewBox="0 0 24 24">).*?(</svg></span>)',
               lambda m: m.group(1) + STACK + m.group(2), s, flags=re.S)
    if 'favicon.svg' not in s:
        s = s.replace('</head>', FAV + '\n</head>', 1)
    open(f, 'w', encoding='utf-8').write(s)

# slightly larger mark inside the tiles
c = open('style.css', encoding='utf-8').read()
c = c.replace('.logo svg{width:17px;height:17px}', '.logo svg{width:20px;height:20px}')
c = c.replace('.crumb .logo svg{width:13px;height:13px}', '.crumb .logo svg{width:15px;height:15px}')
open('style.css', 'w', encoding='utf-8').write(c)

# keep build.py in sync so rebuilding keeps the logo and favicon
b = open('build.py', encoding='utf-8').read()
if 'favicon.svg' not in b:
    b = b.replace('<link rel="stylesheet" href="pages.css">\n</head>', '<link rel="stylesheet" href="pages.css">\n' + FAV + '\n</head>', 1)
open('build.py', 'w', encoding='utf-8').write(b)
print('Logo updated: favicon.svg + all pages')

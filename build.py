import re, os

def rd(p): return open(p, encoding='utf-8').read()
def wr(p, t): open(p, 'w', encoding='utf-8').write(t)

def I(d, c='i'):
    return '<svg class="%s" viewBox="0 0 24 24">%s</svg>' % (c, d)

IC = {
 'home': '<path d="M4 11l8-7 8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1v-8z"/>',
 'chev': '<path d="M9 6l6 6-6 6"/>',
 'nodes': '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="12" r="2.5"/><path d="M8.5 12h7"/>',
 'layers': '<path d="M12 4l9 5-9 5-9-5 9-5zM3 14l9 5 9-5"/>',
 'bld': '<path d="M5 20V5h9v15M14 9h5v11M3 20h18M8 9h3M8 13h3"/>',
 'help': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 .9-1 1.7M12 17h.01"/>',
 'chat': '<path d="M4 5h16v11H9l-5 4V5z"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'card': '<rect x="3" y="6" width="18" height="13" rx="3"/><path d="M3 10h18M7 15h3"/>',
 'wallet': '<path d="M4 7h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7zm0 0V6a2 2 0 0 1 2-2h11M16 14h.01"/>',
 'store': '<path d="M4 9l1.5-4h13L20 9M4 9v10h16V9M4 9c0 2 4 2 4 0 0 2 4 2 4 0 0 2 4 2 4 0 0 2 4 2 4 0"/>',
 'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/>',
 'code': '<path d="M9 8l-4 4 4 4M15 8l4 4-4 4"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 'flag': '<path d="M5 21V4M5 5h12l-2 4 2 4H5"/>',
 'info': '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
 'users': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.5 3-6 6-6s6 2.5 6 6M16 5a3 3 0 0 1 0 6M18 14c2 .8 3 3 3 6"/>',
 'pin': '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 'check': '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
 'bolt': '<path d="M13 3L5 14h6l-1 7 8-11h-6l1-7z"/>',
 'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>',
 'server': '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/>',
 'qr': '<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><path d="M14 14h2v2h-2zM18 18h2M14 18v2"/>',
 'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 'bell': '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4l2-2zM10 20a2 2 0 0 0 4 0"/>',
 'chart': '<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>',
 'lock': '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'search': '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4-4"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 'box': '<path d="M4 8l8-4 8 4v8l-8 4-8-4V8zM4 8l8 4 8-4M12 12v8"/>',
}
def ic(k, c='i'): return I(IC[k], c)

# ---------- 1. split index.html: style.css + links, rewrite page links ----------
idx = rd('index.html')
if '<style>' in idx:
    m = re.search(r'<style>(.*?)</style>', idx, re.S)
    wr('style.css', m.group(1).strip() + '\n')
    idx = idx.replace(m.group(0), '<link rel="stylesheet" href="style.css">')
idx = idx.replace('Manrope:wght@400;500;600', 'Inter:wght@400;500;600')
if 'pages.css' not in idx:
    idx = idx.replace('<link rel="stylesheet" href="style.css">',
                      '<link rel="stylesheet" href="style.css">\n<link rel="stylesheet" href="pages.css">', 1)
for a, b in [('href="#how"', 'href="how-it-works.html"'), ('href="#stack"', 'href="under-the-hood.html"'),
             ('href="#about"', 'href="about.html"'), ('href="#faq"', 'href="faq.html"')]:
    idx = idx.replace(a, b)
wr('index.html', idx)

nav = re.search(r'<nav>.*?</nav>', idx, re.S).group(0)
foot = re.search(r'<footer class="ft">.*?</footer>', idx, re.S).group(0)
def up(h): return h.replace('href="#"', 'href="index.html"').replace('href="#', 'href="index.html#')
nav, foot = up(nav), up(foot)

# ---------- 2. pages.css ----------
CSS = r'''
body,.fs summary,.ft{font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.ft{letter-spacing:-.01em;font-size:14.5px}
.fs summary{color:var(--ink)}
.page-hero{padding-bottom:56px}
.page-hero h1{font-size:clamp(38px,7.4vw,72px);margin:34px 0 16px;max-width:16ch}
.crumbs{display:flex;align-items:center;gap:8px;margin-top:26px}
.cr{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;color:#fff;background:linear-gradient(180deg,rgba(255,255,255,.18),rgba(255,255,255,.05));border:1px solid rgba(255,255,255,.24);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);box-shadow:inset 0 1px 0 rgba(255,255,255,.45),0 8px 24px rgba(0,0,0,.28);transition:.25s}
a.cr:hover{background:rgba(255,255,255,.3);transform:translateY(-2px)}
.cr.on{background:#fff;color:#0a0a0c}
.cr svg{width:19px;height:19px}
.crumbs>svg{width:16px;height:16px;color:#aab2c0}
.tl{margin-top:40px;display:grid;gap:14px}
.tr{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:start;border:1px solid var(--line);border-radius:24px;padding:22px;background:linear-gradient(180deg,var(--bg),color-mix(in srgb,var(--bg) 93%,var(--ink)));box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 14px 34px -18px rgba(10,10,12,.22)}
.tr .si{margin:0}
.tr small{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
.tr h3{font-size:22px;margin:4px 0 6px}
.tr p{color:var(--mute);font-size:15px}
.card.st{min-height:300px;cursor:default}
.arch{background:#0b0b0e;color:#fff;border-radius:26px;padding:26px;position:relative;overflow:hidden;border:1px solid #1d1d24;margin-top:40px;box-shadow:inset 0 1px 0 rgba(255,255,255,.14)}
.arch::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.1) 1.2px,transparent 1.3px);background-size:18px 18px;pointer-events:none}
.arch>*{position:relative}
.al{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#aab2c0;margin-bottom:12px}
.ar{display:flex;flex-wrap:wrap;gap:10px}
.ac{display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:14px;border:1px solid rgba(255,255,255,.2);background:linear-gradient(145deg,rgba(255,255,255,.16),rgba(255,255,255,.03));font-size:14px;box-shadow:inset 0 1px 0 rgba(255,255,255,.3)}
.ac svg{width:18px;height:18px}
.core{border:1px solid rgba(255,255,255,.28);border-radius:20px;padding:18px;background:rgba(255,255,255,.06)}
.lk{height:34px;width:0;margin:0 auto;border-left:2px dashed rgba(255,255,255,.3)}
.three{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.gridfi{margin-top:40px;display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:30px}
.chip{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border:1px solid var(--line);border-radius:99px;font-size:14px;background:linear-gradient(180deg,var(--bg),color-mix(in srgb,var(--bg) 93%,var(--ink)));box-shadow:inset 0 1px 0 rgba(255,255,255,.8)}
.chip svg{width:16px;height:16px}
.note2{color:var(--mute);font-size:13px;margin-top:16px}
.kv{margin-top:34px;border:1px solid var(--line);border-radius:24px;overflow:hidden}
.kv div{display:flex;justify-content:space-between;gap:16px;padding:18px 22px;border-bottom:1px solid var(--line)}
.kv div:last-child{border-bottom:0}
.kv span{color:var(--mute)}.kv b{font-weight:600;text-align:right}
.two{display:grid;gap:26px;margin-top:34px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.two p{color:var(--mute);font-size:16px}
.search{display:flex;align-items:center;gap:10px;border:1px solid var(--line);border-radius:99px;padding:12px 18px;margin-top:34px;max-width:520px}
.search svg{color:var(--mute)}
.search input{border:0;outline:0;background:none;flex:1;font:inherit;color:var(--ink);min-width:0}
.gh{font-size:26px;margin:0;display:flex;align-items:center;gap:10px;max-width:none}
.fg{margin-top:54px}
.fg .faq{margin-top:16px}
.hide{display:none}
.band.sm{margin-top:80px}
'''
wr('pages.css', CSS.strip() + '\n')

# ---------- 3. page template ----------
T = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%%TITLE%% | ChatFi NetTech</title>
<meta name="description" content="%%DESC%%">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="pages.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
</head>
<body>
<header class="hero page-hero">
<div class="grid"></div>
<div class="wrap">
%%NAV%%
<div class="crumbs" role="navigation" aria-label="Breadcrumb"><a class="cr" href="index.html" aria-label="Home" title="Home">%%HOME%%</a>%%CHEV%%<span class="cr on" aria-current="page" title="%%TITLE%%">%%PIC%%</span></div>
<h1>%%H1%%</h1>
<p class="lead">%%LEAD%%</p>
</div>
</header>
<main class="wrap">
%%BODY%%
</main>
%%FOOT%%
<script>
if(matchMedia('(min-width:800px)').matches)document.querySelectorAll('.fs').forEach(function(d){d.open=true});
document.querySelectorAll('.card').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();c.style.setProperty('--x',(e.clientX-r.left)+'px');c.style.setProperty('--y',(e.clientY-r.top)+'px')})});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.1});
document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});
%%JS%%
</script>
</body>
</html>
'''
def page(fn, title, desc, pic, h1, lead, body, js=''):
    h = T
    for k, v in [('%%TITLE%%', title), ('%%DESC%%', desc), ('%%NAV%%', nav), ('%%HOME%%', ic('home')),
                 ('%%CHEV%%', ic('chev')), ('%%PIC%%', ic(pic)), ('%%H1%%', h1), ('%%LEAD%%', lead),
                 ('%%BODY%%', body), ('%%FOOT%%', foot), ('%%JS%%', js)]:
        h = h.replace(k, v)
    wr(fn, h)

def tag(k, t): return '<span class="tag">%s%s</span>' % (ic(k), t)
def band(h, p, a1, a2):
    return ('<section><div class="band sm rv"><h2>%s</h2><p>%s</p><div class="cta">%s%s</div></div></section>' % (h, p, a1, a2))
BTN_MAIL = '<a class="btn w" href="mailto:adelekesamuel917@gmail.com">%sEmail us %s</a>' % (ic('mail'), ic('arrow'))
def btn_o(href, k, t): return '<a class="btn o" href="%s">%s%s</a>' % (href, ic(k), t)

# ---------- 4. How it works ----------
steps = [
 ('link', 'Create', 'A merchant creates a payment from Store checkout, a payment link or the Pay API. Every payment gets its own unique on-chain reference.'),
 ('qr', 'Present', 'The customer sees a QR code or taps connect wallet. It works with Solana Pay wallets and with ChatFi Wallet.'),
 ('wallet', 'Approve', 'The customer approves in their wallet. The transfer settles on Solana, usually within seconds.'),
 ('shield', 'Verify', 'ChatFi Pay finds the transaction by its reference and checks the amount and token before marking it complete.'),
 ('bell', 'Notify', 'A webhook reaches the merchant, Store turns the payment into an order, and the customer lands on a confirmation page.'),
 ('chart', 'Report', 'Funds are forwarded to the merchant, and orders, customers and analytics update in the dashboard.'),
]
tl = ''.join('<div class="tr"><span class="si">%s</span><div><small>Step 0%d</small><h3>%s</h3><p>%s</p></div></div>' % (ic(k), i, t, p) for i, (k, t, p) in enumerate(steps, 1))
aud = [
 ('p1', 'user', 'Customers', 'Hold funds in ChatFi Wallet, scan or connect to pay, and keep a clear history of what you sent and received.'),
 ('p2', 'store', 'Merchants', 'Open a shop in Store, accept payments through Pay, and watch orders and revenue in one dashboard.'),
 ('p3', 'code', 'Developers', 'Use the same backend through API keys and webhooks to accept payments inside your own product.'),
]
cards = ''.join('<div class="card st"><div class="pat %s"></div><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>' % (p, ic(k), t, d) for p, k, t, d in aud)
body = ('<section><div class="rv">%s<h2>A payment, start to finish.</h2><p class="sub">Six steps, one backend. Each step hands off to the next without anything for you to stitch together.</p></div><div class="tl rv">%s</div></section>'
        '<section><div class="rv">%s<h2>Built for three kinds of people.</h2></div><div class="cards rv">%s</div></section>'
        % (tag('nodes', 'The flow'), tl, tag('users', 'Who it is for'), cards)
        + band('Want the technical view?', 'See the architecture, services and API behind the flow.', '<a class="btn w" href="under-the-hood.html">%sUnder the hood %s</a>' % (ic('layers'), ic('arrow')), btn_o('index.html#contact', 'chat', 'Talk to us')))
page('how-it-works.html', 'How it works', 'How ChatFi Wallet, Pay and Store work together on one backend.', 'nodes',
     'How <span>ChatFi works.</span>', 'From a customer\u2019s first tap to a merchant\u2019s confirmed order, one backend carries every step.', body)

# ---------- 5. Under the hood ----------
def chips(items): return ''.join('<span class="ac">%s%s</span>' % (ic(k), t) for k, t in items)
arch = ('<div class="arch rv"><div class="al">Clients</div><div class="ar">%s</div><div class="lk"></div>'
        '<div class="core"><div class="al">ChatFi backend</div><div class="ar">%s</div></div><div class="lk"></div>'
        '<div class="three"><div><div class="al">Network</div><div class="ar">%s</div></div><div><div class="al">Data and services</div><div class="ar">%s</div></div></div></div>') % (
    chips([('wallet', 'Wallet app'), ('store', 'Store dashboard'), ('card', 'Pay checkout')]),
    chips([('card', 'Payments'), ('user', 'Accounts'), ('box', 'Commerce'), ('bell', 'Webhooks')]),
    chips([('globe', 'Solana')]),
    chips([('server', 'Database'), ('chart', 'Analytics')]))
svc = [('card', 'Payments', 'Creates payments, tracks them by reference and confirms them on-chain.'),
       ('user', 'Accounts and wallets', 'Keeps profiles, balances and activity for every user.'),
       ('box', 'Commerce engine', 'Products, themes, orders and checkout for every storefront.'),
       ('bell', 'Webhooks and events', 'Sends payment events to your server as they happen.'),
       ('chart', 'Analytics and reports', 'Revenue, orders, customers and scheduled summaries.'),
       ('key', 'Developer keys', 'Create, rotate and retire API keys without downtime.')]
fis = ''.join('<div class="fi">%s<b>%s</b><span>%s</span></div>' % (ic(k), t, d) for k, t, d in svc)
def term(title, lines): return '<div class="term"><div class="d"><i></i><i></i><i></i></div><div><span class="m">// %s</span></div>%s</div>' % (title, ''.join('<div>%s</div>' % l for l in lines))
terms = (term('create a payment', ['<span class="k">POST</span> /api/payments', '{ <span class="g">"amount"</span>: 25, <span class="g">"token"</span>: <span class="g">"USDC"</span> }'])
         + term('check its status', ['<span class="k">GET</span> /api/payments/{id}', '{ <span class="g">"status"</span>: <span class="g">"completed"</span> }'])
         + term('receive the webhook', ['<span class="k">POST</span> your-server.com/hook', '{ <span class="g">"event"</span>: <span class="g">"payment.completed"</span>,', '&nbsp;&nbsp;<span class="g">"amount"</span>: 25 }']))
stack = ''.join('<span class="chip">%s%s</span>' % (ic(k), t) for k, t in [('globe', 'Solana'), ('code', 'Next.js'), ('server', 'Vercel'), ('box', 'Firestore'), ('wallet', 'React Native'), ('bolt', 'Helius'), ('chart', 'Jupiter')])
prin = [('shield', 'Verify on-chain', 'A payment is complete only when the ledger says so.'),
        ('key', 'Rotate freely', 'Keys and webhook URLs change without breaking anything.'),
        ('layers', 'One backend', 'One source of truth shared by every product.'),
        ('bolt', 'Stay fast', 'Built on Solana for quick confirmation and low fees.')]
pr = ''.join('<div class="fi">%s<b>%s</b><span>%s</span></div>' % (ic(k), t, d) for k, t, d in prin)
body = ('<section><div class="rv">%s<h2>The architecture, in one picture.</h2><p class="sub">Every client talks to the same backend, and the backend talks to Solana.</p></div>%s</section>'
        '<section><div class="rv">%s<h2>Core services.</h2></div><div class="gridfi rv">%s</div></section>'
        '<section><div class="rv">%s<h2>The API, at a glance.</h2><p class="sub">Simple requests in, clear events out.</p></div><div class="dev rv" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">%s</div><p class="note2">Example shapes only. Full documentation arrives with open developer access.</p></section>'
        '<section><div class="rv">%s<h2>Design principles.</h2></div><div class="gridfi rv">%s</div></section>'
        '<section><div class="rv">%s<h2>Built with.</h2></div><div class="chips rv">%s</div></section>'
        % (tag('layers', 'Architecture'), arch, tag('server', 'Services'), fis, tag('code', 'API'), terms, tag('shield', 'Principles'), pr, tag('bolt', 'Stack'), stack)
        + band('Build on ChatFi.', 'Ask for early developer access and we will get you started.', BTN_MAIL, btn_o('how-it-works.html', 'nodes', 'How it works')))
page('under-the-hood.html', 'Under the hood', 'The architecture, services and API behind ChatFi.', 'layers',
     'Under <span>the hood.</span>', 'The architecture behind Wallet, Pay and Store: one backend, clear boundaries, built on Solana.', body)

# ---------- 6. About ----------
vals = [('p1', 'layers', 'Build the core once', 'One backend means every new product starts with payments, accounts and orders already solved.'),
        ('p2', 'bolt', 'Ship small, ship often', 'We release in small steps and fix what real merchants and customers run into.'),
        ('p3', 'globe', 'Local roots, global reach', 'Based in Nigeria and built so anyone, anywhere, can pay and sell.')]
vc = ''.join('<div class="card st"><div class="pat %s"></div><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>' % (p, ic(k), t, d) for p, k, t, d in vals)
kv = ''.join('<div><span>%s</span><b>%s</b></div>' % (a, b) for a, b in [
    ('Registered name', 'CHATFI NETTECH'), ('Business name no.', '9983489'), ('Registered', '3 November 2026'),
    ('Registered under', 'Companies and Allied Matters Act 2020'), ('Location', 'Oyo, Nigeria'), ('Network', 'Solana')])
body = ('<section><div class="rv">%s<h2>Why we exist.</h2></div><div class="two rv"><p>Money, shopping and play usually live in separate apps with separate accounts. We think they should share one foundation.</p><p>ChatFi NetTech is the parent company that builds and runs that foundation, so Wallet, Pay, Store and what comes next all work as one.</p></div></section>'
        '<section><div class="rv">%s<h2>What we believe.</h2></div><div class="cards rv">%s</div></section>'
        '<section><div class="rv">%s<h2>Company details.</h2></div><div class="kv rv">%s</div></section>'
        '<section><div class="rv">%s<h2>Who builds it.</h2></div><div class="cards rv"><a class="card st tl" href="https://x.com/SamuelA6643" target="_blank" rel="noopener noreferrer" aria-label="Adeleke Samuel on X (opens in a new tab)"><div class="pat p1"></div><div class="ic">%s</div><h3>Adeleke Samuel</h3><span class="pur">Founder</span><p>Builds the ChatFi products and the backend behind them.</p><span class="xl">@SamuelA6643<svg class="i" viewBox="0 0 24 24"><path d="M7 17L17 7M8 7h9v9"/></svg></span></a></div><style>a.card.tl{color:inherit;text-decoration:none;cursor:pointer;transition:transform .25s}a.card.tl:hover{transform:translateY(-3px)}a.card.tl:focus-visible{outline:2px solid #0a0a0a;outline-offset:3px}a.card.tl .xl{display:inline-flex;align-items:center;gap:6px;margin-top:18px;font-size:14px;font-weight:600;color:#fff;opacity:.9}a.card.tl .xl svg{width:16px;height:16px}@media (prefers-reduced-motion:reduce){a.card.tl{transition:none}a.card.tl:hover{transform:none}}</style></section>'
        % (tag('bld', 'Our story'), tag('flag', 'Values'), vc, tag('info', 'Facts'), kv, tag('users', 'Team'), ic('user'))
        + band('Let\u2019s talk.', 'Partnerships, merchants or press. We reply to every message.', BTN_MAIL, btn_o('faq.html', 'help', 'Read the FAQ')))
page('about.html', 'About', 'About ChatFi NetTech, the parent company behind ChatFi Wallet, Pay and Store.', 'bld',
     'About <span>ChatFi NetTech.</span>', 'The parent company behind the ChatFi products, building the backend that makes money, commerce and play work together.', body)

# ---------- 7. FAQ ----------
groups = [
 ('globe', 'General', [
  ('What is ChatFi NetTech?', 'The parent company behind the ChatFi products. We build and run the shared backend that powers Wallet, Pay and Store.'),
  ('Where are you based?', 'We are registered in Nigeria and serve customers anywhere.'),
  ('How do I contact you?', 'Email us at adelekesamuel917@gmail.com and we will reply.')]),
 ('box', 'Products', [
  ('What is ChatFi Wallet?', 'A mobile wallet for sending, receiving, swapping and earning on Solana.'),
  ('What is ChatFi Pay?', 'Payment infrastructure for merchants: payment links, QR codes and Solana Pay, verified on-chain.'),
  ('What is ChatFi Store?', 'A shop builder with themes, products, orders and analytics, with checkout powered by ChatFi Pay.'),
  ('What is the redacted product?', 'We cannot say yet. It is being built and will plug into everything else.')]),
 ('card', 'Payments', [
  ('Which currencies can I use?', 'Stablecoins such as USDC, SOL and Nigerian naira.'),
  ('How long does a payment take?', 'Solana settles in seconds, and ChatFi Pay confirms the payment automatically once it lands.')]),
 ('code', 'Developers', [
  ('Can I build on your backend?', 'Developer access is being opened up. Email us and we will get you started.'),
  ('Do you support webhooks?', 'Yes. Payment events are sent to your server as they happen.'),
  ('Where are the API docs?', 'Public documentation arrives with open developer access. Our Under the hood page shows the shape of the API.')])]
plus = '<svg class="i" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>'
gh = ''
for k, name, qs in groups:
    gh += '<div class="fg rv"><h2 class="gh">%s%s</h2><div class="faq">%s</div></div>' % (ic(k), name, ''.join('<details><summary>%s%s</summary><p>%s</p></details>' % (q, plus, a) for q, a in qs))
body = ('<section><div class="rv">%s<h2>Quick answers.</h2><div class="search">%s<input id="q" type="search" placeholder="Search questions" aria-label="Search questions"></div></div>%s<div id="none" class="sub hide" style="margin-top:30px">No questions match your search.</div></section>'
        % (tag('help', 'FAQ'), ic('search'), gh)
        + band('Still have a question?', 'Send us a message and we will get back to you.', BTN_MAIL, btn_o('how-it-works.html', 'nodes', 'How it works')))
js = ("var q=document.getElementById('q');q.addEventListener('input',function(){var v=q.value.toLowerCase().trim(),any=false;"
      "document.querySelectorAll('.fg').forEach(function(g){var s=0;g.querySelectorAll('details').forEach(function(d){var m=!v||d.textContent.toLowerCase().indexOf(v)>-1;d.classList.toggle('hide',!m);if(m){s++;d.open=!!v}});g.classList.toggle('hide',!s);if(s)any=true});"
      "document.getElementById('none').classList.toggle('hide',any)});")
page('faq.html', 'FAQ', 'Answers to common questions about ChatFi NetTech.', 'help',
     'Frequently <span>asked questions.</span>', 'Short answers about our products, payments and how to build with us.', body, js)

print('Built: index.html, style.css, pages.css, how-it-works.html, under-the-hood.html, about.html, faq.html')

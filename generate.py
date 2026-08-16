#!/usr/bin/env python3
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent
SITE = "https://hukinteractive.io"
PUB = "ca-pub-2479747791019341"
EMAIL = "gubin2423@gmail.com"

NAV = [
    ("/", "Home", "home"),
    ("/projects/", "Projects", "projects"),
    ("/about/", "About", "about"),
    ("/blog/", "Blog", "blog"),
    ("/contact/", "Contact", "contact"),
]


def page(
    path: str,
    title: str,
    description: str,
    body: str,
    active: str = "",
    canonical: Optional[str] = None,
    jsonld: str = "",
    og_image: str = "/assets/og.jpg",
):
    canonical = canonical or f"{SITE}{path if path.endswith('/') or path.endswith('.html') else path + '/'}"
    if path == "/":
        canonical = f"{SITE}/"
    nav = "".join(
        f'<a href="{href}" class="{"is-active" if key == active else ""}">{label}</a>'
        for href, label, key in NAV
    )
    extra_ld = f",{jsonld}" if jsonld else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index,follow" />
  <link rel="canonical" href="{canonical}" />
  <meta name="google-adsense-account" content="{PUB}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Huk Interactive" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE}{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{SITE}{og_image}" />
  <link rel="icon" href="/assets/favicon.png" type="image/png" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css?v=20260816" />
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>
  <script type="application/ld+json">
  [{{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Huk Interactive",
    "url": "{SITE}/",
    "logo": "{SITE}/assets/logo.svg",
    "email": "{EMAIL}",
    "address": {{"@type": "PostalAddress", "addressCountry": "UA"}},
    "sameAs": [
      "https://www.youtube.com/@HukInteractive",
      "https://www.instagram.com/hukinteractive/",
      "https://x.com/hukinteractive",
      "https://www.patreon.com/c/Hukinteractive",
      "https://discord.gg/GKa2yTp5jG"
    ]
  }},
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Huk Interactive",
    "url": "{SITE}/",
    "publisher": {{"@type": "Organization", "name": "Huk Interactive"}}
  }}{extra_ld}]
  </script>
</head>
<body>
  <div class="bg" aria-hidden="true"></div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="/"><img src="/assets/logo.svg" alt="" width="34" height="34" />Huk Interactive</a>
      <nav class="nav" aria-label="Primary">{nav}</nav>
      <div class="header-cta">
        <a class="btn btn-primary" href="https://ko-fi.com/hukinteractive" target="_blank" rel="noopener noreferrer">Support the studio</a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Open menu">☰</button>
      </div>
    </div>
  </header>
  <main>
{body}
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div>
          <strong>Huk Interactive</strong>
          <p>Independent game and app studio in Ukraine. We ship mobile games, tools, and live experiments.</p>
        </div>
        <div class="footer-links">
          <a href="/projects/">Projects</a>
          <a href="/about/">About</a>
          <a href="/blog/">Blog</a>
          <a href="/contact/">Contact</a>
        </div>
        <div class="footer-links">
          <a href="/privacy/">Privacy Policy</a>
          <a href="/terms/">Terms of Service</a>
          <a href="/refund/">Refund Policy</a>
          <a href="/ads.txt">ads.txt</a>
        </div>
      </div>
      <p class="legal">© 2026 Huk Interactive. All rights reserved.</p>
    </div>
  </footer>
  <script src="/script.js?v=20260816"></script>
</body>
</html>
"""
    out = ROOT / path.lstrip("/")
    if path == "/":
        out = ROOT / "index.html"
    elif path.endswith("/"):
        out = ROOT / path.lstrip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


def project_card(href, img, name, blurb, pills):
    pills_html = "".join(f'<span class="pill {cls}">{label}</span>' for cls, label in pills)
    return f"""
        <a class="project-card" href="{href}">
          <div class="thumb"><img src="{img}" alt="{name} icon" width="108" height="108" /></div>
          <div class="body">
            <h3>{name}</h3>
            <p>{blurb}</p>
            <div class="pills">{pills_html}</div>
          </div>
        </a>"""


PROJECTS = [
    ("/projects/block-runner-x/", "/assets/projects/brx.png", "Block Runner X",
     "Fast voxel runner with coin trails. Out now on the App Store.",
     [("live", "Live"), ("", "iOS")]),
    ("/projects/till/", "/assets/projects/till.png", "Till",
     "A 30-second cashier shift. Make exact change. Keep the combo alive.",
     [("review", "App Store review"), ("", "iOS")]),
    ("/projects/nook-sort/", "/assets/projects/nook.png", "Nook Sort",
     "Cozy book-sorting puzzle. Fill a shelf, lock the color, keep the shop.",
     [("dev", "In development"), ("", "iOS")]),
    ("/projects/smartbnb/", "/assets/projects/smartbnb.png", "SmartBNB",
     "Operations hub for short-term and long-term rental teams.",
     [("dev", "In development"), ("", "iOS"), ("", "Android")]),
    ("/projects/samurai-vs-yoikai/", "/assets/projects/svy.png", "Samurai vs Yoikai",
     "Lane defense where a samurai holds the line against demons.",
     [("dev", "In development"), ("", "iOS"), ("", "Android")]),
    ("/projects/samurun/", "/assets/projects/sr.png", "SamuRun",
     "Samurai endless runner inspired by arcade classics.",
     [("dev", "In development"), ("", "iOS"), ("", "Android")]),
]


def software_ld(name, desc, url, app_id=None, category="Game"):
    data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": name,
        "applicationCategory": category,
        "operatingSystem": "iOS",
        "description": desc,
        "url": url,
        "author": {"@type": "Organization", "name": "Huk Interactive"},
    }
    if app_id:
        data["installUrl"] = f"https://apps.apple.com/app/id{app_id}"
    import json
    return json.dumps(data, ensure_ascii=False)


# --- Home ---
page(
    "/",
    "Huk Interactive — Game and App Studio",
    "Huk Interactive is an independent studio in Ukraine. We build mobile games and apps: Block Runner X, Till, Nook Sort, SmartBNB, and more.",
    f"""
    <section class="hero" id="home">
      <div class="container hero-inner">
        <div>
          <span class="eyebrow">Studio in Ukraine</span>
          <h1>Games and apps, shipped with care.</h1>
          <p class="lead">We are a small team making arcade games, cozy puzzles, and useful tools. Unity, native iOS, and Android — from first sketch to the store.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="/projects/">See what we are building</a>
            <a class="btn btn-ghost" href="/contact/">Work with us</a>
          </div>
          <div class="metrics">
            <div><strong>6</strong>active projects</div>
            <div><strong>iOS + Android</strong>store-ready builds</div>
            <div><strong>2026</strong>shipping year</div>
          </div>
        </div>
        <div class="hero-mosaic" aria-hidden="true">
          <a class="mosaic-card" href="/projects/block-runner-x/"><img src="/assets/projects/brx.png" alt="" /><span>Block Runner X</span></a>
          <a class="mosaic-card" href="/projects/till/"><img src="/assets/projects/till.png" alt="" /><span>Till</span></a>
          <a class="mosaic-card" href="/projects/nook-sort/"><img src="/assets/projects/nook.png" alt="" /><span>Nook Sort</span></a>
          <a class="mosaic-card" href="/projects/smartbnb/"><img src="/assets/projects/smartbnb.png" alt="" /><span>SmartBNB</span></a>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <p class="section-kicker">What we do</p>
        <h2>A studio that ships both play and product.</h2>
        <div class="feature-grid" style="margin-top:28px">
          <article class="card"><div class="icon">▶</div><h3>Mobile game development</h3><p>Arcade runners, defense games, and casual puzzles built in Unity and Swift. Tight loops, clear juice, store-ready builds.</p></article>
          <article class="card"><div class="icon">⌂</div><h3>Apps for real work</h3><p>SmartBNB and other tools for teams who need dashboards, roles, tasks, and offline-friendly sync — not another spreadsheet.</p></article>
          <article class="card"><div class="icon">✦</div><h3>Art, UI, and feel</h3><p>Readable icons, animation, and menus that stay alive when the world pauses. We sweat the first ten seconds.</p></article>
          <article class="card"><div class="icon">◎</div><h3>Live ops and ads</h3><p>AdMob, rewarded ads, IAP, and retention experiments. We treat monetization as part of the design, not a sticker on top.</p></article>
        </div>
      </div>
    </section>

    <section id="projects">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="section-kicker">Now in production</p>
            <h2>Projects we are working on</h2>
          </div>
          <a class="btn btn-ghost" href="/projects/">All projects</a>
        </div>
        <div class="project-grid">
          {''.join(project_card(*p) for p in PROJECTS)}
        </div>
      </div>
    </section>

    <section class="sponsors" id="sponsors">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="section-kicker">Support</p>
            <h2>Sponsors keep the lights on</h2>
          </div>
          <div class="hero-actions">
            <a class="btn btn-primary" href="https://www.patreon.com/c/Hukinteractive" target="_blank" rel="noopener noreferrer">Patreon</a>
            <a class="btn btn-ghost" href="https://ko-fi.com/hukinteractive" target="_blank" rel="noopener noreferrer">Ko-fi</a>
          </div>
        </div>
        <p class="muted" style="margin-bottom:18px">We build from Ukraine, often through power cuts. A one-time gift of $300 or more is listed here.</p>
        <div class="sponsor-table">
          <div class="sponsor-row sponsor-head"><span>Name</span><span>Tier</span><span>Since</span></div>
          <div class="sponsor-row"><span>Your name can be first</span><span>—</span><span>—</span></div>
        </div>
      </div>
    </section>

    <section id="blog">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="section-kicker">Dev log</p>
            <h2>Notes from the build</h2>
          </div>
          <a class="btn btn-ghost" href="/blog/">Read all</a>
        </div>
        <div class="blog-grid">
          <a class="blog-card" href="/blog/fantasy-ui-integration/"><p class="blog-meta">Feb 9, 2026</p><h3>Fantasy UI that still moves when the game freezes</h3><p>Unscaled time, pause menus, and why the Game Over screen comes next.</p></a>
          <a class="blog-card" href="/blog/bringing-the-samurai-to-life/"><p class="blog-meta">Feb 2, 2026</p><h3>Bringing the samurai to life</h3><p>Death states, instant restarts, and animation that has to feel like impact.</p></a>
          <a class="blog-card" href="/blog/project-stability/"><p class="blog-meta">Jan 27, 2026</p><h3>Stability before spectacle</h3><p>Unity Version Control, safe experiments, and keeping the run loop solid.</p></a>
        </div>
      </div>
    </section>
    """,
    active="home",
)

# --- Projects index ---
page(
    "/projects/",
    "Projects — Huk Interactive",
    "Current Huk Interactive projects: Block Runner X, Till, Nook Sort, SmartBNB, Samurai vs Yoikai, and SamuRun.",
    f"""
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumbs"><a href="/">Home</a> / Projects</p>
        <h1>What we are building now</h1>
        <p class="lead">Games you can play in a minute, and one operations app for rental teams. Live, in review, or in active development.</p>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="project-grid">
          {''.join(project_card(*p) for p in PROJECTS)}
        </div>
      </div>
    </section>
    """,
    active="projects",
)


def project_page(slug, name, img, status_pills, lead, body, app_id=None, category="GameApplication", extra_links=""):
    pills = "".join(f'<span class="pill {cls}">{label}</span>' for cls, label in status_pills)
    url = f"{SITE}/projects/{slug}/"
    ld = software_ld(name, lead, url, app_id, category)
    page(
        f"/projects/{slug}/",
        f"{name} — Huk Interactive",
        lead,
        f"""
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumbs"><a href="/">Home</a> / <a href="/projects/">Projects</a> / {name}</p>
        <div class="project-hero">
          <img src="{img}" alt="{name} icon" width="140" height="140" />
          <div>
            <div class="pills">{pills}</div>
            <h1>{name}</h1>
            <p class="lead">{lead}</p>
            {extra_links}
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container prose">
        {body}
        <p><a class="btn btn-ghost" href="/projects/">← All projects</a></p>
      </div>
    </section>
        """,
        active="projects",
        jsonld=ld,
        og_image=img,
    )


project_page(
    "block-runner-x",
    "Block Runner X",
    "/assets/projects/brx.png",
    [("live", "Live on App Store"), ("", "iOS"), ("", "Endless runner")],
    "A fast voxel runner with coin trails. Jump, slide, and chase a cleaner line.",
    """
        <p>Block Runner X is our live endless runner. The world is built from chunks you can read at speed: coins pull the eye, gaps ask for a jump, and a miss should restart before frustration sets in.</p>
        <h2>Why we made it</h2>
        <p>We wanted a runner that feels like an arcade cabinet — short sessions, readable danger, and a score you can beat on the next train ride. Voxel art keeps the silhouette clear on a phone.</p>
        <h2>What you play</h2>
        <ul>
          <li>Lane running with jump and slide timing</li>
          <li>Coin trails that teach the good line</li>
          <li>Quick restarts so a crash is part of the loop, not the end of the night</li>
        </ul>
        <p>Block Runner X is available on the App Store. Support and privacy for the game live on this site, same as our other titles.</p>
    """,
    app_id="6758046092",
    extra_links='<a class="btn btn-primary" href="https://apps.apple.com/us/app/blockrunner-x/id6758046092" target="_blank" rel="noopener noreferrer">Get it on the App Store</a>',
)

project_page(
    "till",
    "Till",
    "/assets/projects/till.png",
    [("review", "Waiting for App Store review"), ("", "iOS"), ("", "Arcade")],
    "A 30-second cashier shift. A customer overpays. You make exact change before they walk.",
    """
        <p>Till is a one-thumb money game. You see TOTAL, PAID, and the change due. Tap bills and coins until the drawer is exact. The fewest pieces is a Perfect. Miss or stall and the combo dies.</p>
        <h2>The loop</h2>
        <p>Each shift is short on purpose. Thirty seconds is enough to feel clever and not enough to get comfortable. Daily modifiers change the rush: Black Friday, coin hops, big spenders, happy hour. Play once a day if you want the streak. Bank tips for longer shifts, more patience, and hotter combos.</p>
        <h2>Monetization we actually designed</h2>
        <p>A short ad can keep the shop open for ten more seconds or double the tips. No Ads and a starter pack are one-time purchases. There is no account. Progress stays on the iPhone. Apple handles every purchase.</p>
        <p>Till is in App Store review. When it is live, this page will carry the store link.</p>
    """,
    app_id="6801702190",
)

project_page(
    "nook-sort",
    "Nook Sort",
    "/assets/projects/nook.png",
    [("dev", "In development"), ("", "iOS"), ("", "Puzzle")],
    "A cozy shelf-sorting puzzle. Drag books onto a matching shelf, lock a color, and keep the shop tidy.",
    """
        <p>Nook Sort (also called Book Nook in the build) is our quiet puzzle. Books wait on the right. You drag them onto a shelf of the same color. Fill a shelf and it locks. Clear every shelf and the shop stays open.</p>
        <h2>How a nook works</h2>
        <p>A full matching shelf is the win condition for that row. An empty shelf is a workbench — park a book there when the move is stuck, then place it when a color opens. Campaign shelves get tighter as you go. Today’s nook is a fresh layout each day if you want a streak without a campaign grind.</p>
        <h2>Help without spoiling the think</h2>
        <p>Undo, a hint, or one extra empty shelf can unstick a board. Those can come from a short ad or from coins. No Ads and a starter pack are optional. No login. Progress stays on the device.</p>
        <p>We are finishing store materials and the first live campaign. This page is the public home for the game while it is in development.</p>
    """,
    app_id="6801847990",
)

project_page(
    "smartbnb",
    "SmartBNB",
    "/assets/projects/smartbnb.png",
    [("dev", "In development"), ("", "iOS"), ("", "Android"), ("", "App")],
    "An operations hub for rental property teams — owners, managers, staff, and tenants in one workspace.",
    """
        <p>SmartBNB is not a game. It is the app we are building for people who run short-term and long-term rentals and are tired of chats, notes, and spreadsheets that do not talk to each other.</p>
        <h2>Who it is for</h2>
        <ul>
          <li><strong>Owners</strong> see income, expenses, occupancy, and what needs a decision.</li>
          <li><strong>Managers</strong> assign turnovers, cleans, and repairs, then review the work.</li>
          <li><strong>Staff</strong> get a task with access codes, a checklist, and photo handoff.</li>
          <li><strong>Tenants</strong> can report a problem without joining the staff chaos.</li>
        </ul>
        <h2>What is in the product</h2>
        <p>Role-specific dashboards. Properties with occupied and vacant status. Tasks with triage colors. A three-step clean protocol (photos before, inventory and lock PIN, photos after). Team chats by property. Custom roles so a bookkeeper does not get the same buttons as a handyman. Voice capture for a quick task. Offline-friendly workspace sync.</p>
        <h2>Pricing we are aiming at</h2>
        <p>A 30-day trial for the working roles, then a low monthly subscription. Tenants stay free. iOS is native SwiftUI. Android is in active development to match.</p>
        <p>SmartBNB is in development. If you run a small rental team and want to try an early build, <a href="/contact/">write to us</a>.</p>
    """,
    category="BusinessApplication",
)

project_page(
    "samurai-vs-yoikai",
    "Samurai vs Yoikai",
    "/assets/projects/svy.png",
    [("dev", "In development"), ("", "iOS"), ("", "Android"), ("", "Tower defense")],
    "Lane defense where a samurai holds the gate while yokai press the line.",
    """
        <p>Samurai vs Yoikai is our lane-defense game. You are the last blade at the gate. Waves come down the path. You spend gold and XP to stay standing. The fantasy is simple: one fighter, many demons, a night that should not end on wave three.</p>
        <h2>What we are tuning</h2>
        <p>Readable silhouettes, a shop that does not stall the next wave, and a difficulty curve that teaches before it punishes.</p>
    """,
)

project_page(
    "samurun",
    "SamuRun",
    "/assets/projects/sr.png",
    [("dev", "In development"), ("", "iOS"), ("", "Android"), ("", "Endless runner")],
    "A samurai runner inspired by endless arcade classics — run, jump, slide, and die with no delay.",
    """
        <p>SamuRun is the sister to Block Runner X, with a different body and a different fantasy. You are a samurai in an endless city of obstacles. The death state has to fire on the first frame. The restart has to be instant. If the fall feels late, the run is already broken.</p>
        <h2>From the current build</h2>
        <p>We integrated a bow-combat animation set and a custom Animator trigger so a hit becomes a fall with zero wait. UI packs are going in next: pause menus that still animate on unscaled time, then a Game Over screen that is worth looking at while you tap retry.</p>
        <p>SamuRun is in development for iOS and Android.</p>
    """,
)

# --- About ---
page(
    "/about/",
    "About Huk Interactive",
    "Huk Interactive is a three-person studio in Ukraine making mobile games and apps. Meet the team and how we work.",
    """
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumbs"><a href="/">Home</a> / About</p>
        <h1>A small studio that still ships.</h1>
        <p class="lead">Three people in Ukraine. We make the games we want to play and the tools we wish existed. Power cuts are real. Deadlines still move.</p>
      </div>
    </section>
    <section>
      <div class="container about-inner">
        <div class="prose">
          <p>Huk Interactive is an independent digital studio. We design, build, and publish our own games and apps. We also take on focused product work when it fits the same craft: clear UX, native feel, and a build you can put in a store.</p>
          <p>Our stack is practical. Unity for 3D and arcade games. SwiftUI for iOS apps. Kotlin for Android when the product needs both phones. We use version control like adults and we do not pretend a vertical slice is a launch.</p>
          <div class="values"><span>Quality</span><span>Ship it</span><span>Player-first</span></div>
        </div>
        <div class="team">
          <div class="member"><div class="avatar lead"></div><div><strong>Vitalii Huk</strong><p>Studio lead — product and vision</p></div></div>
          <div class="member"><div class="avatar art"></div><div><strong>Denis Bebrosyan</strong><p>Creative director — art and animation</p></div></div>
          <div class="member"><div class="avatar eng"></div><div><strong>Mariia Kolianovska</strong><p>Tech director — engineering and systems</p></div></div>
        </div>
      </div>
    </section>
    """,
    active="about",
)

# --- Blog ---
page(
    "/blog/",
    "Dev blog — Huk Interactive",
    "Build notes from Huk Interactive: Unity UI, animation, and how we keep projects stable.",
    """
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumbs"><a href="/">Home</a> / Blog</p>
        <h1>Dev blog</h1>
        <p class="lead">Short notes from the current builds. No recap decks — just what we actually changed.</p>
      </div>
    </section>
    <section>
      <div class="container blog-grid">
        <a class="blog-card" href="/blog/fantasy-ui-integration/"><p class="blog-meta">Feb 9, 2026 · Dev blog</p><h3>Fantasy UI that still moves when the game freezes</h3><p>Unscaled time on UI animators, and why the pause menu has to feel alive.</p></a>
        <a class="blog-card" href="/blog/bringing-the-samurai-to-life/"><p class="blog-meta">Feb 2, 2026 · Dev blog</p><h3>Bringing the samurai to life</h3><p>Death states and a trigger-based Animator so a hit never waits a frame.</p></a>
        <a class="blog-card" href="/blog/project-stability/"><p class="blog-meta">Jan 27, 2026 · Dev blog</p><h3>Stability before spectacle</h3><p>Unity Version Control, safe experiments, and a run loop we can revert.</p></a>
      </div>
    </section>
    """,
    active="blog",
)


def blog_page(slug, title, date, body):
    page(
        f"/blog/{slug}/",
        f"{title} — Huk Interactive",
        f"{title}. Dev notes from Huk Interactive, {date}.",
        f"""
    <article class="page-hero">
      <div class="container prose">
        <p class="breadcrumbs"><a href="/">Home</a> / <a href="/blog/">Blog</a> / {title}</p>
        <p class="blog-meta">{date} · Dev blog</p>
        <h1>{title}</h1>
        {body}
      </div>
    </article>
        """,
        active="blog",
    )


blog_page(
    "fantasy-ui-integration",
    "Fantasy UI that still moves when the game freezes",
    "February 9, 2026",
    """
        <p>The look of the current runner is finally one piece. We dropped in Fantasy Menus and Warrior HUD and spent the week making them belong to the same game.</p>
        <p>The hard part was the pause menu. If you pause with <code>timeScale = 0</code>, every animator that lives in scaled time dies with the world. Buttons should still fly in. We moved those UI animators to unscaled time so the menu can breathe while the samurai is frozen mid-slide.</p>
        <p>Next is a dedicated Game Over screen. High score deserves a stage, not a leftover pause panel.</p>
    """,
)

blog_page(
    "bringing-the-samurai-to-life",
    "Bringing the samurai to life",
    "February 2, 2026",
    """
        <p>We spent this week on the Synty bow-combat set inside the runner. The clip that matters most is not the pretty run. It is the death.</p>
        <p>If the fall waits on a transition, the player already tapped retry in their head and the game feels late. We added a custom trigger on the Animator so a hit becomes the falling state on the same frame. Impact first. Restart second. That is the whole feel of an endless runner.</p>
    """,
)

blog_page(
    "project-stability",
    "Stability before spectacle",
    "January 27, 2026",
    """
        <p>Game development is not only art and code. It is being able to try a wild idea and come home.</p>
        <p>We hit a useful milestone with Unity Version Control (Plastic SCM). New movement experiments live on a changeset we can revert. The run, jump, and slide stay on a known-good line while we test animation and UI. That sounds boring. It is why the next trailer will not be a lie.</p>
    """,
)

# --- Contact ---
page(
    "/contact/",
    "Contact Huk Interactive",
    "Email Huk Interactive at gubin2423@gmail.com. Response time 24–48 hours. Studio based in Ukraine.",
    f"""
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumbs"><a href="/">Home</a> / Contact</p>
        <h1>Contact</h1>
        <p class="lead">Press, players, sponsors, and store review teams — one inbox.</p>
      </div>
    </section>
    <section>
      <div class="container split">
        <div class="policy-card">
          <p><strong>Email</strong><br /><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p><strong>Response time</strong><br />24–48 hours.</p>
          <p><strong>Payments</strong><br />Include the email you used to pay and the transaction ID if you have one.</p>
          <p><strong>Business</strong><br />Huk Interactive · Digital game and app studio · Ukraine</p>
        </div>
        <div>
          <h2>Social</h2>
          <div class="support-links">
            <a class="support-link" href="https://www.youtube.com/@HukInteractive" target="_blank" rel="noopener noreferrer">YouTube</a>
            <a class="support-link" href="https://www.instagram.com/hukinteractive/" target="_blank" rel="noopener noreferrer">Instagram</a>
            <a class="support-link" href="https://x.com/hukinteractive" target="_blank" rel="noopener noreferrer">X</a>
            <a class="support-link" href="https://discord.gg/GKa2yTp5jG" target="_blank" rel="noopener noreferrer">Discord</a>
            <a class="support-link" href="https://www.reddit.com/user/sttatrek/" target="_blank" rel="noopener noreferrer">Reddit</a>
            <a class="support-link" href="https://www.linkedin.com/groups/18048051/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a class="support-link" href="https://www.patreon.com/c/Hukinteractive" target="_blank" rel="noopener noreferrer">Patreon</a>
            <a class="support-link" href="https://ko-fi.com/hukinteractive" target="_blank" rel="noopener noreferrer">Ko-fi</a>
            <a class="support-link" href="https://www.kickstarter.com/profile/hukinteractive" target="_blank" rel="noopener noreferrer">Kickstarter</a>
          </div>
        </div>
      </div>
    </section>
    """,
    active="contact",
)

# --- Legal ---
page(
    "/privacy/",
    "Privacy Policy — Huk Interactive",
    "Privacy policy for hukinteractive.io and Huk Interactive digital products, including analytics and Google AdSense.",
    f"""
    <section class="page-hero">
      <div class="container prose">
        <p class="breadcrumbs"><a href="/">Home</a> / Privacy Policy</p>
        <h1>Privacy Policy</h1>
        <p class="blog-meta">Effective August 16, 2026</p>
        <p>Huk Interactive (“we”, “our”, “us”) operates hukinteractive.io and publishes digital games and apps. This policy explains what we collect on the website and how ads work.</p>
        <h2>1. Information we collect</h2>
        <ul>
          <li>Name and email if you write to us</li>
          <li>Payment details handled by Stripe, Apple, or Google — we do not store card numbers</li>
          <li>Standard analytics (pages viewed, device type, referrer)</li>
          <li>Advertising cookies and identifiers when Google AdSense serves ads on this site</li>
        </ul>
        <h2>2. How we use it</h2>
        <ul>
          <li>Answer mail and deliver digital products or early access</li>
          <li>Improve games, apps, and this website</li>
          <li>Show ads and measure whether they loaded</li>
        </ul>
        <h2>3. Advertising (Google AdSense)</h2>
        <p>This site uses Google AdSense. Google and its partners may use cookies and similar technologies to show ads, including ads based on your visits to this and other sites. You can opt out of personalized advertising at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener noreferrer">Google Ads Settings</a> and learn more at <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener noreferrer">Google advertising policies</a>.</p>
        <p>Third-party vendors, including Google, use cookies to serve ads based on a user’s prior visits to this website or other websites.</p>
        <h2>4. Payments</h2>
        <p>Website and sponsor payments go through Stripe, Patreon, or Ko-fi. App purchases go through the App Store or Google Play. We do not process raw card data.</p>
        <h2>5. Third-party services</h2>
        <p>We may use Stripe, Apple, Google (Play, AdSense, AdMob, analytics), Cloudflare, and social platforms linked from this site. Each has its own policy.</p>
        <h2>6. Data protection</h2>
        <p>We take reasonable measures to protect information. No method of transmission is perfect.</p>
        <h2>7. Contact</h2>
        <p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </section>
    """,
)

page(
    "/terms/",
    "Terms of Service — Huk Interactive",
    "Terms of service for the Huk Interactive website and digital products.",
    f"""
    <section class="page-hero">
      <div class="container prose">
        <p class="breadcrumbs"><a href="/">Home</a> / Terms of Service</p>
        <h1>Terms of Service</h1>
        <p class="blog-meta">Effective August 16, 2026</p>
        <p>By using hukinteractive.io you agree to these terms.</p>
        <h2>1. Services</h2>
        <p>Huk Interactive is an independent studio. We provide information about our games and apps, early access builds, digital content, and supporter tiers.</p>
        <h2>2. Digital products</h2>
        <p>Products sold here or through storefronts are digital. Nothing physical is shipped.</p>
        <h2>3. Intellectual property</h2>
        <p>Games, apps, art, text, and marks belong to Huk Interactive unless we say otherwise.</p>
        <h2>4. Early access</h2>
        <p>Early builds can be unfinished or buggy. That is the point of early access.</p>
        <h2>5. Ads</h2>
        <p>The website may show third-party ads. Ads in our mobile games are covered by each app’s store listing and privacy details.</p>
        <h2>6. Liability</h2>
        <p>We are not responsible for outages or issues outside our control, including hosting and storefronts.</p>
        <h2>7. Changes</h2>
        <p>We may update these terms. The date at the top is the current version.</p>
        <p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </section>
    """,
)

page(
    "/refund/",
    "Refund Policy — Huk Interactive",
    "Refund policy for Huk Interactive digital goods and supporter purchases.",
    f"""
    <section class="page-hero">
      <div class="container prose">
        <p class="breadcrumbs"><a href="/">Home</a> / Refund Policy</p>
        <h1>Refund Policy</h1>
        <p class="blog-meta">Effective August 16, 2026</p>
        <p>Huk Interactive sells digital goods. Because access is instant, sales are generally final.</p>
        <p>We may consider a refund for a duplicate charge or a technical error that blocked access you already paid for.</p>
        <p>App Store and Google Play purchases follow Apple and Google refund rules. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> with your payment email and transaction ID. We review requests case by case.</p>
      </div>
    </section>
    """,
)

# 404
page(
    "/404.html",
    "Page not found — Huk Interactive",
    "That page is not on hukinteractive.io.",
    """
    <section class="page-hero">
      <div class="container">
        <h1>This page is not in the build.</h1>
        <p class="lead">The URL is wrong or the page moved.</p>
        <a class="btn btn-primary" href="/">Back home</a>
        <a class="btn btn-ghost" href="/projects/">Projects</a>
      </div>
    </section>
    """,
    canonical=f"{SITE}/404.html",
)

# sitemap
urls = [
    "/",
    "/projects/",
    "/projects/block-runner-x/",
    "/projects/till/",
    "/projects/nook-sort/",
    "/projects/smartbnb/",
    "/projects/samurai-vs-yoikai/",
    "/projects/samurun/",
    "/about/",
    "/blog/",
    "/blog/fantasy-ui-integration/",
    "/blog/bringing-the-samurai-to-life/",
    "/blog/project-stability/",
    "/contact/",
    "/privacy/",
    "/terms/",
    "/refund/",
]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap.append(f"  <url><loc>{SITE}{u}</loc><changefreq>weekly</changefreq></url>")
sitemap.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
print("wrote sitemap.xml")

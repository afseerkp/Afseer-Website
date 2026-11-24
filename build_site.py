"""Generate the personal website from the same content source as the CV.

Run after any edit to cv_content.py so the site and the CV never drift apart.
"""
from html import escape as e
from pathlib import Path

import cv_content as C

# Update this once the domain is pointed at the site (used for canonical + social tags).
SITE_URL = "https://afseer.com"
CV_FILE = "Afseer-KP-CV.pdf"

OUT_DIR = Path(__file__).parent / "website"

STATS = [
    ("15+", "Years in IT infrastructure"),
    ("2", "Expert-level DevOps certifications"),
    ("1", "Cloud ERP built end to end"),
]

MODULES = [
    ('<path d="M4 19V9"/><path d="M10 19V5"/><path d="M16 19v-7"/><path d="M22 19V8"/>',
     "Accounting", "Ledgers, invoicing, VAT-ready reporting"),
    ('<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4'
     'a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
     "Inventory", "Multi-warehouse stock and valuation"),
    ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
     '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
     "CRM", "Customers, quotations and follow-ups"),
    ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
     '<path d="m16 11 2 2 4-4"/>',
     "HR & Payroll", "Employees, attendance and salaries"),
    ('<path d="M5 17h14v-5H5z"/><path d="M7 17v2"/><path d="M17 17v2"/>'
     '<path d="M3 12h2l2-5h10l2 5h2"/>',
     "VAN Sales", "Mobile route sales and settlements"),
    ('<path d="M12 3v18"/><path d="M5 8h14"/><path d="M7 13h10"/><path d="M9 18h6"/>',
     "Production", "Work orders, BOM and production costing"),
]

SITE_CERTS = [
    ("AZ", "Microsoft Certified: DevOps Engineer Expert", "AZ-400 \u00b7 Expert level", True),
    ("AWS", "AWS Certified DevOps Engineer", "Amazon Web Services \u00b7 Professional level", True),
    ("MS", "MCITP", "Microsoft Certified IT Professional", False),
    ("EX", "Microsoft Exchange Server 2007", "Enterprise messaging administration", False),
    ("HW", "Diploma in Computer Hardware & Networking", "IIHT Bangalore \u00b7 2006", False),
    ("NW", "Advanced Networking", "Government ITI, Kasaragod", False),
]

NAV = [("about", "About"), ("bizapp365", "BizApp365"),
       ("skills", "Skills"), ("certifications", "Certifications")]

LOCATION = "Dubai, United Arab Emirates"
WHATSAPP_URL = "https://wa.me/971582885633"

product = C.EXPERIENCE[0]
name_title = C.NAME_DISPLAY
summary_parts = [p.strip() for p in C.SUMMARY.replace(". Independently", ".|Independently").split("|")]


def tags(detail):
    return "\n".join(
        f'            <span class="tag">{e(t.strip())}</span>'
        for t in detail.split(",") if t.strip()
    )


nav_links = "\n".join(
    f'      <a href="#{slug}" data-nav>{label}</a>' for slug, label in NAV
)

proof_html = "\n".join(
    f'''      <div class="proof-item reveal">
        <strong>{e(v)}</strong>
        <span>{e(label)}</span>
      </div>''' for v, label in STATS
)

modules_html = "\n".join(
    f'''          <article class="module reveal" role="listitem">
            <span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24">{icon}</svg></span>
            <h3>{e(title)}</h3>
            <p>{e(desc)}</p>
          </article>''' for icon, title, desc in MODULES
)

product_points = "\n".join(
    f"            <li>{e(b)}</li>" for b in product["bullets"][1:4]
)

skills_html = "\n".join(
    f'''        <article class="skill reveal">
          <h3>{e(label)}</h3>
          <div class="tags">
{tags(detail)}
          </div>
        </article>''' for label, detail in C.SKILLS
)

certs_html = "\n".join(
    f'''        <article class="cert{" featured" if featured else ""} reveal">
          <div class="mark" aria-hidden="true">{e(mark)}</div>
          <div>
            <h3>{e(title)}</h3>
            <p>{e(sub)}</p>
          </div>
        </article>'''
    for mark, title, sub, featured in SITE_CERTS
)

focus_html = "\n".join(
    f"          <li>{e(c)}</li>" for c in C.COMPETENCIES[:6]
)

about_paras = "\n".join(
    f"        <p>{e(part if part.endswith('.') else part + '.')}</p>" for part in summary_parts if part
)

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(name_title)} \u2014 IT Team Lead, DevOps &amp; Cloud Engineer</title>
<meta name="description" content="IT Team Lead in Dubai with 15+ years in IT infrastructure. Microsoft Certified DevOps Engineer Expert (AZ-400) and AWS Certified DevOps Engineer Professional. Founder and developer of BizApp365 cloud ERP.">
<link rel="canonical" href="{SITE_URL}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(name_title)} \u2014 IT Team Lead, DevOps &amp; Cloud Engineer">
<meta property="og:description" content="15+ years in IT infrastructure. AZ-400 and AWS DevOps Professional certified. Founder of BizApp365 cloud ERP.">
<meta property="og:url" content="{SITE_URL}/">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{e(name_title)}",
  "jobTitle": "IT Team Lead",
  "url": "{SITE_URL}/",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE" }},
  "worksFor": {{ "@type": "Organization", "name": "OMNIX International LLC" }},
  "knowsAbout": ["DevOps", "Microsoft Azure", "Amazon Web Services", "CI/CD", "IT Infrastructure", "ERP Software"]
}}
</script>
</head>
<body>

<a class="skip-link" href="#main">Skip to main content</a>
<div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>

<header class="nav" id="siteNav">
  <div class="wrap nav-inner">
    <a href="#top" class="brand" aria-label="Afseer KP home">Afseer<span>.</span></a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links" id="primaryNav" aria-label="Primary">
{nav_links}
      <a class="btn btn-primary btn-sm locked-cv" href="{CV_FILE}" download data-locked="cv">
        <svg class="btn-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>
        Download CV
      </a>
    </nav>
  </div>
</header>

<main id="main">
  <div id="top"></div>

  <section class="hero">
    <div class="hero-atmosphere" aria-hidden="true"></div>
    <div class="wrap hero-content">
      <p class="eyebrow reveal">
        <span class="status-dot" aria-hidden="true"></span>
        Available for senior IT &amp; DevOps roles
      </p>
      <h1 class="reveal">{e(name_title)}</h1>
      <p class="role reveal">IT Team Lead \u00b7 DevOps &amp; Cloud \u00b7 Founder of BizApp365</p>
      <p class="lede reveal">Fifteen years building and running IT infrastructure across the UAE and India \u2014 now leading delivery with Azure and AWS DevOps pipelines, and shipping a multi-tenant cloud ERP.</p>
      <div class="hero-cta reveal">
        <a class="btn btn-primary locked-cv" href="{CV_FILE}" download data-locked="cv">
          <svg class="btn-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>
          Download CV
        </a>
        <a class="btn btn-secondary" href="#bizapp365">View product</a>
      </div>
      <p class="hero-meta reveal">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        {e(LOCATION)}
      </p>
    </div>
  </section>

  <section class="proof" aria-label="Highlights">
    <div class="wrap proof-grid">
{proof_html}
    </div>
  </section>

  <section id="about">
    <div class="wrap about-grid">
      <div class="section-head reveal">
        <p class="kicker">About</p>
        <h2>Infrastructure engineer who ships software</h2>
      </div>
      <div class="about-body reveal">
{about_paras}
        <ul class="focus-list">
{focus_html}
        </ul>
      </div>
    </div>
  </section>

  <section id="bizapp365" class="product">
    <div class="wrap">
      <div class="product-layout">
        <div class="product-copy reveal">
          <p class="kicker">Product</p>
          <h2>BizApp365 \u2014 cloud ERP for growing SMEs</h2>
          <p class="lede">{e(product["bullets"][0])}</p>
          <ul class="product-points">
{product_points}
          </ul>
          <a class="btn btn-primary" href="https://bizapp365.com" target="_blank" rel="noopener noreferrer">
            Visit bizapp365.com
            <svg class="btn-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>
          </a>
        </div>
        <div class="module-grid" role="list">
{modules_html}
        </div>
      </div>
    </div>
  </section>

  <section id="skills">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">Capabilities</p>
        <h2>Technical skills</h2>
        <p>Hands-on depth across cloud platforms, automation, infrastructure and delivery.</p>
      </div>
      <div class="skills-grid">
{skills_html}
      </div>
    </div>
  </section>

  <section id="certifications">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">Credentials</p>
        <h2>Certifications</h2>
      </div>
      <div class="cert-grid">
{certs_html}
      </div>
    </div>
  </section>

  <section class="closing">
    <div class="wrap closing-inner reveal">
      <p class="kicker">Next step</p>
      <h2>Discuss a role or project</h2>
      <p>Message on WhatsApp for the CV password, or unlock and download the full profile PDF.</p>
      <div class="closing-cta">
        <a class="btn btn-primary" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        <a class="btn btn-secondary locked-cv" href="{CV_FILE}" download data-locked="cv">Download CV</a>
      </div>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap foot-inner">
    <span>\u00a9 <span id="year"></span> {e(name_title)}</span>
    <span>Languages: {e(C.LANGUAGES.replace('  |  ', ', '))}</span>
  </div>
</footer>

<a class="whatsapp-float" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
  </svg>
</a>

<div class="lock-modal" id="lockModal" hidden>
  <div class="lock-modal-backdrop" data-lock-close tabindex="-1"></div>
  <div class="lock-dialog" role="dialog" aria-modal="true" aria-labelledby="lockTitle" aria-describedby="lockDesc">
    <button type="button" class="lock-close" data-lock-close aria-label="Close dialog">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
    </button>
    <div class="lock-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
    </div>
    <h3 id="lockTitle">Protected content</h3>
    <p id="lockDesc">Please enter the password. To obtain the password, please contact me via WhatsApp.</p>
    <form id="lockForm" autocomplete="off">
      <label class="field-label" for="lockPassword">Password</label>
      <div class="password-field">
        <input id="lockPassword" type="password" name="password" placeholder="Enter password" required autocomplete="current-password">
        <button type="button" class="password-toggle" id="passwordToggle" aria-label="Show password" aria-pressed="false">
          <svg class="icon-eye" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>
          <svg class="icon-eye-off" viewBox="0 0 24 24" aria-hidden="true" hidden><path d="M17.94 17.94A10.07 10.07 0 0 1 12 19c-6.5 0-10-7-10-7a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c6.5 0 10 7 10 7a18.5 18.5 0 0 1-2.16 3.19"/><path d="m1 1 22 22"/><path d="M14.12 14.12a3 3 0 1 1-4.24-4.24"/></svg>
        </button>
      </div>
      <p class="lock-error" id="lockError" role="alert" hidden>Incorrect password. Please try again.</p>
      <button type="submit" class="btn btn-primary" id="unlockBtn">Unlock</button>
    </form>
  </div>
</div>

<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="script.js"></script>
</body>
</html>
"""

OUT_DIR.mkdir(exist_ok=True)
(OUT_DIR / "index.html").write_text(HTML, encoding="utf-8")
print("wrote", OUT_DIR / "index.html")

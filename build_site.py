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

# Website-only presentation details.
STATS = [
    ("15+", "Years in IT infrastructure"),
    ("2", "Expert-level DevOps certifications"),
    ("1", "Cloud ERP product built end to end"),
]

MODULES = [
    ('<line x1="6" y1="20" x2="6" y2="13"/><line x1="12" y1="20" x2="12" y2="4"/>'
     '<line x1="18" y1="20" x2="18" y2="9"/>',
     "Accounting", "Ledgers, invoicing, VAT-ready reporting"),
    ('<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4'
     'a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.3 7 12 12 20.7 7"/>'
     '<line x1="12" y1="22" x2="12" y2="12"/>',
     "Inventory", "Multi-warehouse stock and valuation"),
    ('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
     '<path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
     "CRM", "Customers, quotations and follow-ups"),
    ('<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/>'
     '<polyline points="17 11 19 13 23 9"/>',
     "HR & Payroll", "Employees, attendance and salaries"),
    ('<rect x="1" y="5" width="14" height="11" rx="1"/><path d="M15 8h4l3 3v5h-7z"/>'
     '<circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18" cy="18.5" r="2.5"/>',
     "VAN Sales", "Mobile route sales and settlements"),
    ('<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4H4a2 2 0 0 0-2 2z"/>'
     '<line x1="7" y1="18" x2="8" y2="18"/><line x1="12" y1="18" x2="13" y2="18"/>'
     '<line x1="17" y1="18" x2="18" y2="18"/>',
     "Production", "Work orders, BOM and production costing"),
]

# Presentation-only titles for the cards; cv_content.CERTIFICATIONS stays the CV wording.
SITE_CERTS = [
    ("AZ", "Microsoft Certified: DevOps Engineer Expert", "AZ-400 \u00b7 Expert level", True),
    ("AWS", "AWS Certified DevOps Engineer", "Amazon Web Services \u00b7 Professional level", True),
    ("MS", "MCITP", "Microsoft Certified IT Professional", False),
    ("EX", "Microsoft Exchange Server 2007", "Enterprise messaging administration", False),
    ("HW", "Diploma in Computer Hardware & Networking", "IIHT Bangalore \u00b7 2006", False),
    ("NW", "Advanced Networking", "Government ITI, Kasaragod", False),
]

NAV = [("about", "About"), ("bizapp365", "BizApp365"), ("experience", "Experience"),
       ("skills", "Skills"), ("certifications", "Certifications"), ("contact", "Contact")]

EMAIL = "mail@afseer.com"
PHONE = "+971 58 288 5633"
LOCATION = "Dubai, United Arab Emirates"

product = C.EXPERIENCE[0]          # BizApp365 gets its own feature section
history = C.EXPERIENCE[1:]         # everything else goes in the timeline
name_title = C.NAME_DISPLAY


def tags(detail):
    return "\n".join(
        f'          <span class="tag">{e(t.strip())}</span>'
        for t in detail.split(",") if t.strip()
    )


nav_links = "\n".join(
    f'        <a href="#{slug}">{label}</a>' for slug, label in NAV
)

stats_html = "\n".join(
    f'''          <div class="stat reveal">
            <b>{e(v)}</b><span>{e(label)}</span>
          </div>''' for v, label in STATS
)

modules_html = "\n".join(
    f'''            <div class="module">
              <span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24">{icon}</svg></span>
              <b>{e(title)}</b><span>{e(desc)}</span>
            </div>''' for icon, title, desc in MODULES
)

product_points = "\n".join(
    f"            <li>{e(b)}</li>" for b in product["bullets"][1:4]
)

jobs_html = "\n".join(
    f'''        <article class="job reveal">
          <div class="job-head">
            <h3>{e(job["title"])}</h3>
            <span class="when">{e(job["dates"])}</span>
          </div>
          <p class="where">{e(job["display"])} \u2014 {e(job["location"])}</p>
          <ul>
{chr(10).join(f"            <li>{e(b)}</li>" for b in job["bullets"])}
          </ul>
        </article>''' for job in history
)

skills_html = "\n".join(
    f'''        <div class="skill card reveal">
          <h3>{e(label)}</h3>
          <div class="tags">
{tags(detail)}
          </div>
        </div>''' for label, detail in C.SKILLS
)

certs_html = "\n".join(
    f'''        <div class="cert card reveal{" featured" if featured else ""}">
          <div class="mark" aria-hidden="true">{e(mark)}</div>
          <div><b>{e(title)}</b><span>{e(sub)}</span></div>
        </div>'''
    for mark, title, sub, featured in SITE_CERTS
)

competencies_html = "  \u00b7  ".join(e(c) for c in C.COMPETENCIES[:6])

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
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{e(name_title)}",
  "jobTitle": "IT Team Lead",
  "email": "mailto:{EMAIL}",
  "telephone": "{PHONE}",
  "url": "{SITE_URL}/",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE" }},
  "worksFor": {{ "@type": "Organization", "name": "OMNIX International LLC" }},
  "knowsAbout": ["DevOps", "Microsoft Azure", "Amazon Web Services", "CI/CD", "IT Infrastructure", "ERP Software"]
}}
</script>
</head>
<body>

<header class="nav">
  <div class="wrap nav-inner">
    <a href="#top" class="brand">Afseer<span>.</span></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav-links">
{nav_links}
      <a class="btn btn-primary btn-sm" href="{CV_FILE}" download>Download CV</a>
    </nav>
  </div>
</header>

<main id="top">

  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="eyebrow"><span class="dot"></span> Available for senior IT &amp; DevOps roles</span>
        <h1>{e(name_title)}</h1>
        <p class="role">IT Team Lead &nbsp;\u00b7&nbsp; DevOps &amp; Cloud (Azure / AWS) &nbsp;\u00b7&nbsp; Founder of BizApp365</p>
        <p class="lede">Fifteen years building and running IT infrastructure across the UAE and India \u2014 now leading an IT team in Dubai, automating delivery with Azure and AWS DevOps pipelines, and shipping my own multi-tenant cloud ERP platform.</p>
        <div class="hero-cta">
          <a class="btn btn-primary" href="#contact">Get in touch</a>
          <a class="btn btn-ghost" href="{CV_FILE}" download>Download CV (PDF)</a>
        </div>
        <div class="hero-meta">
          <span><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>{e(LOCATION)}</span>
          <a href="mailto:{EMAIL}"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22 6 12 13 2 6"/></svg>{EMAIL}</a>
          <a href="tel:{PHONE.replace(' ', '')}"><svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>{PHONE}</a>
        </div>
      </div>
      <div class="stats">
{stats_html}
      </div>
    </div>
  </section>

  <section id="about">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">About</p>
        <h2>Infrastructure engineer who ships software</h2>
      </div>
      <div class="card reveal" style="padding:1.9rem 2.1rem">
        <p style="color:var(--muted)">{e(C.SUMMARY)}</p>
        <p style="margin-top:1.2rem;font-size:.83rem;font-weight:700;color:var(--navy)">{competencies_html}</p>
      </div>
    </div>
  </section>

  <section id="bizapp365" class="product">
    <div class="wrap product-hero">
      <div class="reveal">
        <span class="product-badge">\u25CF My own product</span>
        <h2>BizApp365 \u2014 cloud ERP for growing SMEs</h2>
        <p class="lede">{e(product["bullets"][0])}</p>
        <ul class="product-points">
{product_points}
        </ul>
        <a class="btn btn-primary" href="https://bizapp365.com" target="_blank" rel="noopener">Visit bizapp365.com \u2192</a>
      </div>
      <div class="module-grid reveal">
{modules_html}
      </div>
    </div>
  </section>

  <section id="experience">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">Experience</p>
        <h2>Career history</h2>
        <p>From hands-on support engineer to leading an IT team in Dubai, across manufacturing, education, retail and managed services.</p>
      </div>
      <div class="timeline">
{jobs_html}
      </div>
    </div>
  </section>

  <section id="skills" style="background:#fff;border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">Capabilities</p>
        <h2>Technical skills</h2>
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

  <section id="contact" class="contact">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">Contact</p>
        <h2>Let's talk</h2>
        <p>Open to IT leadership, DevOps and cloud engineering roles in the UAE, and to ERP projects for growing businesses.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-card reveal">
          <span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
        <div class="contact-card reveal">
          <span>Phone</span>
          <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a>
        </div>
        <div class="contact-card reveal">
          <span>Location</span><b>{e(LOCATION)}</b>
        </div>
      </div>
      <a class="btn btn-primary" href="{CV_FILE}" download>Download full CV (PDF)</a>
      <footer>
        <div class="foot-inner">
          <span>\u00a9 <span id="year"></span> {e(name_title)}</span>
          <span>Languages: {e(C.LANGUAGES.replace('  |  ', ', '))}</span>
        </div>
      </footer>
    </div>
  </section>

</main>

<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="script.js"></script>
</body>
</html>
"""

OUT_DIR.mkdir(exist_ok=True)
(OUT_DIR / "index.html").write_text(HTML, encoding="utf-8")
print("wrote", OUT_DIR / "index.html")

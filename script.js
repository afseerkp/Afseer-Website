// Sticky nav
const nav = document.querySelector('.nav');
const onScrollNav = () => nav.classList.toggle('scrolled', window.scrollY > 8);
onScrollNav();
window.addEventListener('scroll', onScrollNav, { passive: true });

// Scroll progress
const progress = document.getElementById('scrollProgress');
const updateProgress = () => {
  const doc = document.documentElement;
  const max = doc.scrollHeight - doc.clientHeight;
  const value = max > 0 ? (doc.scrollTop / max) * 100 : 0;
  progress.style.width = `${value}%`;
};
updateProgress();
window.addEventListener('scroll', updateProgress, { passive: true });
window.addEventListener('resize', updateProgress);

// Mobile menu
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');

const closeMenu = () => {
  links.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', 'Open menu');
};

toggle.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
});

links.querySelectorAll('a').forEach((a) => a.addEventListener('click', closeMenu));

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && links.classList.contains('open')) closeMenu();
});

// Active section in nav
const sectionIds = ['about', 'bizapp365', 'skills', 'certifications'];
const navItems = [...document.querySelectorAll('[data-nav]')];
const sections = sectionIds
  .map((id) => document.getElementById(id))
  .filter(Boolean);

const setActiveNav = () => {
  const offset = nav.offsetHeight + 24;
  let current = null;
  for (const section of sections) {
    if (section.getBoundingClientRect().top - offset <= 0) current = section.id;
  }
  navItems.forEach((item) => {
    const active = current && item.getAttribute('href') === `#${current}`;
    item.classList.toggle('is-active', Boolean(active));
  });
};
setActiveNav();
window.addEventListener('scroll', setActiveNav, { passive: true });
window.addEventListener('resize', setActiveNav);

// Scroll reveal
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px' }
  );
  document.querySelectorAll('.reveal').forEach((el, i) => {
    el.style.transitionDelay = `${Math.min(i % 6, 5) * 45}ms`;
    observer.observe(el);
  });
} else {
  document.querySelectorAll('.reveal').forEach((el) => el.classList.add('in'));
}

// Password gate for CV download
const LOCK_KEY = 'afseer-unlocked';
const LOCK_PASSWORD = 'Pa$@2026';
const modal = document.getElementById('lockModal');
const form = document.getElementById('lockForm');
const passwordInput = document.getElementById('lockPassword');
const errorEl = document.getElementById('lockError');
const passwordToggle = document.getElementById('passwordToggle');
const unlockBtn = document.getElementById('unlockBtn');
let pendingCvHref = null;
let lastFocus = null;

const isUnlocked = () => sessionStorage.getItem(LOCK_KEY) === '1';

const revealPrivate = () => {
  document.body.classList.add('is-unlocked');
};

const getFocusable = () =>
  modal.querySelectorAll(
    'button:not([disabled]), [href], input:not([disabled]), select, textarea, [tabindex]:not([tabindex="-1"])'
  );

const openModal = (cvHref = null) => {
  pendingCvHref = cvHref;
  lastFocus = document.activeElement;
  errorEl.hidden = true;
  passwordInput.value = '';
  passwordInput.type = 'password';
  passwordToggle.setAttribute('aria-pressed', 'false');
  passwordToggle.setAttribute('aria-label', 'Show password');
  passwordToggle.querySelector('.icon-eye').hidden = false;
  passwordToggle.querySelector('.icon-eye-off').hidden = true;
  unlockBtn.textContent = 'Unlock';
  unlockBtn.disabled = false;
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
  closeMenu();
  setTimeout(() => passwordInput.focus(), 30);
};

const closeModal = () => {
  modal.hidden = true;
  document.body.style.overflow = '';
  pendingCvHref = null;
  errorEl.hidden = true;
  if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
};

const unlock = () => {
  sessionStorage.setItem(LOCK_KEY, '1');
  revealPrivate();
  const href = pendingCvHref;
  closeModal();
  if (href) {
    const a = document.createElement('a');
    a.href = href;
    a.download = '';
    document.body.appendChild(a);
    a.click();
    a.remove();
  }
};

if (isUnlocked()) revealPrivate();

document.querySelectorAll('[data-locked="cv"]').forEach((el) => {
  el.addEventListener('click', (e) => {
    if (isUnlocked()) return;
    e.preventDefault();
    openModal(el.getAttribute('href'));
  });
});

passwordToggle.addEventListener('click', () => {
  const showing = passwordInput.type === 'text';
  passwordInput.type = showing ? 'password' : 'text';
  passwordToggle.setAttribute('aria-pressed', String(!showing));
  passwordToggle.setAttribute('aria-label', showing ? 'Show password' : 'Hide password');
  passwordToggle.querySelector('.icon-eye').hidden = !showing;
  passwordToggle.querySelector('.icon-eye-off').hidden = showing;
  passwordInput.focus();
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (passwordInput.value === LOCK_PASSWORD) {
    unlockBtn.textContent = 'Unlocked';
    unlockBtn.disabled = true;
    unlock();
    return;
  }
  errorEl.hidden = false;
  passwordInput.select();
});

modal.querySelectorAll('[data-lock-close]').forEach((el) => {
  el.addEventListener('click', closeModal);
});

document.addEventListener('keydown', (e) => {
  if (modal.hidden) return;
  if (e.key === 'Escape') {
    closeModal();
    return;
  }
  if (e.key !== 'Tab') return;
  const focusable = [...getFocusable()];
  if (!focusable.length) return;
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if (e.shiftKey && document.activeElement === first) {
    e.preventDefault();
    last.focus();
  } else if (!e.shiftKey && document.activeElement === last) {
    e.preventDefault();
    first.focus();
  }
});

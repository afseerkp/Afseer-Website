// Sticky nav shadow
const nav = document.querySelector('.nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
onScroll();
window.addEventListener('scroll', onScroll, { passive: true });

// Mobile menu
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
toggle.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
});
links.querySelectorAll('a').forEach((a) =>
  a.addEventListener('click', () => {
    links.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  })
);

// Scroll reveal
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
  el.style.transitionDelay = `${Math.min(i % 6, 5) * 60}ms`;
  observer.observe(el);
});

// Password gate for CV download
const LOCK_KEY = 'afseer-unlocked';
const LOCK_PASSWORD = 'Pa$@2026';
const modal = document.getElementById('lockModal');
const form = document.getElementById('lockForm');
const passwordInput = document.getElementById('lockPassword');
const errorEl = document.getElementById('lockError');
let pendingCvHref = null;

const isUnlocked = () => sessionStorage.getItem(LOCK_KEY) === '1';

const revealPrivate = () => {
  document.body.classList.add('is-unlocked');
};

const openModal = (cvHref = null) => {
  pendingCvHref = cvHref;
  errorEl.hidden = true;
  passwordInput.value = '';
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
  setTimeout(() => passwordInput.focus(), 30);
};

const closeModal = () => {
  modal.hidden = true;
  document.body.style.overflow = '';
  pendingCvHref = null;
  errorEl.hidden = true;
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

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (passwordInput.value === LOCK_PASSWORD) {
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
  if (e.key === 'Escape' && !modal.hidden) closeModal();
});

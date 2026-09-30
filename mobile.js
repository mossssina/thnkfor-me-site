(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    var toggle = document.querySelector('.nav-toggle');
    var header = document.querySelector('.site-header');
    if (!toggle || !header) return;

    // Move nav-toggle outside header-nav so it stays visible when nav is hidden
    var headerNav = header.querySelector('.header-nav');
    var headerMain = header.querySelector('.header-main');
    if (headerNav && headerMain && headerNav.contains(toggle)) {
      headerMain.appendChild(toggle);
    }

    function openNav() {
      header.classList.add('nav-open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('nav-overlay');
    }

    function closeNav() {
      header.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-overlay');
    }

    toggle.addEventListener('click', function(e) {
      e.stopPropagation();
      header.classList.contains('nav-open') ? closeNav() : openNav();
    });

    // Sub-dropdown toggle for Контент завод (mobile: tap to expand, not navigate)
    var subItem = header.querySelector('.nav-subitem');
    var subLink = subItem ? subItem.querySelector('a') : null;
    if (subItem && subLink) {
      subLink.addEventListener('click', function(e) {
        if (header.classList.contains('nav-open')) {
          e.preventDefault();
          e.stopImmediatePropagation();
          subItem.classList.toggle('sub-open');
        }
      });
    }

    // Close when clicking a nav link (subItem link handled above)
    header.querySelectorAll('.header-nav a').forEach(function(link) {
      if (link === subLink) return;
      link.addEventListener('click', closeNav);
    });

    // Close CTA click
    var cta = header.querySelector('.header-cta');
    if (cta) cta.addEventListener('click', closeNav);

    // Close on outside click
    document.addEventListener('click', function(e) {
      if (header.classList.contains('nav-open') && !header.contains(e.target)) {
        closeNav();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeNav();
    });
  });
})();

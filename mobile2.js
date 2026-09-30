(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    var toggle = document.querySelector('.nav-toggle');
    var header = document.querySelector('.site-header');
    if (!toggle || !header) return;

    function openNav() {
      header.classList.add('nav-open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('nav-overlay');
    }

    function closeNav() {
      header.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-overlay');
      // Reset all accordion states
      header.querySelectorAll('.nav-item.sub-open').forEach(function(el) { el.classList.remove('sub-open'); });
      header.querySelectorAll('.nav-subitem.sub-open').forEach(function(el) { el.classList.remove('sub-open'); });
    }

    toggle.addEventListener('click', function(e) {
      e.stopPropagation();
      header.classList.contains('nav-open') ? closeNav() : openNav();
    });

    // Mark nav items that have dropdowns and wire accordion
    header.querySelectorAll('.nav-item').forEach(function(item) {
      var dropdown = item.querySelector('.nav-dropdown');
      if (!dropdown) return;

      item.classList.add('has-dropdown');
      var trigger = item.querySelector('a, span');
      if (!trigger) return;

      trigger.addEventListener('click', function(e) {
        if (!header.classList.contains('nav-open')) return;
        e.preventDefault();
        e.stopImmediatePropagation();
        var isOpen = item.classList.contains('sub-open');
        // Close other open items at this level
        header.querySelectorAll('.nav-item.sub-open').forEach(function(other) {
          other.classList.remove('sub-open');
        });
        if (!isOpen) item.classList.add('sub-open');
      });
    });

    // Sub-dropdown accordion for Контент завод
    header.querySelectorAll('.nav-subitem').forEach(function(subItem) {
      var subLink = subItem.querySelector('a');
      if (!subLink) return;
      subLink.addEventListener('click', function(e) {
        if (!header.classList.contains('nav-open')) return;
        e.preventDefault();
        e.stopImmediatePropagation();
        subItem.classList.toggle('sub-open');
      });
    });

    // Close when clicking a leaf nav link (items without dropdowns)
    header.querySelectorAll('.header-nav a').forEach(function(link) {
      var parentItem = link.closest('.nav-item');
      var parentSubItem = link.closest('.nav-subitem');
      // Skip: links that are accordion triggers (direct child of nav-item with dropdown)
      if (parentItem && parentItem.classList.contains('has-dropdown') && link === parentItem.querySelector('a, span')) return;
      if (parentSubItem && link === parentSubItem.querySelector('a')) return;
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
      if (e.key === 'Escape') {
        closeNav();
        header.querySelectorAll('.nav-item.click-open').forEach(function(el) { el.classList.remove('click-open'); });
      }
    });

    // ── Desktop: click-to-open dropdown ─────────────────────────
    // First click opens dropdown; second click on same trigger navigates.
    // Fixes touch-laptop/iPad where CSS :hover is unreliable.
    header.querySelectorAll('.nav-item.has-dropdown').forEach(function(item) {
      var trigger = item.querySelector(':scope > a, :scope > span');
      if (!trigger) return;

      trigger.addEventListener('click', function(e) {
        if (header.classList.contains('nav-open')) return; // mobile accordion handles it

        if (item.classList.contains('click-open')) {
          // Second click on already-open item → allow navigation
          item.classList.remove('click-open');
          return;
        }

        e.preventDefault();
        // Close any other open item
        header.querySelectorAll('.nav-item.click-open').forEach(function(other) {
          other.classList.remove('click-open');
        });
        item.classList.add('click-open');
      });
    });

    // Close click-open dropdowns when clicking outside nav
    document.addEventListener('click', function(e) {
      if (!header.contains(e.target)) {
        header.querySelectorAll('.nav-item.click-open').forEach(function(el) { el.classList.remove('click-open'); });
      }
    });
  });
})();

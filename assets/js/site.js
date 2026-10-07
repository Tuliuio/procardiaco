/* Clínica Procardíaco — site interactions */
(function () {
  "use strict";
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var body = document.body;

  /* Sticky header state */
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 24) header.classList.add("solid");
    else header.classList.remove("solid");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile nav */
  if (toggle) {
    toggle.setAttribute("aria-label", "Abrir menu");
    toggle.setAttribute("aria-expanded", "false");
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    });
  }
  /* Close mobile nav when a link is tapped */
  document.querySelectorAll(".nav a").forEach(function (a) {
    a.addEventListener("click", function () { body.classList.remove("nav-open"); });
  });

  /* Reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ===================== Atribuição + captura de leads ===================== */
  // Cole aqui a URL do Web App do Google Apps Script (ver README). Vazio = não registra.
  var LEAD_ENDPOINT = "";

  /* Guarda UTMs/origem da 1ª visita para persistir entre páginas */
  var UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid"];
  function captureAttribution() {
    try {
      var qs = new URLSearchParams(location.search), found = false, store = {};
      UTM_KEYS.forEach(function (k) { if (qs.get(k)) { store[k] = qs.get(k); found = true; } });
      if (found) sessionStorage.setItem("pc_attr", JSON.stringify(store));
      if (!sessionStorage.getItem("pc_ref") && document.referrer && document.referrer.indexOf(location.host) === -1) {
        sessionStorage.setItem("pc_ref", document.referrer);
      }
    } catch (e) {}
  }
  function getAttribution() {
    var attr = {};
    try { attr = JSON.parse(sessionStorage.getItem("pc_attr") || "{}"); } catch (e) {}
    UTM_KEYS.forEach(function (k) { attr[k] = attr[k] || ""; });
    try { attr.referrer = sessionStorage.getItem("pc_ref") || document.referrer || ""; } catch (e) { attr.referrer = document.referrer || ""; }
    return attr;
  }
  captureAttribution();

  function logLead(data) {
    if (!LEAD_ENDPOINT) return;
    try {
      var payload = JSON.stringify(data);
      if (navigator.sendBeacon) {
        navigator.sendBeacon(LEAD_ENDPOINT, new Blob([payload], { type: "application/json" }));
      } else {
        fetch(LEAD_ENDPOINT, { method: "POST", mode: "no-cors", headers: { "Content-Type": "application/json" }, body: payload });
      }
    } catch (e) {}
  }

  /* Evento de conversão para Google Ads / GA4 (via gtag ou GTM/dataLayer, se instalados).
     Cada botão "Agendar <exame>" envia o exame, permitindo medir conversão por exame. */
  function trackConversion(el) {
    var params = {
      exame: el.getAttribute("data-exame") || "",
      cta_texto: (el.textContent || "").replace(/\s+/g, " ").trim(),
      pagina: location.pathname
    };
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: "agendar_whatsapp" }, params));
      if (typeof window.gtag === "function") window.gtag("event", "agendar_whatsapp", params);
    } catch (e) {}
  }

  /* Botões de WhatsApp: abrem a conversa direto (sem modal).
     Registra o lead best-effort, sem bloquear a navegação para o WhatsApp. */
  document.querySelectorAll('a[href*="wa.me"]').forEach(function (el) {
    el.addEventListener("click", function () {
      trackConversion(el);
      logLead(Object.assign({
        timestamp: new Date().toISOString(),
        exame: el.getAttribute("data-exame") || "",
        origem: "wa-direto",
        pagina: location.pathname
      }, getAttribution()));
    });
  });
})();

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

  /* ===================== Agendamento + captura de leads ===================== */
  // Cole aqui a URL do Web App do Google Apps Script (ver README). Vazio = não registra.
  var LEAD_ENDPOINT = "";
  var WA_NUMBER = "5553991431183";
  var EXAMS = [
    "Ecocardiograma", "Eletrocardiograma (ECG)", "Holter e MAPA",
    "Eco-Doppler de Carótidas e Vertebrais", "Eco-Doppler de Membros Inferiores",
    "Ecocardiograma Transesofágico"
  ];

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

  function waLink(msg) { return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(msg); }

  /* Monta o modal uma vez */
  var modal, els = {};
  function buildModal() {
    var opts = '<option value="">Selecione o exame…</option>' +
      EXAMS.map(function (e) { return '<option value="' + e + '">' + e + '</option>'; }).join("") +
      '<option value="__orientacao__">Ainda não sei / quero orientação</option>';
    var wa = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.7-.8-2-.9-.3-.1-.5-.2-.7.2-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-1.7-.9-2.9-1.5-4-3.4-.3-.5.3-.5.8-1.6.1-.2 0-.4 0-.5 0-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5 1.9.8 2.6.9 3.5.7.6-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.2-.3-.2-.6-.4zM12 2a10 10 0 0 0-8.6 15L2 22l5.1-1.3A10 10 0 1 0 12 2z"/></svg>';
    var wrap = document.createElement("div");
    wrap.className = "modal-overlay";
    wrap.setAttribute("hidden", "");
    wrap.innerHTML =
      '<div class="modal" role="dialog" aria-modal="true" aria-labelledby="agTitle">' +
        '<button class="modal-close" type="button" aria-label="Fechar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
        '<div class="modal-head"><span class="eyebrow">Agendamento</span><h2 id="agTitle">Solicite seu horário</h2><p>Escolha sua preferência e a nossa equipe confirma o horário pelo WhatsApp.</p></div>' +
        '<div class="modal-body">' +
          '<label class="field"><span>Qual exame?</span><select id="agExame">' + opts + '</select></label>' +
          '<div class="field-row">' +
            '<label class="field"><span>Preferência de data</span><input type="date" id="agData"></label>' +
            '<div class="field"><span>Período</span><div class="chips">' +
              '<label class="chip"><input type="radio" name="agPeriodo" value="manhã"><span>Manhã</span></label>' +
              '<label class="chip"><input type="radio" name="agPeriodo" value="tarde"><span>Tarde</span></label>' +
            '</div></div>' +
          '</div>' +
          '<label class="field"><span>Seu nome <em style="font-weight:400;color:var(--muted)">(opcional)</em></span><input type="text" id="agNome" placeholder="Como podemos te chamar?" autocomplete="name"></label>' +
        '</div>' +
        '<div class="modal-foot">' +
          '<a class="btn btn--wa btn--block btn--lg" id="agConfirm" target="_blank" rel="noopener" href="' + waLink("Olá! Vim pelo site e gostaria de agendar um exame.") + '">' + wa + ' Confirmar pelo WhatsApp</a>' +
          '<button class="modal-direct" type="button" id="agDirect">Prefiro falar direto no WhatsApp</button>' +
          '<p class="modal-note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> Resposta no horário de atendimento: Seg–Sex, 8h–12h e 14h–18h.</p>' +
        '</div>' +
      '</div>';
    document.body.appendChild(wrap);
    modal = wrap;
    els.dialog = wrap.querySelector(".modal");
    els.exame = wrap.querySelector("#agExame");
    els.data = wrap.querySelector("#agData");
    els.nome = wrap.querySelector("#agNome");
    els.confirm = wrap.querySelector("#agConfirm");
    els.direct = wrap.querySelector("#agDirect");
    // data mínima = hoje
    els.data.min = new Date().toISOString().split("T")[0];

    function currentMsg() {
      var ex = els.exame.value;
      var per = (wrap.querySelector('input[name="agPeriodo"]:checked') || {}).value || "";
      var nome = els.nome.value.trim();
      var msg;
      if (ex === "__orientacao__") msg = "Olá! Vim pelo site e gostaria de orientação sobre qual exame realizar.";
      else if (ex) msg = "Olá! Vim pelo site e gostaria de agendar: " + ex + ".";
      else msg = "Olá! Vim pelo site e gostaria de agendar um exame.";
      var pref = [];
      if (els.data.value) { var d = els.data.value.split("-"); pref.push("dia " + d[2] + "/" + d[1]); }
      if (per) pref.push("no período da " + per);
      if (pref.length) msg += " Minha preferência: " + pref.join(", ") + ".";
      if (nome) msg += " Meu nome é " + nome + ".";
      return msg;
    }
    function refresh() { els.confirm.href = waLink(currentMsg()); }
    wrap.addEventListener("input", refresh);
    wrap.addEventListener("change", refresh);

    function leadData(origem) {
      var per = (wrap.querySelector('input[name="agPeriodo"]:checked') || {}).value || "";
      var attr = getAttribution();
      return Object.assign({
        timestamp: new Date().toISOString(),
        exame: els.exame.value === "__orientacao__" ? "Orientação" : (els.exame.value || ""),
        data_preferida: els.data.value || "",
        periodo: per,
        nome: els.nome.value.trim(),
        origem: origem,
        pagina: location.pathname
      }, attr);
    }
    els.confirm.addEventListener("click", function () { logLead(leadData("modal-confirmar")); closeModal(); });
    els.direct.addEventListener("click", function () {
      logLead(leadData("modal-direto"));
      window.open(waLink("Olá! Vim pelo site e gostaria de agendar um exame."), "_blank", "noopener");
      closeModal();
    });

    // fechar
    wrap.querySelector(".modal-close").addEventListener("click", closeModal);
    wrap.addEventListener("mousedown", function (e) { if (e.target === wrap) closeModal(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal && !modal.hasAttribute("hidden")) closeModal(); });
    refresh();
  }

  var lastFocus = null;
  function openModal(preExame) {
    if (!modal) buildModal();
    if (preExame) {
      for (var i = 0; i < els.exame.options.length; i++) {
        if (els.exame.options[i].value === preExame) { els.exame.value = preExame; break; }
      }
      els.confirm.href = waLink((function () { els.exame.dispatchEvent(new Event("change", { bubbles: true })); return els.confirm.href; })());
    }
    lastFocus = document.activeElement;
    modal.removeAttribute("hidden");
    document.body.classList.add("modal-open");
    requestAnimationFrame(function () { modal.classList.add("open"); });
    setTimeout(function () { els.exame.focus(); }, 60);
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove("open");
    document.body.classList.remove("modal-open");
    setTimeout(function () { modal.setAttribute("hidden", ""); }, 250);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  /* Liga os CTAs de agendamento ao modal (sem JS, continuam indo ao WhatsApp).
     Pega botões de WhatsApp de agendamento; ignora .wa-direct (nº de contato,
     confirmar convênio, ícone do rodapé). */
  document.querySelectorAll('a.btn--wa, a.wa-float, a.qa-card[href*="wa.me"]').forEach(function (el) {
    if (el.classList.contains("wa-direct")) return;
    el.addEventListener("click", function (e) {
      e.preventDefault();
      openModal(el.getAttribute("data-exame"));
    });
  });
})();

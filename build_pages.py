#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas internas da Clínica Procardíaco no design system novo.
Executar a partir da pasta que contém 'procardiaco-site/'."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://clinicaprocardiaco.com"
WA_NUM = "5553991431183"

def wa(msg="Olá! Vim pelo site e gostaria de agendar um exame."):
    from urllib.parse import quote
    return f"https://wa.me/{WA_NUM}?text={quote(msg)}"

# ---- SVG icons -------------------------------------------------------------
IC = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.7-.8-2-.9-.3-.1-.5-.2-.7.2-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-1.7-.9-2.9-1.5-4-3.4-.3-.5.3-.5.8-1.6.1-.2 0-.4 0-.5 0-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5 1.9.8 2.6.9 3.5.7.6-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.2-.3-.2-.6-.4zM12 2a10 10 0 0 0-8.6 15L2 22l5.1-1.3A10 10 0 1 0 12 2z"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 15h6M9 11h2"/></svg>',
 "no-fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v7c0 1.1.9 2 2 2h0a2 2 0 0 0 2-2V2M5 11v11M11 2v20M11 8s3-1 3-3 0-3 0-3"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.5-1.5 3-3.3 3-5.5A3.5 3.5 0 0 0 12 6 3.5 3.5 0 0 0 2 8.5c0 2.2 1.5 4 3 5.5l7 7 7-7z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 "insta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 8.6 8 10 4.6-1.4 8-5 8-10V5l-8-3z"/><path d="m9 12 2 2 4-4"/></svg>',
 "pulse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
}

NAV = """      <a class="navlink" href="/#sobre">A Clínica</a>
      <a class="navlink" href="/#exames">Exames</a>
      <a class="navlink" href="/consultas-medicas/">Consultas</a>
      <a class="navlink" href="/#equipe">Equipe</a>
      <a class="navlink" href="/#instalacoes">Instalações</a>
      <a class="navlink" href="/#convenios">Convênios</a>
      <a class="navlink" href="/#contato">Contato</a>
      <a class="btn btn--magenta" href="https://resultados.clinicaprocardiaco.com" target="_blank" rel="noopener">Acessar resultados</a>"""

def header():
    return f"""<header class="site-header solid">
  <div class="container header-inner">
    <a href="/" class="brand" aria-label="Clínica Procardíaco — início">
      <span class="brand-imgs">
        <img class="brand-full" src="/assets/img/logo.webp" alt="Clínica Procardíaco" width="180" height="42">
        <img class="brand-mark" src="/assets/img/mark.webp" alt="" aria-hidden="true" width="42" height="42">
      </span>
    </a>
    <button class="nav-toggle" type="button"><span></span></button>
    <nav class="nav" aria-label="Navegação principal">
{NAV}
    </nav>
  </div>
</header>"""

def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col footer-col--brand">
        <a href="/" class="brand"><img src="/assets/img/logo.webp" alt="Clínica Procardíaco" width="180" height="40"></a>
        <p>Clínica de cardiologia e diagnóstico cardiovascular em Pelotas, RS. Exames cardiológicos e vasculares, consulta médica e acesso digital aos resultados.</p>
        <div class="footer-social">
          <a href="https://www.instagram.com/procardiacopelotas" target="_blank" rel="noopener" aria-label="Instagram">{IC['insta']}</a>
          <a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{IC['wa']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Navegação</h4>
        <a href="/#sobre">A Clínica</a>
        <a href="/#exames">Exames</a>
        <a href="/consultas-medicas/">Consultas</a>
        <a href="/#equipe">Equipe</a>
        <a href="/#instalacoes">Instalações</a>
        <a href="/#convenios">Convênios</a>
        <a href="/#contato">Contato</a>
      </div>
      <div class="footer-col">
        <h4>Contato</h4>
        <a href="tel:+555330277377">53 3027.7377</a>
        <a href="{wa()}" target="_blank" rel="noopener">WhatsApp: 53 99143.1183</a>
        <a href="https://www.google.com/maps?q=Rua%20Andrade%20Neves%204043%2C%20Pelotas" target="_blank" rel="noopener">Rua Andrade Neves 4043, sala 01</a>
        <a href="https://resultados.clinicaprocardiaco.com" target="_blank" rel="noopener">Acessar resultados de exames</a>
      </div>
    </div>
    <div class="footer-legal">
      <span>Clínica Procardíaco – FNB Saúde e Consultoria LTDA · Registro CREMERS 16.042</span>
      <span>Diretor técnico-médico: Dr. Eduardo Gehling Bertoldi · CREMERS 29.584</span>
    </div>
    <p class="footer-note"><strong>Atenção:</strong> o WhatsApp e o agendamento da clínica não são canais de emergência. Em caso de dor no peito de início súbito, falta de ar intensa, desmaio ou sinais súbitos de AVC, procure atendimento de urgência ou ligue para o SAMU 192.</p>
    <div class="footer-bottom">
      <span>© 2026 Clínica Procardíaco — Diagnóstico Cardiovascular. Todos os direitos reservados.</span>
      <span>Pelotas / RS</span>
    </div>
    <p class="footer-disclaimer">Este site contém informações gerais sobre saúde e não substitui avaliação médica individual.</p>
  </div>
</footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
  {IC['wa']}<span>Agende pelo WhatsApp</span>
</a>"""

def page(rel, title, desc, body, extra_ld=""):
    canonical = SITE + "/" + rel.replace("index.html", "")
    ld = ""
    if extra_ld:
        ld = f'\n<script type="application/ld+json">{extra_ld}</script>'
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#02398C">
<script>document.documentElement.className+=" js";</script>
<link rel="icon" href="/assets/img/favicon.png" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=Noto+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v=3">{ld}
</head>
<body>
{header()}
{body}
{footer()}
<script src="/assets/js/site.js?v=3" defer></script>
</body>
</html>
"""
    out = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel)

def page_hero(crumbs, h1, sub):
    cr = " <span>/</span> ".join(crumbs)
    return f"""<section class="page-hero">
  <div class="container">
    <div class="crumbs">{cr}</div>
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div>
</section>"""

def byline():
    return f"""<div class="byline">
  <div class="av"><img src="/assets/img/dr-eduardo.webp" alt="Dr. Eduardo Bertoldi"></div>
  <div>
    <b>Revisão técnica: Dr. Eduardo Gehling Bertoldi</b>
    <span>Especialista em Cardiologia e Ecocardiografia (SBC) · Mestre e Doutor em Cardiologia · CRM-RS 29.584 / RQE 23189</span>
  </div>
</div>"""

def cta_side(msg, exame="", label="Falar no WhatsApp", title="Agende seu exame"):
    dx = f' data-exame="{exame}"' if exame else ""
    return f"""<div class="side-card side-card--cta">
    <h3>{title}</h3>
    <p>Rápido e sem complicação, direto pela nossa equipe.</p>
    <a class="btn btn--wa btn--block"{dx} href="{wa(msg)}" target="_blank" rel="noopener">{IC['wa']} {label}</a>
    <a class="btn btn--outline-light btn--block" href="tel:+555330277377" style="margin-top:10px;">Ligar: 53 3027.7377</a>
  </div>"""

def faq_block(items):
    rows = "\n".join(
        f'    <details><summary>{q}</summary><div class="faq-a">{a}</div></details>'
        for q, a in items)
    return f'<h2>Perguntas frequentes</h2>\n<div class="faq">\n{rows}\n</div>'

def faq_ld(items):
    import json
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return json.dumps(data, ensure_ascii=False)

def side_facts(facts, title="Resumo do exame"):
    rows = "\n".join(
        f'    <div class="side-fact"><div class="ic">{IC[i]}</div><div><b>{v}</b><span>{l}</span></div></div>'
        for i, l, v in facts)
    return f'<div class="side-card">\n    <h3>{title}</h3>\n{rows}\n  </div>'

# ============================================================================
#  EXAMES
# ============================================================================
EXAMS = [
 dict(slug="ecocardiograma", nome="Ecocardiograma", cta="Agendar ecocardiograma",
   title="Ecocardiograma em Pelotas | Clínica Procardíaco",
   desc="Ecocardiograma (ultrassom do coração) em Pelotas-RS, com Doppler colorido, laudo em até 1 hora e cardiologistas especialistas. Agende pelo WhatsApp.",
   img="/assets/img/exame-ecocardiograma.png",
   sub="O “ultrassom do coração”: avalia em tempo real as câmaras, válvulas, paredes e o fluxo sanguíneo, com segurança total e sem radiação ionizante.",
   card="O “ultrassom do coração”: avalia em tempo real as câmaras, válvulas, paredes e o fluxo sanguíneo, com segurança total e sem radiação.",
   body="""<h2>O que é o ecocardiograma?</h2>
<p>O ecocardiograma (também chamado de <strong>ecodopplercardiograma</strong>) é o “ultrassom do coração”. Um transdutor encostado no tórax emite ondas de som de alta frequência que atravessam os tecidos e retornam em forma de eco. O equipamento converte esses ecos em <strong>imagens dinâmicas</strong>, permitindo ao cardiologista avaliar o tamanho das câmaras, a espessura das paredes, a força de contração e a direção dos fluxos sanguíneos.</p>
<h2>Como funciona o exame na prática?</h2>
<ul>
<li><strong>Posicionamento:</strong> o paciente deita em decúbito lateral esquerdo, com o braço levantado para melhorar a janela acústica.</li>
<li><strong>Gel condutor:</strong> uma fina camada de gel elimina o ar entre a pele e o transdutor.</li>
<li><strong>Aquisição de imagens:</strong> o médico posiciona o transdutor em diferentes pontos do tórax, capturando cortes e fluxos em tempo real.</li>
<li><strong>Doppler colorido:</strong> códigos de cores mostram direção e velocidade do sangue, ajudando a quantificar refluxos valvares ou estenoses.</li>
<li><strong>Métodos avançados:</strong> conforme a necessidade, aplicamos Doppler tissular, strain, speckle tracking e medida de volumes.</li>
</ul>
<div class="info-box"><h3>Principais benefícios</h3><p><strong>Segurança total</strong> (sem radiação ionizante), <strong>diagnóstico precoce</strong> antes que sintomas graves apareçam, <strong>acompanhamento fácil</strong> (pode ser repetido sempre que necessário) e orientação de cirurgias e tratamentos clínicos.</p></div>
<h2>Quando o ecocardiograma é indicado?</h2>
<ul>
<li>Sopros cardíacos detectados ao estetoscópio;</li>
<li>Avaliação da repercussão cardíaca da hipertensão arterial;</li>
<li>Suspeita de insuficiência cardíaca (cansaço, inchaço nas pernas, falta de ar);</li>
<li>Doenças valvares (estenose ou insuficiência mitral, aórtica etc.);</li>
<li>Avaliações esportivas ou pré-operatórias;</li>
<li>Acompanhamento pós-infarto e pós-cirurgia cardíaca;</li>
<li>Avaliação da repercussão cardíaca de quimioterapias e imunoterapias;</li>
<li>Avaliação de risco de doenças genéticas hereditárias, para tratamento precoce.</li>
</ul>
<p>Nossas práticas seguem as <strong>Diretrizes Brasileiras de Ecocardiografia</strong>.</p>
<h2>Precisa de preparo?</h2>
<p>Para o ecocardiograma transtorácico <strong>não é necessário jejum</strong> nem suspensão de medicamentos. Pedimos apenas: evitar cremes ou óleos na região peitoral no dia do exame; levar pedidos médicos e exames anteriores, se houver; e, em caso de cirurgia cardíaca prévia, levar a descrição cirúrgica.</p>
<h2>Quanto tempo dura e como é o pós-exame?</h2>
<p>O exame leva de <strong>20 a 30 minutos</strong>. O paciente é imediatamente liberado e pode retornar às atividades normais, dirigir e trabalhar. O <strong>laudo é emitido em até 1 hora</strong>, impresso e com opção de PDF.</p>""",
   faq=[("O exame dói?","Não. O máximo que se sente é uma leve pressão do transdutor sobre o tórax."),
        ("Gestantes podem fazer ecocardiograma?","Sim. O exame é seguro em qualquer fase da gestação, pois não usa radiação."),
        ("Qual a diferença entre ecocardiograma e eletrocardiograma?","O ecocardiograma mostra imagens do coração em movimento; o eletrocardiograma (ECG) registra apenas a atividade elétrica. Eles se complementam."),
        ("Posso fazer se tenho marcapasso ou prótese metálica?","Pode. Implantes não interferem nas ondas de ultrassom."),
        ("O convênio cobre o exame?","Informe-se no agendamento, pois documentos e cobertura variam conforme o convênio.")]),

 dict(slug="ecg", nome="Eletrocardiograma (ECG)", cta="Agendar ECG",
   title="Eletrocardiograma (ECG) em Pelotas | Clínica Procardíaco",
   desc="Eletrocardiograma (ECG) em Pelotas-RS: exame rápido, indolor e sem jejum, com resultado no mesmo dia. Agende pelo WhatsApp.",
   img="/assets/img/exame-ecg.jpg",
   sub="Exame simples, rápido e indolor que registra a atividade elétrica do coração e ajuda a diagnosticar arritmias, infarto e outras alterações.",
   body="""<h2>O que é o eletrocardiograma?</h2>
<p>O ECG capta os pequenos impulsos elétricos que fazem o coração bater e os transforma em traçados (ondas P, QRS, T). Alterações na forma ou no intervalo dessas ondas podem indicar problemas de ritmo, isquemia (falta de sangue), aumento de cavidades cardíacas ou efeitos de medicamentos.</p>
<div class="info-box"><h3>Resumo rápido</h3><p><strong>Duração:</strong> 5 a 10 minutos. <strong>Não precisa de jejum.</strong> Resultado imediato impresso, com opção de acesso em PDF.</p></div>
<h2>Como o exame é feito, passo a passo</h2>
<ul>
<li><strong>Posicionamento:</strong> o paciente deita confortavelmente em decúbito dorsal;</li>
<li><strong>Eletrodos:</strong> dez adesivos descartáveis são colocados no peito, punhos e tornozelos, com gel condutor;</li>
<li><strong>Registro:</strong> o aparelho registra um eletrocardiograma de 12 derivações em poucos segundos;</li>
<li><strong>Impressão e laudo:</strong> o traçado sai na hora e o cardiologista avalia e assina o laudo.</li>
</ul>
<h2>Para que serve o ECG?</h2>
<ul>
<li>Detectar arritmias (taquicardia, fibrilação atrial, extrassístoles);</li>
<li>Avaliar dor no peito e ajudar a identificar infarto agudo;</li>
<li>Avaliação de rotina, sobretudo em diabéticos, hipertensos e atletas;</li>
<li>Controle de marcapasso;</li>
<li>Pré-operatório, quando indicado pelo médico.</li>
</ul>
<h2>Diferenciais na Clínica Procardíaco</h2>
<ul>
<li>Equipamento digital de alta resolução, com filtros para reduzir artefatos;</li>
<li>Equipe titulada pela Sociedade Brasileira de Cardiologia;</li>
<li>Agilidade: exame e laudo com análise e entrega rápidas.</li>
</ul>""",
   faq=[("Precisa de preparo especial?","Não. Basta chegar alguns minutos antes e trazer documento com foto e, se possível, a lista de medicamentos."),
        ("O exame dói ou causa choque?","Não. Os eletrodos apenas captam a eletricidade natural do coração; nada é injetado no corpo."),
        ("Gestantes podem fazer?","Sim. O ECG é totalmente seguro em qualquer fase da gestação, pois não usa radiação."),
        ("Qual a diferença entre ECG e Teste Ergométrico?","O ECG de repouso é feito deitado e avalia ritmo e estrutura elétrica básica. O Teste Ergométrico registra o ECG durante esforço (esteira), revelando isquemia que só aparece com exercício.")]),

 dict(slug="holter", nome="Holter", cta="Agendar Holter", tag="24h a 7 dias",
   title="Holter 24h a 7 dias em Pelotas | Clínica Procardíaco",
   desc="Holter (24 horas a 7 dias) em Pelotas-RS: monitorização contínua do ritmo cardíaco com equipamentos digitais e laudo por cardiologista. Agende pelo WhatsApp.",
   img="/assets/img/exame-holter.jpg",
   sub="Alguns problemas do coração só aparecem fora do consultório. O Holter registra seu ritmo cardíaco no dia a dia, revelando o que a consulta não capta.",
   body="""<h2>Em resumo</h2>
<div class="info-box"><p>O exame grava o eletrocardiograma de forma contínua — oferecemos de <strong>24 horas a 7 dias</strong> de monitorização.</p></div>
<h2>O que é o Holter?</h2>
<p>O Holter é um aparelho portátil que grava o eletrocardiograma continuamente. O exame tradicional dura 24 horas, mas oferecemos também monitoramento de <strong>2 até 7 dias</strong> para flagrar arritmias que não ocorrem diariamente. Nosso dispositivo é <strong>à prova d'água</strong>, permitindo banho de chuveiro e atividade física conforme orientação da equipe.</p>
<p><strong>Para que serve:</strong> detectar arritmias intermitentes, investigar tonturas, desmaios e palpitações sem causa aparente, avaliar a eficácia de medicamentos ou de marcapasso e monitorar o pós-infarto ou pós-ablação.</p>
<h2>Diferenciais na Clínica Procardíaco</h2>
<ul>
<li>Equipamentos digitais para monitorização ambulatorial, incluindo opções de Holter prolongado;</li>
<li>Instalação por profissional treinado pela equipe da clínica e laudo por cardiologista especialista;</li>
<li>Relatório detalhado com gráficos, histogramas e correlação de sintomas;</li>
<li>Suporte via WhatsApp para dúvidas durante a monitorização.</li>
</ul>""",
   faq=[("Preciso de preparo?","Não é necessário jejum. Prefira roupas confortáveis. Evite cremes ou óleos no tórax no dia do exame. Mantenha seus medicamentos habituais, salvo orientação médica diferente."),
        ("Posso trabalhar e dirigir?","Em geral, o objetivo é manter atividades habituais durante a monitorização. Siga as orientações da equipe e evite atividades que possam danificar ou molhar o aparelho, conforme o modelo utilizado."),
        ("O exame dói?","O Holter não causa dor; pode haver leve coceira onde ficam os eletrodos."),
        ("Quando recebo o resultado?","O laudo fica pronto em 10 dias úteis.")]),

 dict(slug="mapa", nome="MAPA", cta="Agendar MAPA", tag="24 horas",
   title="MAPA 24 horas em Pelotas | Clínica Procardíaco",
   desc="MAPA (Monitorização Ambulatorial da Pressão Arterial) 24 horas em Pelotas-RS: avalia a pressão arterial no dia a dia, com laudo por cardiologista. Agende pelo WhatsApp.",
   img="/assets/img/exame-mapa.jpg",
   sub="Alguns problemas do coração só aparecem fora do consultório. O MAPA registra sua pressão arterial no dia a dia, revelando o que a consulta não capta.",
   body="""<h2>Em resumo</h2>
<div class="info-box"><p>O aparelho mede a pressão arterial a cada <strong>15–30 minutos por 24 horas</strong>.</p></div>
<h2>O que é o MAPA?</h2>
<p>MAPA significa <strong>Monitorização Ambulatorial da Pressão Arterial</strong>. É um pequeno aparelho preso à cintura, conectado a uma braçadeira que infla automaticamente em horários programados (geralmente a cada 15 min de dia e 30 min à noite), gravando todas as medições.</p>
<p><strong>Para que serve:</strong> diagnosticar hipertensão mascarada, confirmar a hipertensão do avental branco, avaliar o controle real da pressão em pacientes tratados e identificar padrões noturnos de risco.</p>
<h2>Diferenciais na Clínica Procardíaco</h2>
<ul>
<li>Equipamentos digitais para monitorização ambulatorial;</li>
<li>Instalação por profissional treinado pela equipe da clínica e laudo por cardiologista especialista;</li>
<li>Relatório detalhado com gráficos, histogramas e correlação de sintomas;</li>
<li>Suporte via WhatsApp para dúvidas durante a monitorização.</li>
</ul>""",
   faq=[("Preciso de preparo?","Não é necessário jejum. Prefira roupas confortáveis. Utilize roupa que permita acesso fácil ao braço. Mantenha seus medicamentos habituais, salvo orientação médica diferente."),
        ("Posso trabalhar e dirigir?","Em geral, o objetivo é manter atividades habituais durante a monitorização. Siga as orientações da equipe e evite atividades que possam danificar ou molhar o aparelho."),
        ("O exame dói?","O inflar do MAPA pode apertar o braço por alguns segundos, mas não causa dor."),
        ("Quando recebo o resultado?","Em 1 dia útil após a retirada do aparelho.")]),

 dict(slug="eco-carotidas-vertebrais", nome="Eco-Doppler de Carótidas e Vertebrais", cta="Agendar Doppler de carótidas",
   title="Eco-Doppler de Carótidas e Vertebrais em Pelotas | Procardíaco",
   desc="Eco-Doppler de carótidas e vertebrais em Pelotas-RS: exame indolor e sem radiação que avalia o fluxo nas artérias do pescoço e o risco de AVC. Agende pelo WhatsApp.",
   img="/assets/img/exame-carotidas.webp",
   sub="Exame de ultrassom indolor e sem radiação que avalia em tempo real o fluxo de sangue nas artérias do pescoço e identifica placas que aumentam o risco de AVC.",
   body="""<h2>O que é o Eco-Doppler de Carótidas e Vertebrais?</h2>
<p>O exame combina duas tecnologias: a <strong>ultrassonografia convencional</strong>, que gera imagens anatômicas das artérias, e o <strong>efeito Doppler</strong>, que mostra em cores a direção e a velocidade do fluxo sanguíneo. Com um pequeno transdutor apoiado sobre a pele, o especialista visualiza as artérias carótidas e vertebrais, detectando placas de ateroma ou estenoses.</p>
<h2>Por que devo fazer este exame?</h2>
<p><strong>Principais fatores de risco:</strong> hipertensão arterial, colesterol ou triglicerídeos elevados, diabetes, tabagismo e histórico familiar de AVC ou doença coronariana. Além disso, alterações neurológicas, perda de consciência ou outros sintomas podem indicar a realização de eco-Doppler de carótidas. Seu médico pode ajudar a decidir se há indicação de realizar o exame.</p>
<div class="info-box info-box--alert"><h3>Atenção aos sinais de AVC</h3><p>Perda súbita de força ou sensibilidade de um lado do corpo, alteração súbita da fala ou da compreensão, assimetria facial ou perda súbita da visão podem indicar um AVC ou ataque isquêmico transitório. Nesses casos, <strong>não aguarde para agendar um exame: procure imediatamente atendimento de urgência ou ligue para o SAMU 192.</strong></p></div>
<h2>Como o exame é realizado?</h2>
<p>Você deita confortavelmente em uma maca, o médico aplica um gel à base de água no pescoço e desliza o transdutor levemente. <strong>Não há dor, agulhas ou radiação.</strong> O procedimento dura de 20 a 30 minutos e o resultado costuma ser liberado logo após a avaliação.</p>
<h2>Preciso de algum preparo?</h2>
<p>Na maioria dos casos não é necessário jejum. Use roupas que permitam acesso fácil ao pescoço e traga exames prévios. Pacientes que usam colar cervical devem avisar a equipe com antecedência.</p>
<h2>Resultados e próximos passos</h2>
<p>Se forem detectadas placas ou estreitamentos, o médico discutirá mudanças no estilo de vida, ajuste de medicamentos ou, em casos selecionados, procedimentos para abrir a artéria. Nosso serviço segue as recomendações da Sociedade Brasileira de Cardiologia.</p>""",
   faq=[("O exame dói?","Não. O Eco-Doppler é indolor e não invasivo."),
        ("Há riscos?","É considerado seguro para todas as idades, pois não usa radiação ionizante."),
        ("Com que frequência devo repetir?","O intervalo de acompanhamento depende dos achados, dos sintomas e do contexto clínico. Não existe um intervalo único de repetição adequado para todos os pacientes; siga a orientação do médico assistente.")]),

 dict(slug="eco-mmii", nome="Eco-Doppler de Membros Inferiores", cta="Agendar Doppler de membros inferiores",
   title="Eco-Doppler de Membros Inferiores em Pelotas | Procardíaco",
   desc="Eco-Doppler de membros inferiores em Pelotas-RS: avalia veias e artérias das pernas para diagnosticar varizes, trombose (TVP) e obstruções arteriais. Agende pelo WhatsApp.",
   img="/assets/img/exame-mmii.webp",
   sub="Ultrassom que avalia o fluxo sanguíneo em veias e artérias das pernas, ajudando a diagnosticar varizes, trombose venosa profunda (TVP) e obstruções arteriais.",
   body="""<h2>O que é o Eco-Doppler de membros inferiores?</h2>
<p>O exame combina a ultrassonografia convencional, que fornece imagens anatômicas, com a tecnologia Doppler, capaz de mostrar a velocidade e a direção do sangue em tempo real. Assim, permite avaliar o fluxo arterial e venoso, podendo identificar trombose, refluxo venoso ou estreitamentos arteriais, conforme o tipo de exame solicitado.</p>
<h2>Por que meu médico solicitou esse exame?</h2>
<ul>
<li><strong>Varizes</strong> — avaliar refluxo venoso antes de cirurgia ou escleroterapia;</li>
<li><strong>Trombose venosa profunda (TVP)</strong> — confirmar a presença de coágulos;</li>
<li><strong>Doença arterial periférica</strong> — investigar obstrução que causa dor ao caminhar;</li>
<li><strong>Pós-operatório vascular</strong> — checar enxertos ou stents.</li>
</ul>
<h2>Como o exame é feito?</h2>
<p>Você permanece deitado(a) ou em pé, conforme a fase do exame. O especialista aplica gel nas pernas e desliza suavemente o transdutor, obtendo imagens e escutando o fluxo sanguíneo. <strong>Não utiliza agulhas nem radiação.</strong> Em algumas etapas pode ser necessário exercer pressão com o transdutor, o que eventualmente causa leve desconforto. O procedimento dura cerca de 30 minutos e o laudo costuma ser entregue logo após a avaliação.</p>
<h2>Preciso de preparo?</h2>
<p>Não há necessidade de jejum. Se usa meias elásticas, traga-as para vestir depois do exame.</p>
<h2>Resultados e próximos passos</h2>
<p>O laudo descreve os achados do exame. A necessidade de tratamento e a escolha da conduta devem ser definidas pelo médico assistente de acordo com o quadro clínico.</p>""",
   faq=[("O exame dói?","Não. Você sentirá apenas o contato do transdutor e do gel sobre a pele."),
        ("Há riscos ou radiação?","Não há radiação ionizante. É seguro para gestantes, crianças e pessoas com marcapasso."),
        ("Quando devo repetir?","A necessidade e o momento de repetir o exame dependem do diagnóstico e da evolução clínica. Siga a orientação do médico assistente."),
        ("Qual a diferença entre o Doppler venoso e o arterial?","O exame venoso avalia as veias e é utilizado, entre outras situações, na investigação de trombose e insuficiência venosa. O exame arterial avalia as artérias e o fluxo de sangue para os membros, podendo identificar estreitamentos ou obstruções.")]),

 dict(slug="eco-te", nome="Ecocardiograma Transesofágico", cta="Agendar eco transesofágico",
   title="Ecocardiograma Transesofágico (ETE) em Pelotas | Procardíaco",
   desc="Ecocardiograma transesofágico (ETE) em Pelotas-RS: imagens detalhadas do coração a partir do esôfago, com sedação e acompanhamento da equipe. Agende pelo WhatsApp.",
   img="/assets/img/exame-transesofagico.webp",
   sub="Exame de ultrassom avançado que obtém imagens detalhadas do coração a partir do esôfago, utilizado em situações específicas para obter imagens detalhadas de válvulas, câmaras cardíacas e outras estruturas.",
   card="Exame de ultrassom avançado que obtém imagens detalhadas do coração a partir do esôfago, utilizado em situações específicas para avaliar válvulas, trombos e outras estruturas cardíacas.",
   body="""<h2>O que é o Ecocardiograma Transesofágico?</h2>
<p>Diferente do ecocardiograma tradicional feito pelo tórax (transtorácico), o <strong>ETE</strong> utiliza um transdutor acoplado a um tubo fino, semelhante a um endoscópio, inserido suavemente pela boca até o esôfago. Por ficar muito próximo das câmaras cardíacas, ele captura imagens de alta resolução, livres da interferência das costelas e dos pulmões.</p>
<h2>Por que meu médico solicitou o ETE?</h2>
<ul>
<li><strong>Endocardite infecciosa</strong> — detectar vegetações nas válvulas;</li>
<li><strong>Trombos ou fontes de embolia</strong> — pesquisar coágulos antes de cardioversão ou ablação de fibrilação atrial;</li>
<li><strong>Próteses valvares</strong> — verificar funcionamento e possíveis vazamentos;</li>
<li><strong>Defeitos congênitos</strong> — como forame oval patente ou comunicação interatrial;</li>
<li><strong>Guia em procedimentos</strong> — monitorar o posicionamento de dispositivos em cirurgias e TAVI.</li>
</ul>
<h2>Como é realizado o exame?</h2>
<ul>
<li>Você chega em jejum de 6 horas;</li>
<li>Uma enfermeira posiciona o acesso venoso para a medicação sedativa leve;</li>
<li>O médico aplica anestésico spray na garganta para reduzir o desconforto;</li>
<li>O transdutor é introduzido cuidadosamente enquanto você respira pelo nariz, e são capturadas imagens sob diferentes ângulos;</li>
<li>Após o exame, você permanece em observação por cerca de 30 minutos e recebe alta com acompanhante.</li>
</ul>
<div class="info-box"><h3>Preparo especial</h3><p>Em nosso serviço, orientamos <strong>jejum de alimentos e líquidos por 6 horas</strong> antes do exame. Informe alergias e medicamentos. Como é utilizada sedação, <strong>é necessário acompanhante</strong> e o paciente não deve dirigir após o exame pelo período informado pela equipe.</p></div>
<p>A maioria dos pacientes relata apenas leve pressão na garganta. Complicações são raras. Seguimos os protocolos da <em>European Society of Cardiology</em>, com monitorização contínua.</p>""",
   faq=[("Quanto tempo leva para sair o resultado?","O cardiologista analisa logo após o exame; o laudo costuma ficar pronto em até 1 hora."),
        ("Posso continuar meus remédios?","Sim, exceto caso seu médico tenha orientado suspensão de algum medicamento específico. Leve sua lista completa de medicações."),
        ("Existe alternativa ao ETE?","Dependendo da questão clínica, tomografia ou ressonância cardíaca podem fornecer informações complementares ou, em algumas situações, ser alternativas. A escolha do método depende da indicação médica."),
        ("O exame dói? Há riscos?","A maioria sente apenas leve pressão na garganta. A sedação consciente mantém você confortável. Complicações são incomuns, mas podem ocorrer. Antes do exame, a equipe avalia contraindicações, explica os riscos e orienta o preparo necessário.")]),
]

EXAM_ICON = {"ecocardiograma":"heart","ecg":"pulse","holter":"cal","mapa":"clock",
             "eco-carotidas-vertebrais":"shield","eco-mmii":"pulse","eco-te":"heart"}

def build_exam(e):
    others = [x for x in EXAMS if x["slug"] != e["slug"]][:3]
    rel_html = "\n".join(
        f'<a class="related-mini" href="/exames-realizados/{o["slug"]}/"><div class="ic">{IC[EXAM_ICON[o["slug"]]]}</div><div><b>{o["nome"]}</b><span>Saiba mais</span></div></a>'
        for o in others)
    body = f"""{page_hero(['<a href="/">Início</a>','<a href="/exames-realizados/">Serviços</a>', e['nome']], e['nome'], e['sub'])}
<section class="section">
  <div class="container">
    <div class="article-layout">
      <article class="prose reveal">
        <div class="article-media"><img src="{e['img']}" alt="{e['nome']} na Clínica Procardíaco" loading="lazy"></div>
        {e['body']}
        {faq_block(e['faq'])}
        {byline()}
      </article>
      <aside class="side">
        {cta_side(f"Olá! Gostaria de agendar: {e['nome']}.", e['nome'], label=e['cta'])}
        <div class="side-card">
          <h3>Outros exames</h3>
          <div style="display:grid; gap:10px;">{rel_html}</div>
        </div>
      </aside>
    </div>
  </div>
</section>"""
    ld = faq_ld(e['faq'])
    page(f"exames-realizados/{e['slug']}/index.html", e['title'], e['desc'], body, extra_ld=ld)

for e in EXAMS:
    build_exam(e)

# ============================================================================
#  SERVIÇOS (exames-realizados index)
# ============================================================================
def build_servicos():
    cards = ""
    for e in EXAMS:
        tag = f'<span class="card__tag">{e["tag"]}</span>' if e.get("tag") else ""
        cards += f"""      <a class="card reveal" href="/exames-realizados/{e['slug']}/">
        {tag}<div class="card__media"><img src="{e['img']}" alt="{e['nome']}" loading="lazy"></div>
        <div class="card__body"><h3>{e['nome']}</h3><p>{e.get('card', e['sub'])}</p>
        <span class="card__link">Saiba mais {IC['arrow']}</span></div>
      </a>\n"""
    body = f"""{page_hero(['<a href="/">Início</a>', 'Serviços'], 'Exames cardiológicos completos, em um só lugar', 'Nossos exames são realizados com responsabilidade, atenção à qualidade técnica e ao conforto do paciente.')}
<section class="section">
  <div class="container">
    <div class="grid grid-4">
{cards}      <a class="card reveal" href="/consultas-medicas/">
        <span class="card__tag">Consulta médica</span><div class="card__media"><img src="/assets/img/about.webp" alt="Consulta com cardiologista" loading="lazy"></div>
        <div class="card__body"><h3>Consulta com Cardiologista</h3><p>Avaliação cardiológica completa com especialistas titulados e estrutura para realizar exames no mesmo local.</p>
        <span class="card__link">Saiba mais {IC['arrow']}</span></div>
      </a>
    </div>
  </div>
</section>
<section class="section section--navy cta-band">
  <div class="cta-band__glow"></div>
  <div class="container">
    <h2>Ficou com dúvida sobre qual exame realizar?</h2>
    <p>Fale com a nossa equipe pelo WhatsApp. Ajudamos você a entender o pedido do seu médico e a agendar da melhor forma.</p>
    <div class="hero__cta"><a class="btn btn--wa btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Falar no WhatsApp</a>
    <a class="btn btn--light btn--lg" href="tel:+555330277377">Ligar: 53 3027.7377</a></div>
  </div>
</section>"""
    page("exames-realizados/index.html", "Serviços e Exames Cardiológicos em Pelotas | Clínica Procardíaco",
         "Ecocardiograma, ECG, Holter, MAPA, Eco-Doppler e consulta com cardiologista em Pelotas-RS. Exames cardiológicos com equipe especialista. Agende pelo WhatsApp.", body)

build_servicos()

# ============================================================================
#  A CLÍNICA
# ============================================================================
def build_clinica():
    vals = [("shield","Segurança nos resultados","Precisão técnica que apoia decisões e procedimentos médicos complexos."),
            ("pulse","Tecnologia e manutenção","Equipamentos de alta qualidade, com manutenção e controles periódicos."),
            ("users","Atuação em equipe","Colaboramos com colegas médicos, fortalecendo a cardiologia da região."),
            ("heart","Cuidado humanizado","Ambiente acolhedor e atendimento centrado no bem-estar do paciente.")]
    vhtml = "".join(
        f'<div class="feature reveal"><div class="ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i,t,d in vals)
    body = f"""{page_hero(['<a href="/">Início</a>', 'A Clínica'], 'Cardiologia e diagnóstico cardiovascular em Pelotas', 'Conheça a Clínica Procardíaco: tecnologia, precisão e acolhimento a serviço do coração dos pacientes de Pelotas e toda a região.')}
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal"><img src="/assets/img/about.webp" alt="Ambiente da Clínica Procardíaco" loading="lazy"></div>
      <div class="split__content reveal">
        <span class="eyebrow">Quem somos</span>
        <h2>Uma clínica dedicada ao seu coração</h2>
        <p class="lead">Somos uma clínica de diagnóstico cardiovascular, atuando em Pelotas-RS.</p>
        <p>Nossa clínica conta com instalações modernas e um ambiente acolhedor. Nossa força é, além da tecnologia dos equipamentos, a precisão e a experiência técnica da nossa equipe médica, promovendo diagnósticos com atenção à qualidade técnica dos exames e à clareza dos laudos.</p>
        <p>Nosso objetivo, além de cuidar da saúde dos pacientes, é atuar em equipe, colaborando com colegas médicos e proporcionando segurança nos resultados. Acreditamos que, desta maneira, contribuímos com o desenvolvimento da cardiologia na nossa região.</p>
        <div class="hero__cta" style="margin-top:28px;"><a class="btn btn--wa" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Falar no WhatsApp</a><a class="btn btn--ghost" href="/#equipe">Conheça a equipe</a></div>
      </div>
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Nossos valores</span><h2>O que nos torna referência</h2></div>
    <div class="grid grid-2" style="gap:30px;">{vhtml}</div>
  </div>
</section>
<section class="section section--navy cta-band">
  <div class="cta-band__glow"></div>
  <div class="container">
    <h2>Conte com a equipe da Procardíaco</h2>
    <p>Agende seu exame pelo WhatsApp e conte com uma equipe que une tecnologia, experiência e acolhimento.</p>
    <div class="hero__cta"><a class="btn btn--wa btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar pelo WhatsApp</a></div>
  </div>
</section>"""
    page("a-clinica-procardiaco/index.html", "A Clínica Procardíaco | Diagnóstico Cardiovascular em Pelotas",
         "Conheça a Clínica Procardíaco, clínica de cardiologia e diagnóstico cardiovascular em Pelotas-RS: instalações modernas, equipamentos de alta qualidade e equipe médica especializada.", body)

build_clinica()

# ============================================================================
#  EQUIPE
# ============================================================================
DOCS = [
 ("Dr. Daniel Ribeiro","/assets/img/dr-daniel.webp","Cardiologista · Ecocardiografista",
  "Mestre e Doutor em Cardiologia pelo Instituto de Cardiologia do Rio Grande do Sul e Professor Adjunto de Cardiologia da UFPel. Possui Especialização em Ecocardiografia pelo Instituto de Cardiologia do RS e Título de Especialista em Ecocardiografia pela Sociedade Brasileira de Cardiologia."),
 ("Dr. Eduardo Gehling Bertoldi","/assets/img/dr-eduardo.webp","Cardiologista · Ecocardiografista · Responsável Técnico",
  "Médico cardiologista e ecocardiografista, responsável técnico da clínica. Mestre e Doutor em Cardiologia pela UFRGS, é docente no Programa de Pós-Graduação em Cardiologia da UFRGS e professor associado da Faculdade de Medicina da UFPel."),
 ("Dr. Winder Marconsini Soares","/assets/img/dr-winder.jpg","Cardiologista · Ecocardiografista",
  "Médico cardiologista pelo Hospital de Base do Distrito Federal (IHBDF), com atuação dedicada à avaliação clínica cardiovascular dos pacientes da clínica."),
 ("Dr. Otávio Oliveira Guimarães","/assets/img/dr-otavio.jpg","Cardiologista · Ecocardiografista",
  "Médico formado pela Universidade Federal de Pelotas, com residência médica em Cardiologia e Ecocardiografia pelo Instituto de Cardiologia — Fundação Universitária de Cardiologia do Rio Grande do Sul (ICFUC)."),
]
def build_equipe():
    docs = "".join(
        f'<article class="doc reveal"><div class="doc__photo"><img src="{img}" alt="{n}" loading="lazy"></div><div class="doc__body"><h3>{n}</h3><p class="doc__role">{r}</p><p class="doc__bio">{b}</p></div></article>'
        for n,img,r,b in DOCS)
    body = f"""{page_hero(['<a href="/">Início</a>', 'Equipe'], 'Conheça a equipe da Clínica Procardíaco', 'Nossa equipe reúne médicos cardiologistas com atuação em avaliação clínica e diagnóstico cardiovascular, atendendo pacientes de Pelotas e região.')}
<section class="section">
  <div class="container">
    <div class="grid grid-4">{docs}</div>
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="split">
      <div class="split__content reveal">
        <span class="eyebrow">Por que escolher nossa equipe</span>
        <h2>Ciência, tecnologia e cuidado no mesmo lugar</h2>
        <p>Atualização científica contínua, uso de tecnologia de ponta e atendimento centrado no paciente fazem da Procardíaco referência na região.</p>
        <p><strong>Suporte humanizado:</strong> profissionais treinados em avaliação especializada cardiovascular completam o cuidado integral, do agendamento ao laudo.</p>
        <div class="hero__cta" style="margin-top:26px;"><a class="btn btn--wa" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar com a equipe</a></div>
      </div>
      <div class="split__media reveal"><img src="/assets/img/instalacao-2.webp" alt="Equipe da Clínica Procardíaco" loading="lazy"></div>
    </div>
  </div>
</section>"""
    page("equipe/index.html", "Equipe Médica | Clínica Procardíaco Pelotas",
         "Conheça a equipe médica da Clínica Procardíaco em Pelotas-RS: cardiologistas e ecocardiografistas com titulação pela SBC, UFPel, UFRGS e Instituto de Cardiologia do RS.", body)

build_equipe()

# ============================================================================
#  INSTALAÇÕES
# ============================================================================
def build_instalacoes():
    feats = [("monitor","Sala de ecocardiograma com imagem HD","Equipamentos com recursos de imagem digital e manutenção periódica. Os laudos são disponibilizados em formato físico e acesso digital."),
             ("heart","Ambiente dedicado ao Eco-Doppler vascular","Leitos ergonômicos e transdutores de alta qualidade para estudos de carótidas e membros inferiores."),
             ("users","Ambientes amplos e acessíveis","Rampas e portas largas facilitam o acesso para pessoas com mobilidade reduzida e idosos."),
             ("pulse","Sala climatizada para ECG, Holter e MAPA","Aparelhos digitais e interpretação por médicos altamente especializados."),
             ("pin","Estacionamento gratuito e fácil acesso","Vagas exclusivas na Rua Andrade Neves 4043, a menos de 200 metros da Av. Dom Joaquim."),
             ("doc","Tecnologia a serviço da sua saúde","Laudos e imagens podem ser acessados digitalmente por meio do portal de resultados e compartilhados com o médico assistente.")]
    fhtml = "".join(
        f'<div class="feature reveal"><div class="ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i,t,d in feats)
    body = f"""{page_hero(['<a href="/">Início</a>', 'Instalações'], 'Estrutura moderna para seu conforto e segurança', 'A Clínica Procardíaco atua em uma região de fácil acesso de Pelotas-RS para oferecer exames rápidos e precisos em um ambiente acolhedor e acessível.')}
<section class="section">
  <div class="container">
    <div class="gallery reveal" style="margin-bottom:56px;">
      <a href="#"><img src="/assets/img/instalacao-1.webp" alt="Instalações da clínica" loading="lazy"></a>
      <a href="#"><img src="/assets/img/instalacao-2.webp" alt="Sala de exames" loading="lazy"></a>
      <a href="#"><img src="/assets/img/instalacao-3.webp" alt="Recepção" loading="lazy"></a>
      <a href="#"><img src="/assets/img/instalacao-4.webp" alt="Ambiente de atendimento" loading="lazy"></a>
    </div>
    <div class="grid grid-2" style="gap:32px;">{fhtml}</div>
  </div>
</section>
<section class="section section--navy cta-band">
  <div class="cta-band__glow"></div>
  <div class="container">
    <h2>Venha nos conhecer em Pelotas</h2>
    <p>Agende seu exame pelo WhatsApp e conte com estrutura moderna, estacionamento gratuito e uma equipe pronta para atender você.</p>
    <div class="hero__cta"><a class="btn btn--wa btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar pelo WhatsApp</a><a class="btn btn--light btn--lg" href="/#contato">Ver localização</a></div>
  </div>
</section>"""
    page("instalacoes/index.html", "Instalações | Clínica Procardíaco Pelotas",
         "Conheça as instalações da Clínica Procardíaco em Pelotas-RS: salas de ecocardiograma em HD, ambientes acessíveis, estacionamento gratuito e acesso digital aos resultados.", body)

build_instalacoes()

# ============================================================================
#  CONVÊNIOS
# ============================================================================
CONV = ["Andaluz","Casembrapa","Cabergs","DS Saúde","Amor Saúde","ABAPP","Cartão de Todos",
 "Policlínica Pelotense","DescontSaúde","Canal Card","Segmed","Liga Operária","Master Desconto",
 "Vida Card","IPERGS","Pró-Vida","Docctor Med","Angelus","Pax","Policlínica Reunidas","Círculo Operário"]
def build_convenios():
    items = "".join(
        f'<div class="conv"><span class="tick">{IC["check"]}</span>{c}</div>' for c in CONV)
    body = f"""{page_hero(['<a href="/">Início</a>', 'Convênios'], 'Atendemos particular e diversos convênios', 'Para exames diagnósticos, realizamos atendimento particular e via convênios. A disponibilidade pode variar conforme o exame específico.')}
<section class="section">
  <div class="container">
    <div class="conv-grid reveal">{items}</div>
    <div class="info-box reveal" style="margin-top:34px; max-width:820px;">
      <h3>Importante</h3>
      <p>A disponibilidade do convênio pode variar em função do exame específico — por favor, entre em contato para maiores detalhes. Para <strong>consultas médicas</strong>, o atendimento é exclusivamente particular.</p>
    </div>
    <div style="text-align:center; margin-top:34px;">
      <a class="btn btn--wa btn--lg wa-direct" href="{wa('Olá! Gostaria de confirmar se meu convênio é atendido.')}" target="_blank" rel="noopener">{IC['wa']} Confirmar meu convênio</a>
    </div>
  </div>
</section>"""
    page("convenios/index.html", "Convênios Atendidos | Clínica Procardíaco Pelotas",
         "Veja os convênios atendidos na Clínica Procardíaco em Pelotas-RS para exames cardiológicos. Atendimento particular e via convênios — confirme o seu pelo WhatsApp.", body)

build_convenios()

# ============================================================================
#  CONTATO
# ============================================================================
def build_contato():
    body = f"""{page_hero(['<a href="/">Início</a>', 'Contato'], 'Localização e Contato', 'Estamos na Rua Andrade Neves, próximo à Av. Dom Joaquim, com estacionamento gratuito para pacientes. Consulte no mapa a melhor rota até a clínica.')}
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card reveal">
        <div class="contact-row"><div class="ic">{IC['pin']}</div><div><b>Endereço</b><span>Rua Andrade Neves 4043, sala 01 — Pelotas/RS</span></div></div>
        <div class="contact-row"><div class="ic">{IC['phone']}</div><div><b>Telefone</b><a href="tel:+555330277377">53 3027.7377</a></div></div>
        <div class="contact-row"><div class="ic">{IC['wa']}</div><div><b>WhatsApp</b><a href="{wa()}" target="_blank" rel="noopener">53 99143.1183</a></div></div>
        <div class="contact-row"><div class="ic">{IC['insta']}</div><div><b>Instagram</b><a href="https://www.instagram.com/procardiacopelotas" target="_blank" rel="noopener">@procardiacopelotas</a></div></div>
        <div class="contact-row"><div class="ic">{IC['clock']}</div><div><b>Horário de atendimento</b><span>Segunda a sexta, das 8h às 12h e das 13h30 às 17h30</span></div></div>
        <div style="margin-top:22px;"><a class="btn btn--wa btn--block btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar meu exame</a></div>
      </div>
      <iframe class="map-embed" src="https://www.google.com/maps?q=Rua%20Andrade%20Neves%204043%2C%20Pelotas%20-%20RS&output=embed" title="Mapa da Clínica Procardíaco" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>"""
    page("contato/index.html", "Localização e Contato | Clínica Procardíaco Pelotas",
         "Fale com a Clínica Procardíaco em Pelotas-RS: Rua Andrade Neves 4043, sala 01. Telefone 53 3027.7377, WhatsApp 53 99143.1183. Estacionamento gratuito e fácil acesso.", body)

build_contato()

# ============================================================================
#  CONSULTAS MÉDICAS
# ============================================================================
def build_consultas():
    faq = [("A consulta é particular ou por convênio?",
            "As consultas médicas são realizadas em atendimento exclusivamente particular. Os convênios se aplicam apenas aos exames diagnósticos — confirme os detalhes com a nossa equipe pelos meios de contato."),
           ("Preciso de pedido médico para consultar?",
            "Não. Você pode agendar diretamente com o cardiologista. Se já tiver exames ou pedidos anteriores, leve-os para enriquecer a avaliação."),
           ("Posso já fazer os exames no mesmo dia?",
            "Dependendo da avaliação e da disponibilidade de agenda, alguns exames podem ser realizados na própria clínica. Fale conosco para organizar tudo com antecedência."),
           ("Quando devo procurar um cardiologista?",
            "Em casos de dor no peito, falta de ar, palpitações, pressão alta, histórico familiar de doença cardíaca, ou simplesmente para uma avaliação preventiva. Mesmo sem sintomas, a avaliação pode ser útil quando existem fatores de risco cardiovascular, histórico familiar relevante ou dúvidas sobre prevenção.")]
    body = f"""{page_hero(['<a href="/">Início</a>', 'Consultas médicas'], 'Consulta com cardiologista em Pelotas', 'Avaliação cardiológica completa com especialistas titulados, em um ambiente acolhedor e com estrutura para realizar exames no mesmo local.')}
<section class="section">
  <div class="container">
    <div class="article-layout">
      <article class="prose reveal">
        <div class="article-media"><img src="/assets/img/about.webp" alt="Consulta cardiológica na Clínica Procardíaco" loading="lazy"></div>
        <h2>O que é a consulta cardiológica?</h2>
        <p>A consulta com o cardiologista é a porta de entrada para o cuidado com o coração. Nela, o médico realiza uma <strong>avaliação clínica completa</strong>: escuta a sua história, analisa sintomas e fatores de risco, examina você e, quando necessário, solicita ou já realiza exames complementares para chegar a um diagnóstico preciso.</p>
        <div class="info-box"><h3>Um cuidado que une avaliação e diagnóstico</h3><p>Na Clínica Procardíaco, a consulta se integra à nossa estrutura de diagnóstico. Isso significa que, muitas vezes, é possível <strong>avaliar e investigar no mesmo lugar</strong>, com agilidade e sem que você precise se deslocar para outra clínica.</p></div>
        <h2>Quando procurar um cardiologista?</h2>
        <ul>
        <li>Dor ou aperto no peito, falta de ar ou cansaço fora do comum;</li>
        <li>Palpitações, batimentos irregulares, tonturas ou desmaios;</li>
        <li>Pressão alta ou histórico familiar de doença cardiovascular;</li>
        <li>Diabetes, colesterol elevado, obesidade ou tabagismo;</li>
        <li>Avaliação cardiovascular antes de atividade física ou de procedimentos cirúrgicos;</li>
        <li>Avaliação preventiva — recomendada especialmente a partir dos 40 anos.</li>
        </ul>
        <div class="info-box info-box--alert"><h3>Observação</h3><p>Se a dor no peito for súbita ou intensa, ou estiver associada a falta de ar importante, suor frio, desmaio ou mal-estar intenso, <strong>não aguarde uma consulta eletiva: procure atendimento de urgência ou ligue 192.</strong></p></div>
        <h2>Como se preparar para a consulta</h2>
        <ul>
        <li>Leve um documento com foto e a lista dos medicamentos que utiliza;</li>
        <li>Traga exames e laudos anteriores, se houver;</li>
        <li>Anote suas dúvidas e os sintomas que deseja relatar;</li>
        <li>Em caso de cirurgia cardíaca prévia, leve a descrição do procedimento.</li>
        </ul>
        <h2>Atendimento particular</h2>
        <p>As <strong>consultas médicas são realizadas exclusivamente em atendimento particular</strong>. Os convênios que atendemos aplicam-se aos exames diagnósticos. Fale com a nossa equipe pelo WhatsApp ou telefone para conhecer valores, condições e a disponibilidade de horários.</p>
        {faq_block(faq)}
        {byline()}
      </article>
      <aside class="side">
        {cta_side("Olá! Gostaria de agendar uma consulta com cardiologista.", "Consulta com cardiologista", label="Agendar consulta", title="Agende sua consulta")}
        <div class="side-card">
          <h3>Também realizamos</h3>
          <div style="display:grid; gap:10px;">
            <a class="related-mini" href="/exames-realizados/"><div class="ic">{IC['pulse']}</div><div><b>Exames cardiológicos</b><span>Ver todos os exames</span></div></a>
            <a class="related-mini" href="/#equipe"><div class="ic">{IC['users']}</div><div><b>Nossa equipe</b><span>Conheça os cardiologistas</span></div></a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>
<section class="section section--navy cta-band">
  <div class="cta-band__glow"></div>
  <div class="container">
    <h2>Agende sua consulta cardiológica</h2>
    <p>Fale com a nossa equipe pelo WhatsApp e marque seu horário com um de nossos cardiologistas de forma rápida e sem complicação.</p>
    <div class="hero__cta"><a class="btn btn--wa btn--lg" data-exame="Consulta com cardiologista" href="{wa('Olá! Gostaria de agendar uma consulta com cardiologista.')}" target="_blank" rel="noopener">{IC['wa']} Agendar consulta</a>
    <a class="btn btn--light btn--lg" href="tel:+555330277377">Ligar: 53 3027.7377</a></div>
  </div>
</section>"""
    ld = faq_ld(faq)
    page("consultas-medicas/index.html", "Consulta com Cardiologista em Pelotas | Clínica Procardíaco",
         "Consulta com cardiologista em Pelotas-RS na Clínica Procardíaco: avaliação cardiológica completa com especialistas titulados e estrutura para exames no mesmo local. Agende pelo WhatsApp.", body, extra_ld=ld)

build_consultas()

print("\nOK — páginas internas geradas.")

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
      <a class="navlink" href="/#equipe">Equipe</a>
      <a class="navlink" href="/#instalacoes">Instalações</a>
      <a class="navlink" href="/#convenios">Convênios</a>
      <a class="navlink" href="/#contato">Contato</a>
      <a class="btn btn--magenta" href="https://resultados.clinicaprocardiaco.com" target="_blank" rel="noopener">Acessar exames</a>"""

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
        <p>Clínica de diagnóstico cardiovascular em Pelotas-RS. Tecnologia de última geração e equipe médica de referência a serviço do seu coração.</p>
        <div class="footer-social">
          <a href="https://www.instagram.com/procardiacopelotas" target="_blank" rel="noopener" aria-label="Instagram">{IC['insta']}</a>
          <a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{IC['wa']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Navegação</h4>
        <a href="/#sobre">A Clínica</a>
        <a href="/#exames">Exames</a>
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
    <div class="footer-bottom">
      <span>© 2026 Clínica Procardíaco — Diagnóstico Cardiovascular. Todos os direitos reservados.</span>
      <span>Pelotas / RS</span>
    </div>
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
<link rel="stylesheet" href="/assets/css/site.css">{ld}
</head>
<body>
{header()}
{body}
{footer()}
<script src="/assets/js/site.js" defer></script>
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

def cta_side(msg):
    return f"""<div class="side-card side-card--cta">
    <h3>Agende seu exame</h3>
    <p>Rápido e sem complicação, direto pela nossa equipe.</p>
    <a class="btn btn--wa btn--block" href="{wa(msg)}" target="_blank" rel="noopener">{IC['wa']} Falar no WhatsApp</a>
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

def side_facts(facts):
    rows = "\n".join(
        f'    <div class="side-fact"><div class="ic">{IC[i]}</div><div><b>{v}</b><span>{l}</span></div></div>'
        for i, l, v in facts)
    return f'<div class="side-card">\n    <h3>Resumo do exame</h3>\n{rows}\n  </div>'

# ============================================================================
#  EXAMES
# ============================================================================
EXAMS = [
 dict(slug="ecocardiograma", nome="Ecocardiograma",
   title="Ecocardiograma em Pelotas | Clínica Procardíaco",
   desc="Ecocardiograma (ultrassom do coração) em Pelotas-RS, com Doppler de alta resolução, laudo em até 1 hora e cardiologistas especialistas. Agende pelo WhatsApp.",
   img="/assets/img/exame-ecocardiograma.png",
   sub="O “ultrassom do coração”: avalia em tempo real as câmaras, válvulas, paredes e o fluxo sanguíneo, com segurança total e sem radiação.",
   facts=[("clock","Duração","20 a 30 min"),("no-fast","Preparo","Não exige jejum"),("doc","Laudo","Em até 1 hora"),("shield","Radiação","Não utiliza")],
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
<li>Hipertensão arterial de longa data;</li>
<li>Suspeita de insuficiência cardíaca (cansaço, inchaço nas pernas, falta de ar);</li>
<li>Doenças valvares (estenose ou insuficiência mitral, aórtica etc.);</li>
<li>Check-ups esportivos ou pré-operatórios;</li>
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

 dict(slug="ecg", nome="Eletrocardiograma (ECG)",
   title="Eletrocardiograma (ECG) em Pelotas | Clínica Procardíaco",
   desc="Eletrocardiograma (ECG) em Pelotas-RS: exame rápido, indolor e sem jejum, com laudo no mesmo dia por cardiologistas experientes. Agende pelo WhatsApp.",
   img="/assets/img/exame-ecg.jpg",
   sub="Exame simples, rápido e indolor que registra a atividade elétrica do coração e ajuda a diagnosticar arritmias, infarto e outras alterações.",
   facts=[("clock","Duração","5 a 10 min"),("no-fast","Preparo","Não precisa jejum"),("doc","Laudo","No mesmo dia"),("shield","Radiação","Não utiliza")],
   body="""<h2>O que é o eletrocardiograma?</h2>
<p>O ECG capta os pequenos impulsos elétricos que fazem o coração bater e os transforma em traçados (ondas P, QRS, T). Alterações na forma ou no intervalo dessas ondas podem indicar problemas de ritmo, isquemia (falta de sangue), aumento de cavidades cardíacas ou efeitos de medicamentos.</p>
<div class="info-box"><h3>Resumo rápido</h3><p><strong>Duração:</strong> 5 a 10 minutos. <strong>Não precisa de jejum.</strong> Resultado imediato impresso, com opção de acesso em PDF.</p></div>
<h2>Como o exame é feito, passo a passo</h2>
<ul>
<li><strong>Posicionamento:</strong> o paciente deita confortavelmente em decúbito dorsal;</li>
<li><strong>Eletrodos:</strong> dez adesivos descartáveis são colocados no peito, punhos e tornozelos, com gel condutor;</li>
<li><strong>Registro:</strong> o aparelho grava de 10 a 12 derivações em até 30 segundos;</li>
<li><strong>Impressão e laudo:</strong> o traçado sai na hora e o cardiologista avalia e assina o laudo.</li>
</ul>
<h2>Para que serve o ECG?</h2>
<ul>
<li>Detectar arritmias (taquicardia, fibrilação atrial, extrassístoles);</li>
<li>Avaliar dor no peito e ajudar a identificar infarto agudo;</li>
<li>Check-up de rotina, sobretudo em diabéticos, hipertensos e atletas;</li>
<li>Controle de marcapasso;</li>
<li>Pré-operatório, garantindo segurança antes de cirurgias.</li>
</ul>
<h2>Diferenciais na Clínica Procardíaco</h2>
<ul>
<li>Equipamento digital de alta resolução, com filtros para reduzir artefatos;</li>
<li>Equipe titulada pela Sociedade Brasileira de Cardiologia;</li>
<li>Agilidade: exame e laudo em menos de 1 hora;</li>
<li>Resultado em PDF que pode ser enviado por e-mail ou anexado ao prontuário eletrônico.</li>
</ul>""",
   faq=[("Precisa de preparo especial?","Não. Basta chegar alguns minutos antes e trazer documento com foto e, se possível, a lista de medicamentos."),
        ("O exame dói ou causa choque?","Não. Os eletrodos apenas captam a eletricidade natural do coração; nada é injetado no corpo."),
        ("Gestantes podem fazer?","Sim. O ECG é totalmente seguro em qualquer fase da gestação, pois não usa radiação."),
        ("Qual a diferença entre ECG e Teste Ergométrico?","O ECG de repouso é feito deitado e avalia ritmo e estrutura elétrica básica. O Teste Ergométrico registra o ECG durante esforço (esteira), revelando isquemia que só aparece com exercício.")]),

 dict(slug="holter-e-mapa", nome="Holter e MAPA",
   title="Holter (24h a 7 dias) e MAPA em Pelotas | Clínica Procardíaco",
   desc="Holter (24h a 7 dias) e MAPA em Pelotas-RS: monitorização do ritmo cardíaco e da pressão arterial com equipamentos digitais e laudo por cardiologista. Agende pelo WhatsApp.",
   img="/assets/img/exame-holter.jpg",
   sub="Alguns problemas do coração só aparecem fora do consultório. O MAPA e o Holter registram sua pressão e seu ritmo cardíaco no dia a dia, revelando o que a consulta não capta.",
   facts=[("cal","Duração","24h a 7 dias"),("no-fast","Preparo","Sem jejum"),("doc","Laudo","MAPA em 24h · Holter 2–4 dias"),("shield","Radiação","Não utiliza")],
   body="""<h2>Em resumo</h2>
<div class="info-box"><p><strong>MAPA:</strong> mede a pressão a cada 15–30 minutos por 24 horas. <strong>Holter:</strong> grava o eletrocardiograma de forma contínua — oferecemos de 24 horas a 7 dias de monitorização. Laudo com envio por e-mail e WhatsApp.</p></div>
<h2>O que é o MAPA?</h2>
<p>MAPA significa <strong>Monitorização Ambulatorial da Pressão Arterial</strong>. É um pequeno aparelho preso à cintura, conectado a uma braçadeira que infla automaticamente em horários programados (geralmente a cada 20 min de dia e 30 min à noite), gravando todas as medições.</p>
<p><strong>Para que serve:</strong> diagnosticar hipertensão mascarada, confirmar a hipertensão do avental branco, avaliar o controle real da pressão em pacientes tratados e identificar padrões noturnos de risco.</p>
<h2>O que é o Holter?</h2>
<p>O Holter é um aparelho portátil que grava o eletrocardiograma continuamente. O exame tradicional dura 24 horas, mas oferecemos também monitores de <strong>2, 3, 5 e 7 dias</strong> para flagrar arritmias que não ocorrem diariamente. Nosso dispositivo é <strong>à prova d'água</strong>, permitindo banho de chuveiro e atividade física conforme orientação da equipe.</p>
<p><strong>Para que serve:</strong> detectar arritmias intermitentes, investigar tonturas, desmaios e palpitações sem causa aparente, avaliar a eficácia de medicamentos ou de marcapasso e monitorar o pós-infarto ou pós-ablação.</p>
<h2>MAPA vs. Holter</h2>
<ul>
<li><strong>MAPA</strong> — mede a pressão arterial; inflagens automáticas; indicado para hipertensão.</li>
<li><strong>Holter</strong> — mede o ritmo elétrico do coração; gravação contínua de ECG; indicado para arritmias.</li>
<li>Ambos podem ser realizados <strong>simultaneamente</strong>, se necessário, para correlacionar pressão e ritmo.</li>
</ul>
<h2>Diferenciais na Clínica Procardíaco</h2>
<ul>
<li>Equipamentos digitais de última geração, incluindo Holter à prova d'água com calibração certificada;</li>
<li>Instalação por enfermeiro treinado e laudo por cardiologista especialista;</li>
<li>Relatório detalhado com gráficos, histogramas e correlação de sintomas;</li>
<li>Suporte via WhatsApp para dúvidas durante a monitorização.</li>
</ul>""",
   faq=[("Preciso de preparo?","Não há jejum. Vista uma blusa sem mangas justas para facilitar o manguito ou os eletrodos e traga a lista de medicamentos."),
        ("Posso trabalhar e dirigir?","Sim. Só evite atividades de alto impacto ou esportes aquáticos durante o período de monitorização."),
        ("O exame dói?","O inflar do MAPA pode apertar o braço por alguns segundos. O Holter não causa dor; pode haver leve coceira onde ficam os eletrodos."),
        ("Quando recebo o resultado?","MAPA: laudo em 24h úteis. Holter: 2 dias úteis para 24h e até 4 dias úteis para gravações maiores. Você recebe impresso e em PDF.")]),

 dict(slug="eco-carotidas-vertebrais", nome="Eco-Doppler de Carótidas e Vertebrais",
   title="Eco-Doppler de Carótidas e Vertebrais em Pelotas | Procardíaco",
   desc="Eco-Doppler de carótidas e vertebrais em Pelotas-RS: exame indolor e sem radiação que avalia o fluxo nas artérias do pescoço e o risco de AVC. Agende pelo WhatsApp.",
   img="/assets/img/exame-carotidas.webp",
   sub="Exame de ultrassom indolor e sem radiação que avalia em tempo real o fluxo de sangue nas artérias do pescoço e identifica placas que aumentam o risco de AVC.",
   facts=[("clock","Duração","20 a 30 min"),("no-fast","Preparo","Geralmente sem jejum"),("doc","Laudo","Logo após o exame"),("shield","Radiação","Não utiliza")],
   body="""<h2>O que é o Eco-Doppler de Carótidas e Vertebrais?</h2>
<p>O exame combina duas tecnologias: a <strong>ultrassonografia convencional</strong>, que gera imagens anatômicas das artérias, e o <strong>efeito Doppler</strong>, que mostra em cores a direção e a velocidade do fluxo sanguíneo. Com um pequeno transdutor apoiado sobre a pele, o especialista visualiza todo o trajeto das artérias carótidas e vertebrais, detectando placas ou estenoses com precisão.</p>
<h2>Por que devo fazer este exame?</h2>
<p><strong>Principais fatores de risco:</strong> hipertensão arterial, colesterol ou triglicerídeos elevados, diabetes, tabagismo e histórico familiar de AVC ou doença coronariana.</p>
<div class="info-box"><h3>Sintomas de alerta</h3><p>Tontura, perda súbita de visão em um olho, formigamentos em braço ou perna e dificuldade para falar ou compreender podem indicar redução do fluxo sanguíneo ao cérebro e justificam a investigação.</p></div>
<h2>Como o exame é realizado?</h2>
<p>Você deita confortavelmente em uma maca, o médico aplica um gel à base de água no pescoço e desliza o transdutor levemente. <strong>Não há dor, agulhas ou radiação.</strong> O procedimento dura de 20 a 30 minutos e o resultado costuma ser liberado logo após a avaliação.</p>
<h2>Preciso de algum preparo?</h2>
<p>Na maioria dos casos não é necessário jejum. Use roupas que permitam acesso fácil ao pescoço e traga exames prévios. Pacientes que usam colar cervical devem avisar a equipe com antecedência.</p>
<h2>Resultados e próximos passos</h2>
<p>Se forem detectadas placas ou estreitamentos, o médico discutirá mudanças no estilo de vida, ajuste de medicamentos ou, em casos selecionados, procedimentos para abrir a artéria. Nosso serviço segue as recomendações da <em>Society for Cardiovascular Angiography &amp; Interventions</em> e da Sociedade Brasileira de Cardiologia.</p>""",
   faq=[("O exame dói?","Não. O Eco-Doppler é indolor e não invasivo."),
        ("Há riscos?","É considerado seguro para todas as idades, pois não usa radiação ionizante."),
        ("Com que frequência devo repetir?","Depende do seu perfil de risco. Placas significativas podem exigir repetição anual; exames normais costumam ser repetidos a cada 3–5 anos ou conforme orientação médica.")]),

 dict(slug="eco-mmii", nome="Eco-Doppler de Membros Inferiores",
   title="Eco-Doppler de Membros Inferiores em Pelotas | Procardíaco",
   desc="Eco-Doppler de membros inferiores em Pelotas-RS: avalia veias e artérias das pernas para diagnosticar varizes, trombose (TVP) e obstruções arteriais. Agende pelo WhatsApp.",
   img="/assets/img/exame-mmii.webp",
   sub="Ultrassom que avalia o fluxo sanguíneo em veias e artérias das pernas, ajudando a diagnosticar varizes, trombose venosa profunda (TVP) e obstruções arteriais.",
   facts=[("clock","Duração","25 a 35 min"),("no-fast","Preparo","Geralmente sem jejum"),("doc","Laudo","Logo após o exame"),("shield","Radiação","Não utiliza")],
   body="""<h2>O que é o Eco-Doppler de membros inferiores?</h2>
<p>O exame combina a ultrassonografia convencional, que fornece imagens anatômicas, com a tecnologia Doppler, capaz de mostrar a velocidade e a direção do sangue em tempo real. Assim, identifica compressões, estreitamentos ou refluxo nas principais veias e artérias das pernas.</p>
<h2>Por que meu médico solicitou esse exame?</h2>
<ul>
<li><strong>Varizes</strong> — avaliar refluxo venoso antes de cirurgia ou escleroterapia;</li>
<li><strong>Trombose venosa profunda (TVP)</strong> — confirmar a presença de coágulos;</li>
<li><strong>Doença arterial periférica</strong> — investigar obstrução que causa dor ao caminhar;</li>
<li><strong>Pós-operatório vascular</strong> — checar enxertos ou stents.</li>
</ul>
<h2>Como o exame é feito?</h2>
<p>Você permanece deitado(a) ou em pé, conforme a fase do exame. O especialista aplica gel nas pernas e desliza suavemente o transdutor, obtendo imagens e escutando o fluxo sanguíneo. <strong>Não há dor, anestesia ou efeitos colaterais.</strong> O procedimento dura de 25 a 35 minutos e o laudo costuma ser entregue logo após a avaliação.</p>
<h2>Preciso de preparo?</h2>
<p>Geralmente não há necessidade de jejum. Use roupas confortáveis que possam ser erguidas acima do joelho. Se usa meias elásticas, traga-as para vestir depois do exame.</p>
<h2>Resultados e próximos passos</h2>
<p>O laudo indicará se há refluxo venoso, trombose ou obstruções arteriais. O tratamento pode variar de meias de compressão e medicamentos até procedimentos como laser endovenoso ou angioplastia. Todas as condutas seguem as diretrizes da Sociedade Brasileira de Angiologia e Cirurgia Vascular.</p>""",
   faq=[("O exame dói?","Não. Você sentirá apenas o contato do transdutor e do gel sobre a pele."),
        ("Há riscos ou radiação?","Não há radiação ionizante. É seguro para gestantes, crianças e pessoas com marcapasso."),
        ("Quando devo repetir?","Varizes são monitoradas conforme os sintomas; trombose pode exigir acompanhamento em 3 a 6 meses. Siga a orientação médica."),
        ("Qual a diferença entre ultrassom vascular e Doppler comum?","O Doppler comum avalia o fluxo em uma única região; o Eco-Doppler vascular inclui o mapeamento completo de veias e artérias, com medidas de velocidade e pressão.")]),

 dict(slug="eco-te", nome="Ecocardiograma Transesofágico",
   title="Ecocardiograma Transesofágico (ETE) em Pelotas | Procardíaco",
   desc="Ecocardiograma transesofágico (ETE) em Pelotas-RS: imagens de altíssima resolução do coração a partir do esôfago, com sedação leve e segurança. Agende pelo WhatsApp.",
   img="/assets/img/exame-transesofagico.webp",
   sub="Exame de ultrassom avançado que obtém imagens detalhadas do coração a partir do esôfago, ideal para avaliar válvulas, trombos e o pré-operatório cardíaco.",
   facts=[("clock","Duração","15 a 25 min"),("no-fast","Preparo","Jejum de 6 horas"),("doc","Laudo","Em até 1 hora"),("users","Sedação","Leve, com acompanhante")],
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
<li>O transdutor é introduzido cuidadosamente enquanto você respira pelo nariz;</li>
<li>Durante 15 a 25 minutos, são capturadas imagens sob diferentes ângulos;</li>
<li>Após o exame, você permanece em observação por cerca de 30 minutos e recebe alta com acompanhante.</li>
</ul>
<div class="info-box"><h3>Preparo especial</h3><p>Jejum absoluto de alimentos e líquidos por <strong>6 horas</strong>. Informe alergias e medicamentos, especialmente anticoagulantes. Traga acompanhante, pois a sedação impede conduzir veículos por 12 horas.</p></div>
<p>A maioria dos pacientes relata apenas leve pressão na garganta. Complicações são raras. Seguimos os protocolos da <em>European Society of Cardiology</em>, com monitorização contínua.</p>""",
   faq=[("Quanto tempo leva para sair o resultado?","O cardiologista analisa logo após o exame; o laudo costuma ficar pronto em até 1 hora."),
        ("Posso continuar meus remédios?","Sim, exceto anticoagulantes e antiplaquetários, que podem ser ajustados pelo seu médico. Leve sua lista completa de medicações."),
        ("Existe alternativa ao ETE?","Em alguns casos, a tomografia ou a ressonância cardíaca oferecem dados complementares, mas nenhuma fornece as imagens valvares dinâmicas em tempo real do ETE."),
        ("O exame dói? Há riscos?","A maioria sente apenas leve pressão na garganta. A sedação consciente mantém você confortável. Complicações são muito raras.")]),
]

EXAM_ICON = {"ecocardiograma":"heart","ecg":"pulse","holter-e-mapa":"cal",
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
        {side_facts(e['facts'])}
        {cta_side(f"Olá! Gostaria de agendar um(a) {e['nome']}.")}
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
    tags = {"holter-e-mapa": "24h a 7 dias"}
    for e in EXAMS:
        tag = f'<span class="card__tag">{tags[e["slug"]]}</span>' if e["slug"] in tags else ""
        cards += f"""      <a class="card reveal" href="/exames-realizados/{e['slug']}/">
        {tag}<div class="card__media"><img src="{e['img']}" alt="{e['nome']}" loading="lazy"></div>
        <div class="card__body"><h3>{e['nome']}</h3><p>{e['sub']}</p>
        <span class="card__link">Saiba mais {IC['arrow']}</span></div>
      </a>\n"""
    body = f"""{page_hero(['<a href="/">Início</a>', 'Serviços'], 'Exames cardiológicos completos, em um só lugar', 'Nossos exames são realizados com excelência e responsabilidade. Nos preocupamos com a assertividade dos resultados e o bem-estar dos nossos pacientes.')}
<section class="section">
  <div class="container">
    <div class="grid grid-3">
{cards}    </div>
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
         "Ecocardiograma, ECG, Holter, MAPA e Eco-Doppler em Pelotas-RS. Exames cardiológicos de alta precisão com laudo rápido e equipe especialista. Agende pelo WhatsApp.", body)

build_servicos()

# ============================================================================
#  A CLÍNICA
# ============================================================================
def build_clinica():
    vals = [("shield","Segurança nos resultados","Precisão técnica que apoia decisões e procedimentos médicos complexos."),
            ("pulse","Tecnologia de ponta","Equipamentos de última geração, com calibrações periódicas rigorosas."),
            ("users","Atuação em equipe","Colaboramos com colegas médicos, fortalecendo a cardiologia da região."),
            ("heart","Cuidado humanizado","Ambiente acolhedor e atendimento centrado no bem-estar do paciente.")]
    vhtml = "".join(
        f'<div class="feature reveal"><div class="ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i,t,d in vals)
    body = f"""{page_hero(['<a href="/">Início</a>', 'A Clínica'], 'Referência em diagnóstico cardiovascular na Zona Sul', 'Conheça a Clínica Procardíaco: tecnologia, precisão e acolhimento a serviço do coração dos pacientes de Pelotas e toda a região.')}
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal"><img src="/assets/img/about.webp" alt="Ambiente da Clínica Procardíaco" loading="lazy"></div>
      <div class="split__content reveal">
        <span class="eyebrow">Quem somos</span>
        <h2>Uma clínica dedicada ao seu coração</h2>
        <p class="lead">Somos uma clínica de diagnóstico cardiovascular, atuando como referência na Zona Sul do estado.</p>
        <p>Nossa clínica conta com instalações modernas e um ambiente acolhedor. Nossa força é, além da tecnologia dos equipamentos, a precisão e a experiência técnica da nossa equipe médica, promovendo diagnósticos altamente precisos.</p>
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
    <h2>Venha cuidar do seu coração com quem é referência</h2>
    <p>Agende seu exame pelo WhatsApp e conte com uma equipe que une tecnologia, experiência e acolhimento.</p>
    <div class="hero__cta"><a class="btn btn--wa btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar pelo WhatsApp</a></div>
  </div>
</section>"""
    page("a-clinica-procardiaco/index.html", "A Clínica Procardíaco | Diagnóstico Cardiovascular em Pelotas",
         "Conheça a Clínica Procardíaco, referência em diagnóstico cardiovascular na Zona Sul do RS: instalações modernas, tecnologia de ponta e equipe médica especializada em Pelotas.", body)

build_clinica()

# ============================================================================
#  EQUIPE
# ============================================================================
DOCS = [
 ("Dr. Daniel Ribeiro","/assets/img/dr-daniel.webp","Cardiologista · Ecocardiografista",
  "Mestre e Doutor em Cardiologia pelo Instituto de Cardiologia do Rio Grande do Sul e Professor Adjunto de Cardiologia da UFPel. Possui Especialização em Ecocardiografia pelo Instituto de Cardiologia do RS e Título de Especialista em Ecocardiografia pela Sociedade Brasileira de Cardiologia."),
 ("Dr. Eduardo Bertoldi","/assets/img/dr-eduardo.webp","Cardiologista · Responsável Técnico",
  "Médico cardiologista e ecocardiografista, responsável técnico da clínica. Mestre e Doutor em Cardiologia pela UFRGS, é docente no Programa de Pós-Graduação em Cardiologia da UFRGS e professor associado da Faculdade de Medicina da UFPel."),
 ("Dr. Winder Marconsini Soares","/assets/img/dr-winder.jpg","Cardiologista",
  "Médico cardiologista pelo Hospital de Base do Distrito Federal (IHBDF), com atuação dedicada à avaliação clínica cardiovascular dos pacientes da clínica."),
 ("Dr. Otávio Oliveira Guimarães","/assets/img/dr-otavio.jpg","Cardiologista · Ecocardiografista",
  "Médico formado pela Universidade Federal de Pelotas, com residência médica em Cardiologia e Ecocardiografia pelo Instituto de Cardiologia — Fundação Universitária de Cardiologia do Rio Grande do Sul (ICFUC)."),
]
def build_equipe():
    docs = "".join(
        f'<article class="doc reveal"><div class="doc__photo"><img src="{img}" alt="{n}" loading="lazy"></div><div class="doc__body"><h3>{n}</h3><p class="doc__role">{r}</p><p class="doc__bio">{b}</p></div></article>'
        for n,img,r,b in DOCS)
    body = f"""{page_hero(['<a href="/">Início</a>', 'Equipe'], 'Conheça a equipe da Clínica Procardíaco', 'Nossa equipe médica é técnica, especializada e experiente. Trabalhamos em Pelotas-RS, com cobertura de toda a região.')}
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
        <p>Atualização científica contínua, uso de tecnologia de ponta e atendimento centrado no paciente fazem da Procardíaco referência na Zona Sul do RS.</p>
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
    feats = [("monitor","Sala de ecocardiograma com imagem HD","Aparelhos modernos, com revisões e calibrações periódicas rigorosas, que permitem laudo digital em até 1 hora."),
             ("heart","Ambiente dedicado ao Eco-Doppler vascular","Leitos ergonômicos e transdutores de alta frequência para estudos de carótidas e membros inferiores."),
             ("users","Ambientes amplos e acessíveis","Rampas e portas largas garantem mobilidade para pessoas com deficiência e idosos."),
             ("pulse","Sala climatizada para ECG, Holter e MAPA","Aparelhos digitais de última geração e interpretação por médicos altamente especializados."),
             ("pin","Estacionamento gratuito e fácil acesso","Vagas exclusivas na Rua Andrade Neves 4043, a menos de 200 metros da Av. Dom Joaquim."),
             ("doc","Tecnologia a serviço da sua saúde","Integração de resultados via prontuário eletrônico: seu médico visualiza laudos e imagens online.")]
    fhtml = "".join(
        f'<div class="feature reveal"><div class="ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i,t,d in feats)
    body = f"""{page_hero(['<a href="/">Início</a>', 'Instalações'], 'Estrutura moderna para seu conforto e segurança', 'A Clínica Procardíaco atua em uma das melhores regiões de Pelotas-RS para oferecer exames rápidos e precisos em um ambiente acolhedor e acessível.')}
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
         "Conheça as instalações da Clínica Procardíaco em Pelotas-RS: salas de ecocardiograma em HD, ambientes acessíveis, estacionamento gratuito e tecnologia de ponta.", body)

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
      <a class="btn btn--wa btn--lg" href="{wa('Olá! Gostaria de confirmar se meu convênio é atendido.')}" target="_blank" rel="noopener">{IC['wa']} Confirmar meu convênio</a>
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
    body = f"""{page_hero(['<a href="/">Início</a>', 'Contato'], 'Localização e Contato', 'Pelotas é referência em saúde para toda a Zona Sul e recebe pacientes das cidades da região. Estamos em uma das melhores regiões da cidade, com fácil acesso e estacionamento gratuito.')}
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card reveal">
        <div class="contact-row"><div class="ic">{IC['pin']}</div><div><b>Endereço</b><span>Rua Andrade Neves 4043, sala 01 — Pelotas/RS</span></div></div>
        <div class="contact-row"><div class="ic">{IC['phone']}</div><div><b>Telefone</b><a href="tel:+555330277377">53 3027.7377</a></div></div>
        <div class="contact-row"><div class="ic">{IC['wa']}</div><div><b>WhatsApp</b><a href="{wa()}" target="_blank" rel="noopener">53 99143.1183</a></div></div>
        <div class="contact-row"><div class="ic">{IC['insta']}</div><div><b>Instagram</b><a href="https://www.instagram.com/procardiacopelotas" target="_blank" rel="noopener">@procardiacopelotas</a></div></div>
        <div class="contact-row"><div class="ic">{IC['clock']}</div><div><b>Horário de atendimento</b><span>Segunda a sexta, das 8h às 12h e das 14h às 18h</span></div></div>
        <div style="margin-top:22px;"><a class="btn btn--wa btn--block btn--lg" href="{wa()}" target="_blank" rel="noopener">{IC['wa']} Agendar meu exame</a></div>
      </div>
      <iframe class="map-embed" src="https://www.google.com/maps?q=Rua%20Andrade%20Neves%204043%2C%20Pelotas%20-%20RS&output=embed" title="Mapa da Clínica Procardíaco" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>"""
    page("contato/index.html", "Localização e Contato | Clínica Procardíaco Pelotas",
         "Fale com a Clínica Procardíaco em Pelotas-RS: Rua Andrade Neves 4043, sala 01. Telefone 53 3027.7377, WhatsApp 53 99143.1183. Estacionamento gratuito e fácil acesso.", body)

build_contato()

print("\nOK — páginas internas geradas.")

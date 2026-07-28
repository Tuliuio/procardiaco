# Clínica Procardíaco — Site

Site institucional estático da **Clínica Procardíaco Pelotas** (diagnóstico cardiovascular).
One Page moderna, focada em conversão, com páginas internas de conteúdo aprofundado (exames, equipe, convênios etc.).

## Stack

100% estático — HTML + CSS + JS puro, sem dependências de build para servir. Fontes via Google Fonts (Figtree + Noto Sans).

## Estrutura

```
index.html                      # One Page (home)
a-clinica-procardiaco/          # Sobre a clínica
equipe/                         # Equipe médica
instalacoes/                    # Instalações
convenios/                      # Convênios atendidos
contato/                        # Localização e contato
exames-realizados/              # Serviços (índice) + páginas de cada exame
  ├── ecocardiograma/
  ├── ecg/
  ├── holter-e-mapa/
  ├── eco-carotidas-vertebrais/
  ├── eco-mmii/
  └── eco-te/
assets/
  ├── css/site.css              # Design system
  ├── js/site.js                # Interações (menu, header, animações)
  └── img/                      # Imagens
sitemap.xml · robots.txt
build_pages.py                  # Gerador das páginas internas (opcional)
```

## Rodar localmente

```bash
python3 -m http.server 8787
```

Acesse http://localhost:8787

## Regenerar páginas internas

O conteúdo das páginas internas é gerado por `build_pages.py` (header/footer compartilhados + conteúdo por página):

```bash
python3 build_pages.py
```

## Agendamento + rastreamento de leads

Os botões de "Agendar" abrem um **modal de pré-agendamento** (exame, preferência de dia/período, nome) e, ao confirmar, abrem o WhatsApp com a mensagem já pronta. Sem JavaScript, os botões continuam indo direto ao WhatsApp (progressive enhancement).

Cada confirmação pode ser **registrada numa planilha do Google Sheets** (sem backend), com os parâmetros de campanha (UTM) para análise de anúncios.

### Como ativar a captura de leads

1. Crie uma planilha no Google Sheets.
2. **Extensões → Apps Script**, cole o conteúdo de [`apps-script.gs`](apps-script.gs) e salve.
3. **Implantar → Nova implantação → App da Web** — *Executar como: Eu*, *Quem pode acessar: Qualquer pessoa*. Autorize.
4. Copie a URL do App da Web e cole em `assets/js/site.js`, na variável `LEAD_ENDPOINT`:
   ```js
   var LEAD_ENDPOINT = "https://script.google.com/macros/s/XXXXX/exec";
   ```
5. Pronto. Cada lead vira uma linha na aba **Leads** com: data/hora, exame, preferência, nome, origem, página, UTMs e referrer.

> Enquanto `LEAD_ENDPOINT` estiver vazio, o site funciona normalmente — apenas não registra os leads.

**Dica de anúncios:** links de campanha com `?utm_source=...&utm_campaign=...` são capturados automaticamente e persistem entre páginas, permitindo cruzar cada lead com o anúncio que o gerou.

## Deploy

Como é um site estático, pode ser hospedado em qualquer serviço (GitHub Pages, Netlify, Vercel, Cloudflare Pages) apontando a raiz do repositório.

---

© Clínica Procardíaco — Diagnóstico Cardiovascular · Pelotas/RS

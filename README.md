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

## Deploy

Como é um site estático, pode ser hospedado em qualquer serviço (GitHub Pages, Netlify, Vercel, Cloudflare Pages) apontando a raiz do repositório.

---

© Clínica Procardíaco — Diagnóstico Cardiovascular · Pelotas/RS

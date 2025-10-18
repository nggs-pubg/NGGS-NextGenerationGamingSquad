# Contexto Atual do Projeto NGGS (Codex)

## Visão Geral
- Repositório estruturado para site estático com **MkDocs Material** e conteúdo em PT-BR.
- Foco em jogadores de FPS (PUBG), enfatizando **fair play** e otimizações legítimas (PC, GPU, mouse, táticas).
- Projeto aplicado com guias modulares (`docs/`), automações em Python (`scripts/`), testes (`tests/`) e pipeline CI/CD.

## Estrutura de Pastas
```
nggs/
├─ docs/                 # Conteúdo MkDocs (Markdown + assets)
│  ├─ assets/images/     # Logos NGGS e hero background
│  ├─ assets/css/        # custom.css com tema UX novo
│  ├─ comunidade/        # CTA Discord com regras
│  ├─ pc/, gpu/, mouse/  # Guias técnicos com Descrição/Por que/Como reverter/Impacto
│  └─ pubg/              # Guia geral, anexos e template de arma
├─ scripts/              # Utilitários Python (Typer CLI + generators + helpers)
│  ├─ cli.py             # Comandos `nggs gen weapon` e `nggs calc edpi`
│  ├─ generators/        # `weapons.py`, `tables.py`
│  ├─ templates/         # `arma_template.md.j2`
│  └─ utils/             # `math.py`, `files.py`
├─ tests/                # pytest com `conftest.py`, cobertura de math/generators
├─ mkdocs.yml            # Navegação hierárquica + tema customizado + extra CSS
├─ pyproject.toml        # Packaging + black/isort/ruff/pytest/mypy config
├─ requirements.txt      # Dependências (MkDocs, Typer, lint, tests)
├─ .github/workflows/    # CI/CD com lint + tests + build + deploy (GitHub Pages)
├─ README.md             # Onboarding CLI, política anti-cheat, contribuição
├─ tests/instruções.md   # Passo a passo para compilar/testar localmente
├─ ai-instruction.md     # (este arquivo)
└─ legacy_site/          # Site anterior em HTML/CSS (referência)
```

## Design & UX
- Home (`docs/index.md`) redesenhada com hero dinâmico, CTAs, estatísticas e cards temáticos.
- `custom.css` define paleta dark neon, efeitos de blur, cards responsivos, tipografia Oswald/Montserrat.
- Imagens NGGS reutilizadas como hero/backgrounds decorativos.
- Nav com abas e sub-abas refletindo as categorias principais.

## Automação & Qualidade
- CLI usa **Typer**; comandos principais:
  - `nggs gen weapon --nome "Beryl" --tipo AR --saida docs/pubg/armas/`
  - `nggs calc edpi --dpi 800 --sens 1.2 --saida docs/mouse/calculadora.md`
- Funções matemáticas com type hints (`calc_edpi`, `calc_360_distance_cm`).
- Templating via **Jinja2**; arquivos gravados com backup `.bak` automático.
- Testes (`pytest`) cobrem cálculos e geração de arquivos; `conftest` injeta raiz no `sys.path`.
- Lint/format: **ruff**, **black**, **isort**, **mypy** (gradual). Pipelines executam tudo antes de publicar.

## Conteúdo e Diretrizes
- Todas as páginas enfatizam política anti-cheat, reversão de ajustes e impacto esperado.
- Página `comunidade/discord.md` possui CTA com placeholder de convite e reforço de regras.
- `sobre.md` destaca fontes oficiais (Microsoft, NVIDIA, AMD, Krafton) e processo de contribuição.
- Conteúdo em `docs/pc`, `docs/gpu`, `docs/mouse`, `docs/pubg` segue formato padronizado.

## Build/Teste Local
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt && pip install -e .`
3. `ruff check --output-format=github .`
4. `black --check .`
5. `isort --check-only .`
6. `pytest -q`
7. `mkdocs build --strict` (gera `site/`)
8. `mkdocs serve` para preview em `localhost:8000`

## Próximos Pontos Potenciais
- Definir link oficial do Discord (substituir placeholder).
- Adicionar métricas reais/atualizadas nas seções hero e estatísticas.
- Conectar formulário de contato/lead se necessário (hoje CLI focada em conteúdo).
- Avaliar se o conteúdo do `legacy_site/` deve ser migrado ou removido após validação.

Este resumo reflete o entendimento atual da estrutura, ferramentas e diretrizes do projeto NGGS para continuidade das otimizações.

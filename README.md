# NGGS — Site e Utilitários

Repositório oficial da NGGS para documentação técnica baseada em MkDocs e automações em Python. O foco é ajudar jogadores de PUBG (e FPS em geral) a otimizar hardware, software e rotina de treino mantendo **fair play absoluto**.

## Estrutura

```
nggs/
├─ docs/                   # Conteúdo em Markdown consumido pelo MkDocs
├─ scripts/                # CLI e geradores em Python (Typer + Jinja2)
├─ tests/                  # Testes automatizados (pytest)
├─ mkdocs.yml              # Configuração do site (tema, navegação)
├─ pyproject.toml          # Lint, formatação, dependências
├─ requirements.txt        # Dependências mínimas para CI/CLI
└─ .github/workflows/      # Pipeline de CI/CD
```

## Requisitos

- Python 3.10 ou superior
- Pip, venv (ou Poetry/pipx se preferir)

Instalação local:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## CLI (`nggs`)

A CLI usa [Typer](https://typer.tiangolo.com/) e fica disponível após `pip install -e .`.

### Gerar páginas de armas

```bash
nggs gen weapon --nome "Beryl M762" --tipo AR --saida docs/pubg/armas/
```

Parâmetros opcionais: `--funcao`, `--cano`, `--empunhadura`, `--municao`, `--otica`.

### Atualizar calculadora de eDPI

```bash
nggs calc edpi --dpi 800 --sens 1.2 --saida docs/mouse/calculadora.md
```

Use `--yaw` para jogos com valor diferente do PUBG (padrão `0.0025`). A CLI cria backup `.bak` antes de sobrescrever o arquivo.

## Desenvolvimento

- `ruff --output-format=github .`
- `black .`
- `isort .`
- `pytest`
- `mkdocs serve`

O pipeline de CI executa todas as etapas acima e publica em GitHub Pages (`main`).

## Política anti-cheat

A NGGS não apoia, distribui ou aceita: no-recoil scripts, macros, bots, automações ou modificações ilegais. Trabalhamos apenas com fontes oficiais (Microsoft, NVIDIA, AMD, Krafton) e focamos em melhorias legítimas de hardware e habilidade.

Leia também `docs/sobre.md` para detalhes de contribuição e referências oficiais.

## Contribuição

1. Abra uma issue descrevendo a melhoria.
2. Crie branch a partir de `main`.
3. Utilize a CLI para gerar conteúdo sempre que possível.
4. Execute lint, testes e `mkdocs build --strict` antes do pull request.
5. Mantenha o padrão **Descrição / Por que fazer / Como reverter / Impacto esperado** em novas dicas técnicas.

## Licença

Distribuído sob licença MIT — ver arquivo `LICENSE` (adicione a licença quando definido pela organização).

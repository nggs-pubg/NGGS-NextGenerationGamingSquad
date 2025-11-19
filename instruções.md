# Instrucoes de compilacao e testes NGGS (Windows)

Siga este passo a passo sempre que precisar validar, compilar e testar o projeto em Windows.

## Comandos rapidos (Linux)

Abra um terminal na raiz do repo e execute:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .

# Checagens locais
ruff check --output-format=github .
black --check .
isort --check-only .
pytest -q

# Build/preview do site
python -m mkdocs build --strict
python -m mkdocs serve
```

Encerre o `mkdocs serve` com `Ctrl+C`. Se faltar permissao de execucao no `activate`, rode `chmod +x .venv/bin/activate`.

## 1. Preparar ambiente Python

Abra um PowerShell na raiz do repo e rode:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Caso prefira CMD, ative o ambiente com `.\.venv\Scripts\activate.bat` antes de instalar as dependencias.

## 2. Validar qualidade do codigo (backend + frontend)

Rode as checagens locais usadas no CI:

```powershell
ruff check --output-format=github .
black --check .
isort --check-only .
pytest -q
```

- **Frontend**: depois de alterar Markdown, assets ou JS, execute `python -m mkdocs build --strict`. Opcionalmente revise via `python -m mkdocs serve` validando breakpoints desktop (>=1280px) e mobile (<=480px). A calculadora eDPI precisa manter 800x600 em monitores e responsividade total em telas menores.

Corrija qualquer apontamento antes de seguir.

## 3. Compilar o site estatico

Gere os arquivos do MkDocs em `site/`:

```powershell
python -m mkdocs build --strict
```

O parametro `--strict` interrompe o build se houver erros de lint nos arquivos Markdown.

> Depois de builds que envolvam a calculadora, valide manualmente no preview se inputs, botoes e graficos respondem corretamente. Em caso de alteracoes na CLI, execute `nggs gen weapon` e `nggs calc edpi` para garantir que ainda geram arquivos dentro do padrao.

## 4. Visualizar em desenvolvimento

Para revisar layout e interacoes em tempo real:

```powershell
python -m mkdocs serve
```

Acesse `http://127.0.0.1:8000` no navegador e finalize com `Ctrl+C`.

## 5. Fluxo sugerido antes do commit

1. Atualize ou gere conteudo via CLI se necessario (`nggs gen weapon`, `nggs calc edpi`).
2. Rode os comandos dos passos 2 e 3.
3. Confirme se nao existem arquivos `.bak` no repo (estao no `.gitignore`, mas nao devem ser comitados).
4. Teste a pagina `PC > Otimizador CMD` para garantir que a tabela e o bloco `.bat` renderizam corretamente.
5. So faca commit quando todos os comandos estiverem verdes e o site estiver ok.

O mesmo pipeline roda no GitHub Actions ao abrir PR ou fazer push na `main`.

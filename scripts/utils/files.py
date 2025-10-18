"""File handling helpers for NGGS automation."""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound

_BASE_DIR = Path(__file__).resolve().parent.parent
_TEMPLATES_DIR = _BASE_DIR / "templates"
_ENV = Environment(
    loader=FileSystemLoader(str(_TEMPLATES_DIR)),
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
)


def ensure_markdown_path(path: str | Path) -> Path:
    """Garantir que o caminho termine com extensão `.md`."""
    candidate = Path(path)
    if candidate.suffix.lower() != ".md":
        candidate = candidate.with_suffix(".md")
    return candidate


def write_markdown(path: str | Path, content: str, backup: bool = True) -> Path:
    """Write markdown content to disk, creating backups quando existir arquivo."""
    md_path = ensure_markdown_path(path)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    if backup and md_path.exists():
        backup_path = md_path.with_suffix(md_path.suffix + ".bak")
        backup_path.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8")

    md_path.write_text(content, encoding="utf-8")
    return md_path


def load_template(name: str) -> Template:
    """Obter template Jinja2 do diretório de templates."""
    try:
        return _ENV.get_template(name)
    except TemplateNotFound as exc:  # pragma: no cover - jinja2 já detalha o erro
        raise FileNotFoundError(f"Template '{name}' não encontrado") from exc

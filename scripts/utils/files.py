"""File handling helpers for NGGS automation."""

from __future__ import annotations

import os
import tempfile
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
    """Gravar Markdown de forma atômica, sem seguir links simbólicos."""
    md_path = ensure_markdown_path(path)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    if md_path.is_symlink():
        raise ValueError(f"Recusa de segurança: '{md_path}' é um link simbólico.")

    if backup and md_path.exists():
        backup_path = md_path.with_suffix(md_path.suffix + ".bak")
        if backup_path.is_symlink():
            raise ValueError(f"Recusa de segurança: '{backup_path}' é um link simbólico.")
        backup_path.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8")

    fd, temporary_name = tempfile.mkstemp(prefix=f".{md_path.name}.", dir=md_path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as temporary_file:
            temporary_file.write(content)
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        temporary_path.replace(md_path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return md_path


def load_template(name: str) -> Template:
    """Obter template Jinja2 do diretório de templates."""
    try:
        return _ENV.get_template(name)
    except TemplateNotFound as exc:  # pragma: no cover - jinja2 já detalha o erro
        raise FileNotFoundError(f"Template '{name}' não encontrado") from exc

"""Geração de páginas de armas do PUBG."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from scripts.utils.files import load_template, write_markdown

_INVALID_CHARS_RE = re.compile(r"[^a-z0-9\-.]+")


def slugify(nome: str) -> str:
    """Converta um nome de arma em slug seguro para arquivo."""
    if not nome.strip():
        raise ValueError("O nome da arma não pode ser vazio.")
    slug = nome.strip().lower().replace(" ", "-")
    slug = _INVALID_CHARS_RE.sub("-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    if not slug:
        raise ValueError("O slug gerado está vazio. Verifique o nome informado.")
    return slug


def create_weapon_page(
    nome: str,
    tipo: str,
    saida: str | Path,
    *,
    funcao: str | None = None,
    cano: str | None = None,
    empunhadura: str | None = None,
    municao: str | None = None,
    otica: str | None = None,
    descricao: str | None = None,
    motivo: str | None = None,
    reverter: str | None = None,
    impacto: str | None = None,
) -> Path:
    """Gerar página de arma a partir do template oficial."""
    data: dict[str, Any] = {
        "nome": nome,
        "tipo": tipo,
        "funcao": funcao,
        "cano": cano,
        "empunhadura": empunhadura,
        "municao": municao,
        "otica": otica,
        "descricao": descricao,
        "motivo": motivo,
        "reverter": reverter,
        "impacto": impacto,
    }
    template = load_template("arma_template.md.j2")
    content = template.render(**data)

    output_dir = Path(saida)
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{slugify(nome)}.md"
    target = output_dir / filename
    write_markdown(target, content)
    return target

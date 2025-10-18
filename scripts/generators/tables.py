"""Geradores de tabelas e calculadoras."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from scripts.utils.files import ensure_markdown_path, write_markdown
from scripts.utils.math import DEFAULT_PUBG_YAW, calc_360_distance_cm, calc_edpi

_RESULT_SECTION_PATTERN = re.compile(
    r"(## Resultado Atual\s*\n)(.*?)(\n## |\Z)", re.DOTALL | re.IGNORECASE
)


def build_calculator_section(
    dpi: float,
    sensitivity: float,
    yaw: float = DEFAULT_PUBG_YAW,
) -> str:
    """Gerar bloco Markdown com resultados de eDPI e distância de 360°."""
    edpi = calc_edpi(dpi, sensitivity)
    distance_cm = calc_360_distance_cm(dpi, sensitivity, yaw)
    timestamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")

    block = "\n".join(
        [
            "| Métrica | Valor |",
            "| --- | --- |",
            f"| DPI | {dpi:.2f} |",
            f"| Sensibilidade | {sensitivity:.4f} |",
            f"| eDPI | {edpi:.2f} |",
            f"| Distância 360° (cm) | {distance_cm:.2f} |",
            "",
            f"> Atualizado em {timestamp} (horário local).",
        ]
    )
    return block


def update_calculator_page(
    path: str | Path,
    dpi: float,
    sensitivity: float,
    yaw: float = DEFAULT_PUBG_YAW,
) -> Path:
    """Atualizar seção _Resultado Atual_ com dados calculados."""
    md_path = ensure_markdown_path(path)
    if not md_path.exists():
        raise FileNotFoundError(
            f"Arquivo '{md_path}' não encontrado. Gere o esqueleto antes de atualizar."
        )

    content = md_path.read_text(encoding="utf-8")
    block = build_calculator_section(dpi, sensitivity, yaw)

    match = _RESULT_SECTION_PATTERN.search(content)
    if not match:
        raise ValueError(
            "Seção '## Resultado Atual' não encontrada. Verifique a estrutura do arquivo."
        )

    updated = "".join([match.group(1), block, "\n", match.group(3)])
    new_content = content[: match.start()] + updated + content[match.end() :]

    write_markdown(md_path, new_content)
    return md_path

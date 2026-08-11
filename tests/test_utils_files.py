from __future__ import annotations

import pytest

from scripts.utils.files import load_template, write_markdown


def test_load_template_not_found() -> None:
    """Garantir que FileNotFoundError é levantado para template inexistente."""
    with pytest.raises(FileNotFoundError, match="Template 'nao-existe.md' não encontrado"):
        load_template("nao-existe.md")


def test_write_markdown_is_atomic_and_creates_backup(tmp_path) -> None:
    path = tmp_path / "guia.md"
    path.write_text("anterior", encoding="utf-8")
    write_markdown(path, "novo")
    assert path.read_text(encoding="utf-8") == "novo"
    assert (tmp_path / "guia.md.bak").read_text(encoding="utf-8") == "anterior"

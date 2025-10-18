from __future__ import annotations

import pytest

from scripts.utils.files import load_template


def test_load_template_not_found() -> None:
    """Garantir que FileNotFoundError é levantado para template inexistente."""
    with pytest.raises(FileNotFoundError, match="Template 'nao-existe.md' não encontrado"):
        load_template("nao-existe.md")

from pathlib import Path

import pytest

from scripts.generators.weapons import create_weapon_page, slugify


def test_slugify_converts_name() -> None:
    assert slugify("Beryl M762") == "beryl-m762"
    assert slugify("MK12 5.56") == "mk12-5.56"


def test_create_weapon_page_generates_file(tmp_path: Path) -> None:
    destino = create_weapon_page(
        nome="Beryl M762",
        tipo="AR",
        saida=tmp_path,
        funcao="Entrada agressiva",
    )
    expected_file = tmp_path / "beryl-m762.md"
    assert destino == expected_file
    assert expected_file.exists()
    content = expected_file.read_text(encoding="utf-8")
    assert "# Beryl M762" in content
    assert "Entrada agressiva" in content


def test_create_weapon_page_invalid_name(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        create_weapon_page(nome="   ", tipo="AR", saida=tmp_path)

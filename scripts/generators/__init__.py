"""Generators transform inputs into Markdown content for the NGGS docs."""

from .tables import build_calculator_section, update_calculator_page
from .weapons import create_weapon_page

__all__ = ["create_weapon_page", "build_calculator_section", "update_calculator_page"]

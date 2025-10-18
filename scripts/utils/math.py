"""Math helpers for NGGS calculators."""

from __future__ import annotations

from typing import Final

DEFAULT_PUBG_YAW: Final[float] = 0.0025
CM_PER_INCH: Final[float] = 2.54


def calc_edpi(dpi: float, sensitivity: float) -> float:
    """Return the effective DPI (DPI físico multiplicado pela sensibilidade do jogo)."""
    if dpi <= 0:
        raise ValueError("DPI deve ser maior que zero.")
    if sensitivity <= 0:
        raise ValueError("A sensibilidade deve ser maior que zero.")
    return dpi * sensitivity


def calc_360_distance_cm(
    dpi: float,
    sensitivity: float,
    yaw: float = DEFAULT_PUBG_YAW,
) -> float:
    """Calculate the distance (in centimeters) needed to rotate 360°.

    Args:
        dpi: DPI do sensor.
        sensitivity: sensibilidade aplicada no jogo.
        yaw: valor de yaw do jogo (graus por contagem). Para o PUBG, usa-se 0.0025.

    Returns:
        Distância em centímetros para completar uma volta de 360°.
    """
    if yaw <= 0:
        raise ValueError("Yaw deve ser maior que zero.")

    edpi = calc_edpi(dpi, sensitivity)
    counts_per_degree = 1.0 / yaw
    inches = (counts_per_degree * 360.0) / edpi
    return inches * CM_PER_INCH

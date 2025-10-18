import pytest

from scripts.utils.math import calc_360_distance_cm, calc_edpi


def test_calc_edpi_basic() -> None:
    assert calc_edpi(800, 1.5) == pytest.approx(1200.0)


@pytest.mark.parametrize("dpi,sens", [(0, 1.0), (800, 0.0)])
def test_calc_edpi_invalid(dpi: float, sens: float) -> None:
    with pytest.raises(ValueError):
        calc_edpi(dpi, sens)


def test_calc_360_distance_cm() -> None:
    result = calc_360_distance_cm(800, 1.5)
    assert result == pytest.approx(304.8, rel=1e-3)


def test_calc_360_invalid_yaw() -> None:
    with pytest.raises(ValueError):
        calc_360_distance_cm(800, 1.0, yaw=0.0)

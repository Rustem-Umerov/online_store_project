from typing import Any

import pytest

from models.entities.lawn_grass import LawnGrass
from models.entities.product import Product
from models.entities.smartphone import Smartphone


def test_lawn_grass(lawn_grass: LawnGrass) -> None:
    """Тест проверяет, что атрибуты класса LawnGrass соответствуют указанным в фикстуре."""

    assert lawn_grass.name == "a"
    assert isinstance(lawn_grass.name, str)

    assert lawn_grass.description == "aaa"
    assert isinstance(lawn_grass.description, str)

    assert lawn_grass.price == 10.10
    assert isinstance(lawn_grass.price, float)

    assert lawn_grass.quantity == 5
    assert isinstance(lawn_grass.quantity, int)

    assert lawn_grass.country == "b"
    assert isinstance(lawn_grass.country, str)

    assert lawn_grass.germination_period == "c"
    assert isinstance(lawn_grass.germination_period, str)

    assert lawn_grass.color == "d"
    assert isinstance(lawn_grass.color, str)


def test_added_lawn_grass(lawn_grass: LawnGrass) -> None:
    """Тест проверяет метод __add__"""

    expected = (lawn_grass.price * lawn_grass.quantity) * 2

    assert lawn_grass.__add__(lawn_grass) == expected
    assert lawn_grass + lawn_grass == expected


@pytest.mark.parametrize(
    "other",
    [
        10,
        "text",
        None,
        Product("X", "Y", 1.0, 1),
        Smartphone(
            "a", "aaa", 10.10, 5, 10.10, "b", 5.5, "s"
        )
    ]
)
def test_added_lawn_grass_error(lawn_grass: LawnGrass, other: Any) -> None:
    """Тест проверяет, что будет ошибка если к объекту класса LawnGrass приплюсовать объект другого класса."""

    with pytest.raises(TypeError) as exc:
        lawn_grass.__add__(other)  # или lawn_grass + other

    assert "Можно сложить только газонную траву с другой газонной травой." in str(exc.value)


def test_lawn_grass_category_name(lawn_grass: LawnGrass) -> None:
    """Тест проверяет правильный вывод названия категории."""

    assert lawn_grass.get_category_name() == "Сад"

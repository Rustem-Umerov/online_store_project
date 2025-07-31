import pytest
from models.entities.smartphone import Smartphone
from models.entities.lawn_grass import LawnGrass
from models.entities.product import Product
from typing import Any


def test_smartphone(smartphone: Smartphone) -> None:
    """Тест проверяет, что атрибуты класса Smartphone соответствуют указанным в фикстуре."""

    assert smartphone.name == "a"
    assert isinstance(smartphone.name, str)

    assert smartphone.description == "aaa"
    assert isinstance(smartphone.description, str)

    assert smartphone.price == 10.10
    assert isinstance(smartphone.price, float)

    assert smartphone.quantity == 5
    assert isinstance(smartphone.quantity, int)

    assert smartphone.efficiency == 100.0
    assert isinstance(smartphone.efficiency, float)

    assert smartphone.model == "new"
    assert isinstance(smartphone.model, str)

    assert smartphone.memory == 10.0
    assert isinstance(smartphone.memory, float)

    assert smartphone.color == "black"
    assert isinstance(smartphone.color, str)


def test_added_smartphone(smartphone: Smartphone) -> None:
    """Тест проверяет метод __add__"""

    expected = (smartphone.price * smartphone.quantity) * 2

    assert smartphone.__add__(smartphone) == expected
    assert smartphone + smartphone == expected


@pytest.mark.parametrize(
    "other",
    [
        10,
        "text",
        None,
        Product("X", "Y", 1.0, 1),
        LawnGrass("a", "aaa", 10.10, 5, "b", "c", "d")
    ]
)
def test_added_smartphone_error(smartphone: Smartphone, other: Any) -> None:
    """Тест проверяет, что будет ошибка если к объекту класса Smartphone приплюсовать объект другого класса."""

    with pytest.raises(TypeError) as exc:
        smartphone.__add__(other)  # или smartphone + other

    assert "Можно сложить только смартфоны с другими смартфонами." in str(exc.value)


def test_smartphone_category_name(smartphone: Smartphone) -> None:
    """Тест проверяет правильный вывод названия категории."""

    assert smartphone.get_category_name() == "Электроника"

from typing import Any

import pytest

from models.entities.category import Category
from models.entities.lawn_grass import LawnGrass
from models.entities.smartphone import Smartphone
from src.distributor import assign_to_category


def test_assign_to_valid_category(smartphone: Smartphone, lawn_grass: LawnGrass) -> None:
    """Тест проверяет, что функция-распределитель работает правильно."""

    category_electronics = Category("Электроника", "Гаджеты и смартфоны")
    category_garden = Category("Сад", "Товары для сада и дачи")


    categories = {"Электроника": category_electronics, "Сад": category_garden}

    assign_to_category(smartphone, categories)
    assign_to_category(lawn_grass, categories)

    assert smartphone in category_electronics.products
    assert lawn_grass in category_garden.products


def test_assign_to_missing_category(smartphone: Smartphone) -> None:
    """Тест проверяет появления ошибки ValueError, если необходимая категория не найдена."""

    categories: dict[str, Any] = {}

    with pytest.raises(ValueError, match="Категория 'Электроника' не найдена"):
        assign_to_category(smartphone, categories)

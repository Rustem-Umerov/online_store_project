import pytest

from models.core.base_product import BaseProduct


class TestProduct(BaseProduct):
    """Тестовый класс. Тестируя данный класс, можно протестировать абстрактный класс BaseProduct."""

    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        return "Тестовая категория"

    @property
    def price(self) -> float:
        """Цена (только для чтения)."""

        return self._price


def test_base_product() -> None:
    """В данном тесте, для тестирования абстрактного класса BaseProduct,
    был создан экземпляр класса TestProduct, который является наследником класса BaseProduct"""

    prod = TestProduct("a", "aaa", 10.1, 5)

    assert prod.name == "a"
    assert isinstance(prod.name, str)

    assert prod.description == "aaa"
    assert isinstance(prod.description, str)

    assert prod.price == 10.1
    assert isinstance(prod.price, float)

    assert prod.quantity == 5
    assert isinstance(prod.quantity, int)

    assert prod.total_cost == 50.5
    assert isinstance(prod.total_cost, float)


def test_base_product_cannot_be_instantiated() -> None:
    """Тест проверяет, что будет ошибка, если попытаться создать экземпляр абстрактного класса."""

    with pytest.raises(TypeError):
        BaseProduct("x", "y", 1.0, 1)  # type: ignore[abstract]


def test_base_product_negative_price_error() -> None:
    """Тест проверяет, что будет ошибка ValueError, если попытаться создать экземпляр класса с отрицательной ценой."""

    with pytest.raises(ValueError, match="Price cannot be a negative value."):
        TestProduct("a", "aaa", -10, 5)


def test_base_product_negative_quantity_error() -> None:
    """Тест проверяет, что будет ошибка ValueError,
    если попытаться создать экземпляр класса с отрицательным количеством."""

    with pytest.raises(ValueError, match="Quantity cannot be a negative value."):
        TestProduct("a", "aaa", 10, -5)


def test_base_product_zero_price_quantity() -> None:
    """Тест проверяет, что экземпляр класса с нулевой ценой и количеством создаётся без ошибок."""

    prod = TestProduct("a", "aaa", 0, 0)

    assert prod.name == "a"
    assert prod.description == "aaa"
    assert prod.price == 0
    assert prod.quantity == 0
    assert prod.total_cost == 0

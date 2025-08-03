import pytest

from models.entities.order import Order
from models.entities.product import Product
from models.entities.smartphone import Smartphone
from src.exceptions import NegativeOrZeroQuantityError


def test_order_class(product: Product) -> None:
    """Тест проверяет класс Order"""

    order_obj = Order(product, 2)

    assert order_obj.product == product
    assert isinstance(order_obj.product, Product)

    assert order_obj.quantity == 2
    assert isinstance(order_obj.quantity, int)

    assert str(order_obj) == "Куплен товар: Name, количество: 2, итоговая стоимость: 199.98."
    assert repr(order_obj) == "Название товара: Name, количество товара: 2, итоговая стоимость: 199.98."


def test_order_class_quantity_error(smartphone: Smartphone) -> None:
    """Тест проверяет возникновение ошибки ValueError,
    если в класс Order передать количество товара больше, чем есть в наличии."""

    with pytest.raises(ValueError) as exc:
        Order(smartphone, 10)

    assert "Ошибка: вы пытаетесь купить: 10 ед. товара, это больше, чем есть, в наличии: 5 ед." in str(exc.value)


def test_order_class_not_obj_product_class() -> None:
    """Тест проверяет, что будет ошибка TypeError, если в класс Order передать объект
    НЕ класса Product или его наследников."""

    with pytest.raises(TypeError, match="Передан объект, не являющийся товаром."):
        Order("aaa", 5)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "quantity", [0, -5]
)
def test_order_class_invalid_quantity(product: Product, quantity: int) -> None:
    """Тест проверяет, что будет персональная ошибка NegativeOrZeroQuantityError, если в класс Order
    передать объект класса Product или его наследников с нулевым или отрицательным количеством."""

    with pytest.raises(NegativeOrZeroQuantityError) as exc:
        Order(product, quantity)

    assert "Нельзя добавить товар 'Name' с нулевым или отрицательным количеством." in str(exc.value)

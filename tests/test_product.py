import pytest
from _pytest.monkeypatch import MonkeyPatch

from models.product import Product, validate_non_negative


def test_product(product: Product) -> None:
    """Тест проверяет, что атрибуты класса соответствуют указанным в фикстуре."""

    assert product.name == "Name"
    assert product.description == "Description"
    assert isinstance(product.price, float)
    assert product.price == 99.99
    assert isinstance(product.quantity, int)
    assert product.quantity == 5


@pytest.mark.parametrize(
    "negative_price",
    [-10.10, -15, -25.25],
)
def test_negative_price(negative_price: float) -> None:
    """Тест проверяет, что, если цена отрицательная, то будет ошибка ValueError."""

    with pytest.raises(ValueError) as exc:
        Product("A", "Abc", negative_price, 10)
    assert "Price cannot be a negative value." in str(exc.value)


@pytest.mark.parametrize(
    "negative_quantity",
    [-10.10, -15, -25.25],
)
def test_negative_quantity(negative_quantity: int) -> None:
    """Тест проверяет, что, если количество отрицательное, то будет ошибка ValueError."""

    with pytest.raises(ValueError) as exc:
        Product("A", "Abc", 10.10, negative_quantity)
    assert "Quantity cannot be a negative value." in str(exc.value)


def test_init_calls_validate_non_negative(monkeypatch: MonkeyPatch) -> None:
    """
    Проверяет, что при инициализации объекта Product вызывается функция validate_non_negative
    с правильными аргументами (сначала для цены, затем для количества).

    :param monkeypatch:
    :return:
    """

    calls = []

    def fake_validator(value: float, field: str) -> None:
        calls.append((value, field))

    monkeypatch.setattr("models.product.validate_non_negative", fake_validator)
    p = Product("Name", "Description", 99.99, 5)

    assert calls == [(99.99, "Price"), (5, "Quantity")]

    assert p.price == 99.99
    assert p.quantity == 5


@pytest.mark.parametrize(
    "value, object_, result_info",
    [
        (-10, "AAA", "AAA cannot be a negative value."),
        (-15, "BBB", "BBB cannot be a negative value."),
        (-25.2563, "EEE", "EEE cannot be a negative value."),
    ],
)
def test_validate_non_negative(value: float, object_: str, result_info: str) -> None:
    """
    Тест проверяет, что в случае отрицательного значения, будет ошибка ValueError.
    """

    with pytest.raises(ValueError) as exc_info:
        validate_non_negative(value, object_)
    assert result_info in str(exc_info.value)

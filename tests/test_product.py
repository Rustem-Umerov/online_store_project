import pytest
from _pytest.monkeypatch import MonkeyPatch

from models.product import Product, validate_non_negative
from src.exceptions import InvalidPriceError, PriceDecreaseError


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


def test_creation_new_product() -> None:
    """Тест проверяет, что класс-метод new_product успешно добавляет новый товар в список."""

    new_prod = Product.new_product(name="a", description="aaa", price=10.00, quantity=1, existing_products=[])

    assert isinstance(new_prod, Product)
    assert new_prod.name == "a"
    assert new_prod.description == "aaa"
    assert new_prod.price == 10.00
    assert new_prod.quantity == 1


def test_update_new_product() -> None:
    """Тест проверяет, что класс-метод new_product успешно обновляет товар в списке."""

    list_product = [
        Product(name="a", description="aaa", price=10.00, quantity=1),
        Product(name="b", description="bbb", price=20.00, quantity=2),
    ]

    prod = Product.new_product(name="b", description="bbb", price=30.00, quantity=10, existing_products=list_product)

    assert isinstance(prod, Product)
    assert len(list_product) == 2
    assert list_product[1].name == "b"
    assert list_product[1].description == "bbb"
    assert list_product[1].price == 30.00
    assert list_product[1].quantity == 12
    assert prod is list_product[1]


@pytest.mark.parametrize(
    "new_price, result",
    [
        (200.00, None),
        (0, [InvalidPriceError, "Недопустимая цена: 0. Цена не должна быть нулевой или отрицательной."]),
        (-5, [InvalidPriceError, "Недопустимая цена: -5. Цена не должна быть нулевой или отрицательной."]),
        (50.0, [PriceDecreaseError, "Вы ввели цену: 50.0, меньше текущей: 99.99."]),
    ],
)
def test_new_price(product: Product, new_price: float, result: list) -> None:
    """
    Проверяет setter price:
    - успешное обновление, если expected is None
    - выброс корректного исключения
    """

    if result is None:
        product.price = new_price
        assert product.price == new_price

    else:
        exc_type, exc_message = result
        with pytest.raises(exc_type) as exc:
            product.price = new_price

        assert exc_message in str(exc.value)

        if exc_type is PriceDecreaseError:
            assert exc.value.old == 99.99
            assert exc.value.new == 50.0


@pytest.mark.parametrize(
    "new_price",
    [
        10.0,
        20.0,
        30.0,
        40.0,
    ],
)
def test_force_price_update(product: Product, new_price: float) -> None:
    """Тест проверяет принудительное обновление цены без срабатывания исключения через метод force_price_update."""

    product.force_price_update(new_price=new_price)

    assert product.price == new_price


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

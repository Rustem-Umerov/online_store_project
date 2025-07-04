import pytest
from models.product import Product
from models.category import Category


@pytest.fixture
def product() -> Product:
    """Фукстура, возвращающая валидный объект Product."""

    return Product("Name", "Description", 99.99, 5)


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    """
    Сбрасывает Category.category_count и Category.product_count
    перед каждым тестом, чтобы они не накапливались между тестами.
    """
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products() -> list[Product]:
    """
    Возвращает список из трёх валидных объектов Product.
    """
    return [
        Product("A", "Desc A", 1.0, 1),
        Product("B", "Desc B", 2.0, 2),
        Product("C", "Desc C", 3.0, 3),
    ]
import pytest

from models.entities.category import Category
from models.entities.lawn_grass import LawnGrass
from models.entities.product import Product
from models.entities.smartphone import Smartphone
from models.helpers.product_iterator import ProductIterator


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


@pytest.fixture
def category(sample_products: list[Product]) -> Category:
    """Фукстура, возвращающая валидный объект Category"""

    return Category("A", "Desc", sample_products)


@pytest.fixture
def product_iterator_obj(category: Category) -> ProductIterator:
    """Фукстура, возвращающая валидный объект ProductIterator"""

    return ProductIterator(category)


@pytest.fixture
def category_with_empty_product_list() -> Category:
    """Фикстура возвращает объект класса Category с пустым списком объектов Product"""

    return Category("A", "Desc", [])


@pytest.fixture
def category_with_one_product_in_products_list(product: Product) -> Category:
    """Фикстура возвращает объект класса Category с одним объектом Product в списке объектов Product"""

    return Category("A", "Desc", [product])


@pytest.fixture
def smartphone() -> Smartphone:
    """Фукстура, возвращающая валидный объект Smartphone."""

    return Smartphone("a", "aaa", 10.10, 5, 100.0, "new", 10.0, "black")


@pytest.fixture
def lawn_grass() -> LawnGrass:
    """Фукстура, возвращающая валидный объект LawnGrass."""

    return LawnGrass("a", "aaa", 10.10, 5, "b", "c", "d")

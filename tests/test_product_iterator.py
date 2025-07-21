import pytest

from models.category import Category
from models.product import Product
from models.product_iterator import ProductIterator


def test_product_iterator(product_iterator_obj: ProductIterator, sample_products: list[Product]) -> None:
    """Тест проверяет итерацию по списку объектов Product"""

    assert product_iterator_obj._index == 0
    assert next(product_iterator_obj) == sample_products[0]
    assert next(product_iterator_obj) == sample_products[1]
    assert next(product_iterator_obj) == sample_products[2]

    with pytest.raises(StopIteration):
        next(product_iterator_obj)


def test_product_iterator_with_for(product_iterator_obj: ProductIterator, sample_products: list[Product]) -> None:
    """Проверяет работу итератора внутри for-цикла"""

    for i, prod in enumerate(product_iterator_obj):
        assert prod == sample_products[i]


def test_product_iterator_iter_returns_self(product_iterator_obj: ProductIterator) -> None:
    """Проверяет, что __iter__ возвращает сам итератор"""

    assert iter(product_iterator_obj) is product_iterator_obj


def test_product_iterator_not_product(category_with_empty_product_list: Category) -> None:
    """Тест проверяет, что, если список с объектами Product пустой, то сразу будет вызвана ошибка StopIteration"""

    with pytest.raises(StopIteration):
        next(ProductIterator(category_with_empty_product_list))


def test(category_with_one_product_in_products_list: Category, product: Product) -> None:
    """Тест проверяет, что если в списке продуктов один объект класса Product, то на втором шаге next
    будет вызвана ошибка StopIteration"""

    iterator = ProductIterator(category_with_one_product_in_products_list)

    assert next(iterator) == product

    with pytest.raises(StopIteration):
        next(iterator)


def test_product_iterator_to_list(product_iterator_obj: ProductIterator, sample_products: list[Product]) -> None:
    """Проверка совместимости с list() — ожидаем получить список продуктов."""

    assert list(product_iterator_obj) == sample_products


def test_product_iterator_repeat(product_iterator_obj: ProductIterator, sample_products: list[Product]) -> None:
    """Проверка сброса индекса при повторной итерации"""

    for _ in product_iterator_obj:
        pass

    repeated = list(product_iterator_obj)
    assert repeated == sample_products


def test_product_iterator_independent_instances(category: Category, sample_products: list[Product]) -> None:
    """Тест проверяет, что два итератора не влияют друг на друга"""

    it1 = ProductIterator(category)
    it2 = ProductIterator(category)

    assert next(it1) == sample_products[0]
    assert next(it2) == sample_products[0]
    assert next(it1) == sample_products[1]
    assert next(it2) == sample_products[1]

import pytest
from models.category import Category
from models.product import Product


def test_initialization_with_an_empty_list_of_products(reset_counters: None) -> None:
    """Инициализация с пустым списком товаров."""

    cat = Category("Еда", "Продукты")

    assert cat.name == "Еда"
    assert cat.description == "Продукты"

    # Вызываю конструктор без параметра products,
    # поэтому внутри __init__ сработает products or [], и cat.products станет новым пустым списком.
    assert isinstance(cat.products, list)
    assert cat.products == []

    # С помощью фикстуры reset_counters счётчики обнуляются перед тестом, затем проверяем,
    # что после создания одного объекта category_count стал 1, а product_count по-прежнему 0.
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_init_with_products_populates_list_and_counters(reset_counters: None, sample_products: list[Product]) -> None:
    """Инициализация с непустым списком товаров"""

    cat = Category("Фрукты", "Еда", sample_products)

    # products сохраняется «как есть»
    assert cat.products is sample_products
    assert cat.products == sample_products

    # category_count += 1, product_count += len(sample_products)
    assert Category.category_count == 1
    assert Category.product_count == len(sample_products)


def test_init_with_invalid_items_raises_type_error_and_no_counter_increment(reset_counters: None) -> None:
    """Проверка, что будет ошибка TypeError, если список продуктов будет состоять не только из объектов Product."""

    invalid_list = [Product("a", "aaa", 10.10, 5),
                    Product("b", "bbb", 15.15, 10),
                    "product", ["abc", "abc"], 99.99]

    with pytest.raises(TypeError) as eac_info:
        Category("name", "desc", invalid_list)  # type: ignore[arg-type]

    assert "The product list must contain only Product objects." in str(eac_info)
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_counters_accumulate_over_multiple_categories(reset_counters: None, sample_products: list[Product]) -> None:
    """Проверка правильности подсчета счетчиков."""

    Category("a", "aaa", [])
    Category("a", "aaa", sample_products)
    Category("a", "aaa", [sample_products[0]])
    Category("b", "bbb", [sample_products[0], sample_products[1]])

    assert Category.category_count == 4
    assert Category.product_count == 6


def test_products_list_is_independent_between_instances(reset_counters: None, sample_products: list[Product]) -> None:
    """Проверка, что у каждого объекта Category свой список товаров с объектами Product."""

    cat1 = Category("One", "", [])
    cat2 = Category("Two", "", [])

    # изменяю список первого экземпляра
    cat1.products.append(sample_products[0])

    # проверяю, что второй экземпляр не пострадал
    assert cat1.products == [sample_products[0]]
    assert cat2.products == []


def test_inheritance_updates_counters_on_subclass(reset_counters: None, sample_products: list[Product]) -> None:
    """Проверка наследования. Проверка того, что счетчики подкласса обновились,
    а счетчики основного класса не изменились."""

    class SpecialCategory(Category):
        pass

    # обнуляем счётчики только у подкласса
    SpecialCategory.category_count = 0
    SpecialCategory.product_count = 0

    SpecialCategory("a", "aaa", sample_products)

    # счётчики подкласса обновились
    assert SpecialCategory.category_count == 1
    assert SpecialCategory.product_count == len(sample_products)

    # базовый класс не затронут
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_instance_scope_of_class_counters(reset_counters: None) -> None:
    """Проверка изоляция атрибутов счётчиков на уровне экземпляра."""

    cat = Category("X", "Y")

    # глобальный счётчик уже 1
    assert Category.category_count == 1

    # запись в экземпляр создаёт локальный атрибут, не меняя класс
    cat.category_count = 5

    assert cat.category_count == 5
    assert Category.category_count == 1

import pytest

from models.entities.category import Category
from models.entities.lawn_grass import LawnGrass
from models.entities.product import Product
from models.entities.smartphone import Smartphone


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

    assert cat.products == sample_products

    # category_count += 1, product_count += len(sample_products)
    assert Category.category_count == 1
    assert Category.product_count == len(sample_products)


def test_init_with_invalid_items_raises_type_error_and_no_counter_increment(reset_counters: None) -> None:
    """Проверка, что будет ошибка TypeError, если список продуктов будет состоять не только из объектов Product."""

    invalid_list = [Product("a", "aaa", 10.10, 5), Product("b", "bbb", 15.15, 10), "product", ["abc", "abc"], 99.99]

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
    cat1.add_product(sample_products[0])

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


def test_not_class_object() -> None:
    """Тест проверяет, что будет ошибка TypeError, если в метод add_product передать не объект класса Product."""

    cat = Category("One", "", [])

    with pytest.raises(TypeError) as exc:
        cat.add_product("aaa")  # type: ignore[arg-type]

    assert "Must add Product instance." in str(exc.value)


@pytest.mark.parametrize("quantity", [0, -5])
def test_add_product_not_quantity(category_with_empty_product_list: Category, quantity: int) -> None:
    """Тест проверяет, что будет ошибка, если в метод add_product передать объект класса Product или его наследников
    с нулевым или отрицательным количеством."""

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        category_with_empty_product_list.add_product(Product("a", "aa", 10, quantity))


def test_add_product_object(reset_counters: None, sample_products: list[Product]) -> None:
    """Проверка работы метода add_product с правильными данными(объектами класса Product)"""

    cat = Category("One", "", [])

    for prod in sample_products:
        cat.add_product(prod)

    assert cat.products == sample_products
    assert type(cat).product_count == 3


def test_valid_result_list_product(reset_counters: None, sample_products: list[Product]) -> None:
    """Тест проверяет правильный вывод списка товаров в виде строк с помощью метода list_product."""

    cat = Category("One", "", sample_products)

    expected = "\n".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in sample_products)

    assert cat.list_product == expected


def test_new_product_in_create_or_update_product(reset_counters: None) -> None:
    """Тест проверяет, что новый объект Product успешно добавлен."""

    cat = Category("name", "description", [])

    new_prod = cat.create_or_update_product("a", "d", 10.00, 5)
    product_from_list = cat.products[0]

    assert new_prod in cat.products

    assert new_prod.name == "a"
    assert new_prod.description == "d"
    assert new_prod.price == 10.00
    assert new_prod.quantity == 5

    assert product_from_list.name == new_prod.name
    assert product_from_list.description == new_prod.description
    assert product_from_list.price == new_prod.price
    assert product_from_list.quantity == new_prod.quantity

    assert cat.product_count == 1
    assert len(cat.products) == 1


def test_not_new_product_in_create_or_update_product(reset_counters: None) -> None:
    """Тест проверяет, что имеющийся в списке объект Product успешно обновлен."""

    prod = Product("a", "d", 10.00, 5)
    cat = Category("name", "description", [prod])
    updated_prod = cat.create_or_update_product("a", "ddd", 20.00, 10)

    assert prod in cat.products
    assert updated_prod is prod

    assert prod.name == "a"
    assert prod.description == "d"
    assert prod.price == 20.00
    assert prod.quantity == 15

    assert cat.product_count == 1
    assert len(cat.products) == 1


def test_str_display_category(category: Category) -> None:
    """Тест строкового отображения."""

    assert str(category) == "A, количество продуктов: 6 шт."


def test_average_price(product: Product, lawn_grass: LawnGrass, smartphone: Smartphone) -> None:
    """Тест метода average_price, который подсчитывает средний ценник всех товаров."""

    cat = Category("a", "aaa", [product, lawn_grass, smartphone])

    assert cat.average_price() == 40.06


def test_average_price_empty_list_product() -> None:
    """Тест метода average_price, который подсчитывает средний ценник всех товаров.
    В данном тесте, метод должен вернуть 0.0, так список продуктов пустой."""

    cat = Category("a", "aaa", [])

    assert cat.average_price() == 0.0

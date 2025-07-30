from models.entities.product import Product
from models.entities.category import Category


CATEGORIES = {
    "Электроника": Category("Электроника", "Гаджеты и смартфоны"),
    "Сад": Category("Сад", "Товары для сада и дачи"),
    "Прочее": Category("Прочее", "Обычные товары без специальной категории")
}


def assign_to_category(product: Product, categories: dict[str, Category]) -> None:
    """
    Функция-распределитель. Распределяет товары по категориям.

    Функция вызывает метод get_category_name(), который возвращает название категории.
    Этот метод прописан в классе Product и во всех классах-наследниках от Product.

    Далее, происходит поиск объекта класса Category с нужной категорией,
    в заранее созданном словаре, где ключ - категория, а значение - объект класса Category.
    После, в нужную категорию добавляется товар.
    Если категория не найдена, то ошибка ValueError.

    :param product: Объект класса Product, либо объект классов-наследников от Product.
    :param categories: Словарь с категориями.
    """

    category_name = product.get_category_name()
    category = categories.get(category_name)

    if category:
        category.add_product(product)
        print(f"{product.__class__.__name__} добавлен в категорию {category_name}.")

    else:
        raise ValueError(f"Категория '{category_name}' не найдена")

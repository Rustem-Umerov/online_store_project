from typing import Optional

from models.product import Product


class Category:
    """
    Класс Category описывает категорию товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        products (list[Product]): Список товаров в категории.

    Атрибуты класса:
        category_count (int): Количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    """

    name: str
    description: str
    products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров (объекты Product), входящих в категорию.
        """

        self.name = name
        self.description = description

        self.products = products or []
        for item in self.products:
            if not isinstance(item, Product):
                raise TypeError("The product list must contain only Product objects.")

        cls = type(self)
        cls.category_count += 1
        cls.product_count += len(self.products)

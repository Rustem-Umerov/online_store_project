from typing import TYPE_CHECKING, Optional

from models.entities.product import Product

if TYPE_CHECKING:
    from models.helpers.product_iterator import ProductIterator


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

        self.__products = products or []
        for item in self.__products:
            if not isinstance(item, Product):
                raise TypeError("The product list must contain only Product objects.")

        cls = type(self)
        cls.category_count += 1
        cls.product_count += len(self.products)

    def __str__(self) -> str:
        """Строковое отображение в следующем виде: Название категории, количество продуктов: 200 шт."""

        return f"{self.name}, количество продуктов: {sum(prod.quantity for prod in self.__products)} шт."

    def __iter__(self) -> "ProductIterator":
        """Класс Category становится итерируемым, но делегирует процесс итерации объекту ProductIterator"""

        return ProductIterator(self)

    def average_price(self) -> float:
        """Метод, который подсчитывает средний ценник всех товаров."""

        if not self.__products:
            return 0

        return sum(prod.price for prod in self.__products) / len(self.__products)

    @property
    def products(self) -> list[Product]:
        """Список товаров (только для чтения)."""

        return list(self.__products)

    def add_product(self, product: Product) -> None:
        """Специальный метод, для добавления товаров в категорию."""

        if not isinstance(product, Product):
            raise TypeError("Must add Product instance.")
        self.__products.append(product)
        type(self).product_count += 1

    @property
    def list_product(self) -> str:
        """Геттер, который выводит список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт."""

        return "\n".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products)

    def create_or_update_product(self, name: str, description: str, price: float, quantity: int) -> Product:
        """Создаёт или обновляет товар через класс-метод Product.new_product,
        передавая в него текущий список self.__products."""

        prod = Product.new_product(
            name=name, description=description, price=price, quantity=quantity, existing_products=self.__products
        )
        if prod not in self.__products:
            self.__products.append(prod)
            type(self).product_count += 1
        return prod

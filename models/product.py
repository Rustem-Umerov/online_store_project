from types import NotImplementedType
from typing import Optional

from src.exceptions import InvalidPriceError, PriceDecreaseError
from models.base_product import BaseProduct


class Product(BaseProduct):
    """
    Класс Product описывает товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара (рубли с копейками).
        quantity (int): Количество товара в наличии.
    """

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Product.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """

        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое отображение в следующем виде: Название продукта, 80 руб. Остаток: 15 шт."""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float | NotImplementedType:
        """Вывод полной стоимости всех товаров на складе"""

        if not isinstance(other, Product):
            return NotImplemented

        return self.total_cost + other.total_cost

    @classmethod
    def new_product(
        cls,
        name: str,
        description: str,
        price: float,
        quantity: int,
        existing_products: Optional[list["Product"]] = None,
    ) -> "Product":
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""

        if existing_products:
            for prod in existing_products:
                if prod.name == name:
                    prod.price = max(prod.price, price)
                    prod.quantity += quantity
                    return prod

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Цена (только для чтения)."""

        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер проверяет новую цену.
        Если цена меньше нуля, возникает исключение InvalidPriceError.
        Если цена меньше предыдущей, возникает исключение PriceDecreaseError.
        Если цена соответствует критериям, то цена переназначается на новую.

        :param new_price: Новая цена
        :return: Либо цена переназначается, либо выводит исключение.
        """

        if new_price <= 0:
            raise InvalidPriceError(new_price)

        if new_price < self._price:
            raise PriceDecreaseError(old=self._price, new=new_price)

        self._price = new_price

    def force_price_update(self, new_price: float) -> None:
        """Принудительное обновление цены без срабатывания исключения."""

        self._price = new_price

    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        return "Прочее"

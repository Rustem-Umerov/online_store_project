from src.exceptions import InvalidPriceError, PriceDecreaseError
from typing import Optional


class Product:
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

        validate_non_negative(price, "Price")
        validate_non_negative(quantity, "Quantity")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

        return self.__price

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

        if new_price < self.__price:
            raise PriceDecreaseError(old=self.__price, new=new_price)

        self.__price = new_price

    def force_price_update(self, new_price: float) -> None:
        """Принудительное обновление цены без срабатывания исключения."""

        self.__price = new_price


def validate_non_negative(value: float | int, object_: str) -> None:
    """
    Универсальный валидатор. Проверяет значение объекта.
    Если переданное значение отрицательное, то вызывается ошибка ValueError.

    :param value: Значение объекта (float | int).
    :param object_: Название объекта.
    """

    if value < 0:
        raise ValueError(f"{object_} cannot be a negative value.")

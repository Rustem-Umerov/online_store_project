from typing import cast

from models.product import Product


class LawnGrass(Product):
    """Класс LawnGrass для товара «Трава газонная» - наследник от класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация объекта LawnGrass.

        :param name: Название товара. Принимает от базового класса Product.
        :param description: Описание товара. Принимает от базового класса Product.
        :param price: Цена товара. Принимает от базового класса Product.
        :param quantity: Количество товара в наличии. Принимает от базового класса Product.

        :param country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет.
        """

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: object) -> float:
        """Вывод полной стоимости всех товаров на складе"""

        if type(other) is not type(self):
            raise TypeError("Можно сложить только газонную траву с другой газонной травой.")

        other = cast(LawnGrass, other)
        return self.total_cost + other.total_cost

    @property
    def total_cost(self) -> float:
        """Определена полная стоимость товаров (цена товара умножается на количество товара)"""

        return self.price * self.quantity

    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        return "Сад"

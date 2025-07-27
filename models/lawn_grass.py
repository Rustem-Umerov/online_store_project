from models.product import Product


class LawnGrass(Product):
    """Класс LawnGrass для товара «Трава газонная» - наследник от класса Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str) -> None:
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
        self.country = color

    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        return "Сад"
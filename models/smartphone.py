from models.product import Product


class Smartphone(Product):
    """Класс Smartphone для товара «Смартфон» - наследник от класса Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: float, color: str) -> None:
        """
        Инициализация объекта Smartphone.

        :param name: Название товара. Принимает от базового класса Product.
        :param description: Описание товара. Принимает от базового класса Product.
        :param price: Цена товара. Принимает от базового класса Product.
        :param quantity: Количество товара в наличии. Принимает от базового класса Product.

        :param efficiency: Производительность.
        :param model: Модель.
        :param memory: Объем встроенной памяти.
        :param color: Цвет.
        """

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:
        """Вывод полной стоимости всех товаров на складе"""

        if type(other) is not type(self):
            raise TypeError("Можно сложить только смартфоны с другими смартфонами.")

        return self.total_cost + other.total_cost

    @property
    def total_cost(self) -> float:
        """Определена полная стоимость товаров (цена товара умножается на количество товара)"""

        return self.price * self.quantity

    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        return "Электроника"

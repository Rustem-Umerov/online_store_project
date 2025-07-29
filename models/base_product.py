from abc import ABC, abstractmethod
from src.utils import validate_non_negative


class BaseProduct(ABC):
    """
    Базовый абстрактный класс.
    Описывает: название, описание, цену, количество.

    Класс имеет абстрактные методы: price, get_category_name.

    Реализованный метод для определения полной стоимости: total_cost.

    """

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация абстрактного класса.

        Атрибуты:
            name (str): Название.
            description (str): Описание.
            price (float): Цена (рубли с копейками).
            quantity (int): Количество в наличии.

        Методы:
            price: абстрактный геттер цены.
            get_category_name(): абстрактный метод, возвращает категорию.
            total_cost: общее свойство для подсчёта полной стоимости.
        """

        super().__init__()

        validate_non_negative(price, "Price")
        validate_non_negative(quantity, "Quantity")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def get_category_name(self) -> str:
        """Данный метод возвращает название категории класса."""

        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Цена (только для чтения)."""

        return self._price

    @property
    def total_cost(self) -> float:
        """Определена полная стоимость товаров (цена товара умножается на количество товара)"""

        return self.price * self.quantity

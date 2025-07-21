from typing import Iterator

from models.category import Category
from models.product import Product


class ProductIterator:
    """
    Класс ProductIterator перебирает товары одной категории.
    Класс принимает на вход объект класса Category и производит итерацию по товарам(объектам класса Product),
    которые хранятся в данной категории.
    """

    category: Category

    def __init__(self, category_obj: Category) -> None:
        """
        Инициализирует итератор.

        :param category_obj: Объект класса Category.
        """

        self._category = category_obj
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        """Магический метод, который возвращает объект итератора."""

        self._index = 0
        return self

    def __next__(self) -> Product:
        """Магический метод, возвращает следующий элемент последовательности."""

        if self._index >= len(self._category.products):
            raise StopIteration

        product = self._category.products[self._index]
        self._index += 1
        return product

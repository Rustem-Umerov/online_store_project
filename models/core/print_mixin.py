from typing import Any


class PrintMixin:
    """Класс-миксин - при создании объекта, то есть при работе метода __init__,
    печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
    Например: Product('Продукт1', 'Описание продукта', 1200, 10)"""

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация вывода информации, в консоль, полученной от __repr__."""

        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        """Магический метод, для отображения информации об объекте класса в режиме отладки (для разработчиков)
        Выводит информацию в виде: Product('Продукт1', 'Описание продукта', 1200, 10)"""

        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self._price}, {self.quantity})"

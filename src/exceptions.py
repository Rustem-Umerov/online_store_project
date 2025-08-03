class ProductError(Exception):
    """Базовое исключение для всех ошибок, связанных с продуктом."""

    pass


class InvalidPriceError(ProductError, ValueError):
    """Ошибка: цена не может быть нулевой или отрицательной."""

    def __init__(self, value: float) -> None:
        super().__init__(f"Недопустимая цена: {value}. Цена не должна быть нулевой или отрицательной.")
        self.value = value


class PriceDecreaseError(ProductError):
    """Ошибка: попытка понизить цену товара."""

    def __init__(self, old: float, new: float) -> None:
        super().__init__(f"Вы ввели цену: {new}, меньше текущей: {old}.")
        self.old = old
        self.new = new


class NegativeOrZeroQuantityError(ProductError):
    """Ошибка: попытка добавить товар с нулевым или отрицательным количеством в категорию или заказ."""

    def __init__(self, product_name: str) -> None:
        super().__init__(f"Нельзя добавить товар '{product_name}' с нулевым или отрицательным количеством.")

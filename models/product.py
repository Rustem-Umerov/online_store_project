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
    price: float
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
        self.price = price
        self.quantity = quantity


def validate_non_negative(value: float | int, object_: str) -> None:
    """
    Универсальный валидатор. Проверяет значение объекта.
    Если переданное значение отрицательное, то вызывается ошибка ValueError.

    :param value: Значение объекта (float | int).
    :param object_: Название объекта.
    """

    if value < 0:
        raise ValueError(f"{object_} cannot be a negative value.")

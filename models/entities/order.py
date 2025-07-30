from models.entities.product import Product


class Order:
    """Класс выводит ссылку на то:
        * какой товар был куплен,
        * количество купленного товара,
        * а также итоговая стоимость.
    В заказе может быть указан только один товар.
    """

    product: Product
    quantity: int
    final_price: float

    def __init__(self, product: Product, quantity: int) -> None:
        """ """

        if quantity > product.quantity:
            raise ValueError(
                f"Ошибка: вы пытаетесь купить {quantity} ед. товара, "
                f"это больше, чем есть, в наличии {product.quantity}"
            )

        self.product = product
        self.quantity = quantity
        self.final_price = product.price * quantity

        product.quantity -= self.quantity

    def __str__(self) -> str:
        """Вывод информации в консоль (для пользователя)
        Пример: Куплен товар: 'название товара', количество: 'кол-во купленного товара',
        итоговая стоимость: 'итоговая стоимость купленного товара'."""

        return (
            f"Куплен товар: {self.product.name}, количество: {self.quantity}, итоговая стоимость: {self.final_price}."
        )

    def __repr__(self) -> str:
        """Вывод информации в режиме отладки
        Пример: Название товара: 'название товара', количество товара: 'количество товара',
        итоговая стоимость: 'итоговая стоимость'."""

        return (f"Название товара: {self.product.name}, количество товара: {self.quantity}, "
                f"итоговая стоимость: {self.final_price}.")

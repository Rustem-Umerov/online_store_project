from src.exceptions import InvalidPriceError, PriceDecreaseError
from models.product import Product


def update_product_price(product: Product) -> bool:
    """
    Функция для изменения цены продукта.
    Получает на вход объект класса Product и вероятно будущую цену.
    Если предложенная цена соответствует критериям, то значение цены переназначается.
    Если цена меньше или равна нулю, то возникает ошибка.
    Если цена больше нуля, но меньше текущей, то пользователю задается вопрос, желает ли он понизить цену.
    В зависимости от пользовательского вопроса, цена, либо изменяется, либо остается прежней.

    :param product: Объект класса Product
    :return: True/False
    """

    try:
        product.price = float(input("Введите новую цену: "))
        print("Цена успешно обновлена")
        return True

    except InvalidPriceError as err:
        print(f"Ошибка: {err}")
        return False

    except PriceDecreaseError as err:
        print(err)
        answer = input("Хотите понизить цену??? Введите 'y' если (да) или 'n' если (нет)").lower().strip()

        if answer == "y":
            product.force_price_update(err.new)
            print("Цена понижена.")
            return True

        else:
            print("Цена осталась прежней.")
            return False

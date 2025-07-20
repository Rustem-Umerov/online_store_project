from src.exceptions import InvalidPriceError, PriceDecreaseError


def test_invalid_price_error_price_zero() -> None:
    """Тест проверяет, что будет вызвано исключение InvalidPriceError, если цена ноль."""
    exc = InvalidPriceError(0)

    assert isinstance(exc, ValueError)
    assert exc.value == 0
    assert "Недопустимая цена: 0. Цена не должна быть нулевой или отрицательной." in str(exc)


def test_invalid_price_error_price_less_than_zero() -> None:
    """Тест проверяет, что будет вызвано InvalidPriceError, если цена меньше нуля."""

    exc = InvalidPriceError(-5)

    assert isinstance(exc, ValueError)
    assert exc.value == -5
    assert "Недопустимая цена: -5. Цена не должна быть нулевой или отрицательной." in str(exc)


def test_price_decrease_error() -> None:
    """Тест проверяет, что будет вызвано исключение PriceDecreaseError, если новая цена меньше текущей."""

    exc = PriceDecreaseError(old=20, new=10)

    assert exc.old == 20
    assert exc.new == 10
    assert "Вы ввели цену: 10, меньше текущей: 20." in str(exc)

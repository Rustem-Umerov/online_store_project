import pytest
from _pytest.capture import CaptureFixture

from models.core.print_mixin import PrintMixin


class TestProduct(PrintMixin):
    """Тестовый класс для теста класса-миксин PrintMixin."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

        super().__init__()


def test_print_called_on_init(capsys: CaptureFixture) -> None:
    """Тест проверяет, что метод __repr__ в PrintMixin выводит правильный вывод."""

    prod = TestProduct("a", "aaa", 10.1, 5)
    captured = capsys.readouterr()
    assert captured.out == "TestProduct('a', 'aaa', 10.1, 5)\n"
    assert repr(prod) == "TestProduct('a', 'aaa', 10.1, 5)"


class BadProduct(PrintMixin):
    """Тестовый класс для тестирования PrintMixin."""

    def __init__(self) -> None:
        # нет обязательных атрибутов
        super().__init__()


def test_missing_attributes_raises_attribute_error() -> None:
    """Тест проверяет поведение при «неполном» классе BadProduct — ожидается ошибка AttributeError"""

    with pytest.raises(AttributeError):
        BadProduct()

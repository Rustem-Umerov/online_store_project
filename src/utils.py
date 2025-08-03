import json
from pathlib import Path
from typing import Any, Union, Optional


def read_json(js_path: Union[str, Path]) -> dict:
    """
    Функция читает json-файл и возвращает словарь.

    :param js_path: Путь к JSON-файлу (str или Path).
    :return: Распарсенный словарь.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если JSON невалиден.
    """

    path = Path(js_path)
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            data: dict[Any, Any] = json.load(file)

        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in the file {path}: {e}.") from e


def validate_min(value: float | int, min_value: float, object_: str, message: Optional[str] = None ) -> None:
    """
    Универсальный валидатор. Проверяет значение объекта.
    Если переданное значение меньше минимально допустимого, то вызывается ошибка ValueError.

    :param value: Значение объекта (float | int).
    :param min_value: Минимально допустимое значение.
    :param object_: Название объекта.
    :param message: Сообщение об ошибке(опционально).
    """

    if value < min_value:
        if message is None:
            message = f"{object_} не может быть меньше {min_value}."
        raise ValueError(message)

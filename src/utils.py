import json
from pathlib import Path
from typing import Any, Union


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

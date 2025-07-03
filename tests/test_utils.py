import json
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.utils import read_json


@patch("src.utils.open", new_callable=mock_open, read_data=json.dumps({"a": 1, "b": 2, "c": 3}))
def test_read_json_success(mock_open_func: MagicMock) -> None:
    """Тест проверяет успешное открытие json-файла."""

    result = read_json("valid.json")
    assert result == {"a": 1, "b": 2, "c": 3}
    mock_open_func.assert_called_once_with(Path("valid.json"), mode="r", encoding="utf-8")


@patch("src.utils.open", side_effect=FileNotFoundError)
def test_read_json_file_not_found_error(mock_file: MagicMock) -> None:
    """Тестирование ошибки FileNotFoundError."""

    with pytest.raises(FileNotFoundError) as exc_info:
        read_json("no_file.json")

    assert "File not found: no_file.json" in str(exc_info.value)


@patch("json.load", side_effect=json.JSONDecodeError("err", "doc", 0))
@patch("src.utils.open", new_callable=mock_open, read_data="I am not JSON")
def test_read_json_decode_error(mock_json_load: MagicMock, mock_file: MagicMock) -> None:
    """Если json.load бросает JSONDecodeError, read_json должен поймать его
    и выдать ValueError с текстом про invalid JSON."""

    with pytest.raises(ValueError) as exc_info:
        read_json("test_json.json")

    msg = str(exc_info.value)
    assert "Invalid JSON in the file test_json.json" in msg

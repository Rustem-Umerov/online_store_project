# online_store_project

## Описание:

В этом проекте реализован базовый функционал для работы с товарами и категориями 
в интернет-магазине, а также утилиты для валидации и чтения данных из JSON-файлов.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Rustem-Umerov/online_store_project.git
```
1. Перейдите в корневую папку:
```
cd online_store_project
```
1. Установите зависимости с помощью Poetry:
```
poetry install
```

## Функциональные возможности

### Классы модели:

* #### Product

Атрибуты: name, description, price, quantity

Валидация: price и quantity не могут быть отрицательными

* #### Category

Атрибуты: name, description, products (список объектов Product)

Счётчики на уровне класса:

category_count – общее число созданных категорий

product_count – общее число товаров во всех категориях

Валидация: список products может содержать только экземпляры Product


### Утилиты:

* validate_non_negative(value, object_) Проверяет, что числовое значение не отрицательное; при нарушении выбрасывает ValueError

* read_json(js_path: Union[str, Path]) -> dict Читает JSON-файл по пути js_path и возвращает словарь 
При отсутствии файла – FileNotFoundError с указанием пути 
При некорректном JSON – ValueError с описанием ошибки


## Примеры использования
```
from src.utils import read_json
from models.product import Product
from models.category import Category

# Чтение данных из файла
data = read_json("data/products.json")

# Создание продуктов и категории
prod1 = Product(name="Кофе", description="Арабика 1 кг", price=450.0, quantity=10)
prod2 = Product(name="Чай", description="Чёрный листовой", price=300.0, quantity=5)

category = Category(
    name="Напитки",
    description="Горячие и холодные",
    products=[prod1, prod2]
)

print(Category.category_count)  # 1
print(Category.product_count)   # 2
```


## Тестирование:

Чтобы установить pytest, используйте команду:
```
poetry add --group dev pytest
```

В pytest для анализа покрытия кода надо поставить библиотеку pytest-cov:
```
poetry add --group dev pytest-cov
```

Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:

При активированном виртуальном окружении:
```
pytest --cov
```
Через poetry:
```
poetry run pytest --cov
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

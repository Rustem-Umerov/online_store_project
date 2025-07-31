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

### Абстрактный класс: BaseProduct

Базовый абстрактный класс.

Атрибуты: name, description, price, quantity.

Класс имеет абстрактные методы: 
price - возвращает цену (только для чтения), 
get_category_name - данный метод возвращает название категории класса.

Реализованный метод для определения полной стоимости: total_cost.

### Класс-миксин: PrintMixin

PrintMixin: класс-миксин - при создании объекта, то есть при работе метода __init__,
печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
Например: Product('Продукт1', 'Описание продукта', 1200, 10)

### Класс Order

Класс выводит ссылку на то:
* какой товар был куплен,
* количество купленного товара,
* а также итоговая стоимость.
В заказе может быть указан только один товар.

Магический метод __str__ выводит:
Пример: Куплен товар: 'название товара', количество: 'кол-во купленного товара',
        итоговая стоимость: 'итоговая стоимость купленного товара'.

Магический метод __repr__ выводит:
Пример: Название товара: 'название товара', количество товара: 'количество товара',
        итоговая стоимость: 'итоговая стоимость'.

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

* #### Smartphone

Наследуется от Product

Конструктор принимает:

name (str)
description (str)
price (float)
quantity (int)
efficiency (float)
model (str)
memory (float)
color (str)

Метод total_cost возвращает price * quantity

Метод __add__ складывает total_cost двух смартфонов, проверяет, 
что оба объекта одного класса, иначе выдаёт TypeError

Метод get_category_name() возвращает строку "Электроника"

* #### LawnGrass

Наследуется от Product

Конструктор принимает:

name (str)
description (str)
price (float)
quantity (int)
country (str)
germination_period (str)
color (str)

Метод total_cost возвращает price * quantity

Метод __add__ складывает total_cost двух объектов класса LawnGrass, 
проверяет одинаковость типов, иначе выдаёт TypeError

Метод get_category_name() возвращает строку "Сад"


### Утилиты:

* validate_non_negative(value, object_) Проверяет, что числовое значение не отрицательное; при нарушении выбрасывает ValueError

* read_json(js_path: Union[str, Path]) -> dict Читает JSON-файл по пути js_path и возвращает словарь 
При отсутствии файла – FileNotFoundError с указанием пути 
При некорректном JSON – ValueError с описанием ошибки

* Функция assign_to_category
Данная функция отвечает за распределение любых товаров (экземпляров Product и его потомков) 
по заранее определённым категориям.

Основное назначение:

При попытке поместить товар вызывает метод get_category_name() у объекта товара.
Смотрит в словаре categories, где ключи — строки с именами категорий, а значения — объекты Category.
Если подходящая категория найдена, вызывает у неё метод add_product(product) и выводит сообщение об успешном добавлении.
Если ключа нет, бросает исключение ValueError с сообщением о том, что категория не найдена.

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

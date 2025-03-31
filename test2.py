"""Задание Холодильник - задание после первого спринта

Нужно написать пять функций, кеоторые будут создавать товары в холодильнике,
обновлять, удалять, по каждой фффункции будут отдельные описания
"""
from datetime import datetime
from decimal import Decimal

# Словарь пустой.
goods: dict[str, list[dict[Decimal, datetime]]] = {}


def add(
        items: dict,
        title: str,
        amount: Decimal,
        expiration_date=None
        ) -> None:
    """Функция добавляет товары в словарь goods, обновляя его."""

    #  Меняю формат аргумента expiration_date из str --> date.
    formatted_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

    #  Добавляю в словарь  продукты. Если в словае уже есть дубль, то
    #  добавляю через append , так как дубли продуктов возможны.
    if title in items:
        items[title].append(
            {'amount': Decimal(amount), 'expiration_date': formatted_date}
            )
    else:
        items[title] = [
            {'amount': Decimal(amount), 'expiration_date': formatted_date}
            ]


#  проверка работы функции
add(goods, 'Яйца', Decimal('3'), '2023-10-15')
add(goods, 'Яйца', Decimal('7'), '2023-10-20')
add(goods, 'Молоко', Decimal('1.5'), '2023-10-14')
add(goods, 'Редис', Decimal('4'), '2023-10-14')
print(f'Работа первой функции add \n\n {goods}')


def add_by_note(
        items: dict,
        note: str
        ) -> None:
    """Функция добавляет товары забирая данные из одной строки"""

    #  Разбиваем строку на элементы.
    split_note = str.split(note)

    #  Ищу в цикле дату, если нахожу  дефис среди элементов, значит это дата.
    for item in split_note:
        if item[-3:-2] == '-':
            # Находим индекс элемента.
            item_index = split_note.index(item)
            # Вырезаем элемент из списка.
            formatted_date = split_note.pop(item_index)
            formatted_date = datetime.strptime(
                formatted_date, '%Y-%m-%d').date()
        continue
    len_note = len(split_note) - 1
    amount = split_note.pop(len_note)  # Вырезали число.
    title = str.join(' ', split_note)  # Объеденяем название товара
    # Итого достали все три элемента pop_item, number_decimal и sum_note

    # Дублируем с небольшими корректировками наш основной код
    # добавления товаров.
    if title in items:
        items[title].append([
            {'amount': Decimal(amount), 'expiration_date': formatted_date}
            ])
    else:
        items[title] = [
            {'amount': Decimal(amount), 'expiration_date': formatted_date}
            ]


#  Проверка работы функции.
add_by_note(goods, 'Яйца гусиные 2 2023-07-15')
add_by_note(goods, 'Яйца перепелинные 18 2023-07-22')
print(f'\nРабота второй функции add_by_note \n\n {goods}')


def find(
        items:  dict,
        needle: str
        ) -> list[str]:
    """Функция осуществляет поиск по подстрокам"""

    #  Создаю пустой лист.
    found_neddle = []
    #  Перебираю ключи словаря и добавляю в новый лист
    #  при этом привожу все к нижнему регистру.
    for item in items.keys():
        if item.lower().find(needle.lower()) >= 0:
            found_neddle.append(item)
    return found_neddle


second_func = find(goods, 'ц')
#  Проверка работы функции.
print(f'\nРабота третьей функции find . Нашли {second_func}')


def get_amount(
        items:  dict,
        needle: str
        ) -> Decimal:
    """Функция возвращакт количество элементов, которые были найдены поиском"""

    amount = []
    #  Перебираю ключи словаря и добавляю в новый лист
    #  при этом привожу все к нижнему регистру.
    for item in items.keys():
        if item.lower().find(needle.lower()) >= 0:
            for i in goods[item]:
                amount.append(i['amount'])
            #  res = sum(i['amount'] for i in goods[item])
    result = sum(amount)
    return Decimal(result)


foth_func = get_amount(goods, 'Яйца')
print(f'\nРабота четвернтой функции get_amount, сумма равна << {foth_func} >>')


def get_expired(items, in_advance_days=0):
    ...
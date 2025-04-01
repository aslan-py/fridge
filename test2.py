"""Задание Холодильник - задание после первого спринта

Нужно написать пять функций, кеоторые будут создавать товары в холодильнике,
обновлять, удалять, по каждой фффункции будут отдельные описания
"""
import datetime
from datetime import datetime, timedelta
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
    if expiration_date != None:
        formatted_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    else:
        formatted_date = None

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
add(goods, 'Яйца', Decimal('3'), '2025-03-31')
add(goods, 'Молоко', Decimal('7'))
print(f'Работа первой функции add \n\n {goods}')



def add_by_note(
        items: dict,
        note: str
        ) -> None:
    """Функция добавляет товары забирая данные из одной строки"""

    #  Разбиваем строку на элементы.
    split_note = str.split(note)
    formatted_date = None
    #  Ищу в цикле дату, если нахожу  дефис среди элементов, значит это дата.
    if '-' in split_note[-1]:
        formatted_date = split_note.pop()

    amount = split_note.pop()  # Вырезали число.
    title = str.join(' ', split_note)  # Объеденяем название товара
    # Итого достали все три элемента pop_item, number_decimal и sum_note

    # Дублируем с небольшими корректировками наш основной код
    # добавления товаров.
    add(items, title, amount, formatted_date)


#  Проверка работы функции.
add_by_note(goods, 'Яйца гусиные 2 2025-04-2')
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
    for word in items.keys():
        if word.lower().find(needle.lower()) >= 0: #  если в искомом ключе(или слове) мы находим заданное слово
            found_neddle.append(word) #  то добавляем это найденное слово в отдельный список
    return found_neddle


second_func = find(goods, 'Яйца')
#  Проверка работы функции.
print(f'\nРабота третьей функции find . Нашли {second_func}')


def get_amount(
        items:  dict,
        needle: str
        ) -> Decimal:
    result = 0
    """Функция возвращакт количество элементов, которые были найдены поиском"""
    for word in find(items, needle): #  Перебираю слова испоьзуя ранее сделанную фунгкцию find
        result = result + sum(key['amount'] for key in items[word]) #  Провалился в словарь внутренний, и дкергаю оттуда значения, суммирую результат
    return (Decimal(result))


result = get_amount(goods, 'яйца')
print(f'\nРабота четвертой функции get_amount. Сумма =  {result}')


def get_expired(items, in_advance_days=0):
    s = []
    for keys, values  in items.items():
        for value in items[keys]:
            if value['expiration_date'] != None:
                if value['expiration_date'] <= datetime.today().date() + timedelta(days = in_advance_days):
                    s.append((keys,Decimal(value['amount'])))
    return s


print(get_expired(goods,2))

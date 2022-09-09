def task1():
    while True:
        year = input("Введите год: ")
        try:
            year = int(year)
        except ValueError:
            print("Введите целочисленный год!")
            continue
        if year == 0:
            print("Выход из китайского календаря")
            break
        else:
            china_year(year)


def china_year(year):
    # Написать функцию, которая определяет год по китайскому календарю,
    # ввод данных закончить, когда пользователь ввел 0.
    # Сделать проверку на правильность введенных данных.
    china_calendar = {0: "обезьяна", 1: "петух", 2: "собака", 3: "свинья", 4: "крыса", 5: "бык", 6: "тигр",
                      7: "кот", 8: "дракон", 9: "змея", 10: "лошадь", 11: "коза"}
    print("Животное года:", china_calendar[year % 12])


def task2():
    # Посчитать, сколько пар (стоят рядом) верхнего и нижнего
    # регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1
    # пара нижнего, 1 пара верхнего), а также сколько гласных букв в слове.
    count_lower = count_upper = count_vowel_letter = 0
    english_vowels = ('e', 'y', 'u', 'i', 'o', 'a')
    russian_vowels = ('у', 'е', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё', 'ы')
    input_string = input("Введите строку: ")
    for i in range(len(input_string) - 1):
        if input_string[i].islower() and input_string[i + 1].islower():
            count_lower += 1
        elif input_string[i].isupper() and input_string[i + 1].isupper():
            count_upper += 1
        if input_string[i].lower() in english_vowels or input_string[i].lower() in russian_vowels:
            count_vowel_letter += 1
    if input_string[len(input_string) - 1].lower() in english_vowels \
            or input_string[len(input_string) - 1].lower() in russian_vowels:
        count_vowel_letter += 1
    print("Итого:\n Пар нижнего регистра:", count_lower, "\n Пар верхнего регистра:", count_upper,
          "\n Гласных букв:", count_vowel_letter)


def task3():
    # Найдите сумму положительных элементов списка.
    # Найдите сумму элементов списка после первого нуля.
    # Если нулевых элементов нет в списке, то выведите «Сумму посчитать нельзя».
    # Удалить из списка все отрицательные элементы
    summary = summary_after_zero = 0
    is_zero_exists = 0
    input_list = []
    count = int(input("Сколько чисел Вы хотите добавить? "))
    for i in range(count):
        input_list.append(int(input("Введите число: ")))
    i = 0
    while i < len(input_list):
        if is_zero_exists == 1:
            summary_after_zero += input_list[i]
        if int(input_list[i]) > 0:
            summary += input_list[i]
        elif int(input_list[i]) == 0 and is_zero_exists == 0:
            is_zero_exists = 1
        else:
            input_list.pop(i)
            continue
        i += 1
    print("Сумма чисел больше нуля:", summary)
    if is_zero_exists == 0:
        print("Сумму посчитать нельзя, нет ни одного нуля")
    else:
        print("Сумма чисел после нуля:", summary_after_zero)
    print("Теперь список выглядит так:", input_list)


def task4():
    # Дана строка в виде случайной последовательности чисел от 0 до 9.
    # Требуется создать словарь, который в качестве ключей будет
    # принимать данные числа (т. е. ключи будут типом int), а в качестве
    # значений – количество этих чисел в имеющейся последовательности
    input_list = input("Введите строку: ")
    if input_list.isdigit() is False:
        print("Строка состоит не из цифр!")
        return
    input_list = [int(n) for n in input_list]
    dictionary = dict.fromkeys(input_list)
    for key_name, val in dictionary.items():
        counter = 0
        for k in input_list:
            if k == key_name:
                counter += 1
        dictionary[key_name] = counter
    print("Словарь: ", dictionary)


def description(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", "".join(val[0]))


def price_list(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", val[1], "руб.")


def quantity(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", val[2], "грамм")


def all_info(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, " -> ", "".join(val[0]), ", ", val[1], " руб., ", val[2], " грамм", sep='')


def purchase(dictionary):
    product = input("Введите название продукции: ")
    var = dictionary.get(product)
    if var is None:
        print("Нет такого наименования!")
        return
    amount = int(input("Введите количество в граммах: "))
    if amount <= 0:
        print("Отрицательное количество!")
        return
    if amount > var[2]:
        print("Нет в наличии столько продукции!\nЕсть только", var[2], "грамм!")
        return
    summary = var[1] * amount / 100
    var[2] -= amount
    print("Приобретено продукции на", summary, "руб.")


def menu():
    while True:
        print("Список заданий:\n "
              "1. Китайский календарь\n "
              "2. Работа с функцией\n "
              "3. Матрица\n "
              "4. Исключения\n "
              "0. Выход")
        variant = int(input("Выберите задание: "))
        if variant > 4 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


menu()

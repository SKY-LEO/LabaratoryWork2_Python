import datetime


def task1():
    # Написать функцию, которая определяет год по китайскому календарю,
    # ввод данных закончить, когда пользователь ввел 0.
    # Сделать проверку на правильность введенных данных.
    while True:
        year = input("Введите год: ")
        try:
            year = int(year)
        except ValueError:
            print("Введите целочисленный год!")
            continue
        except Exception:
            print("Ошибка!")
            continue
        if year == 0:
            print("Выход из китайского календаря")
            break
        else:
            china_year(year)


def china_year(year):
    china_calendar = {0: "обезьяна", 1: "петух", 2: "собака", 3: "свинья", 4: "крыса", 5: "бык", 6: "тигр",
                      7: "кот", 8: "дракон", 9: "змея", 10: "лошадь", 11: "коза"}
    print("Животное года:", china_calendar[year % 12])


def func(var):
    print("Тип входной переменной:", type(var))
    if isinstance(var, list):
        is_zero = False
        summary = i = 0
        while i < len(var):
            if is_zero:
                summary += var[i]
            if var[i] < 0:
                var.pop(i)
                continue
            elif var[i] == 0 and is_zero is False:
                is_zero = True
            i += 1
        print("Теперь список выглядит так:", var, "\nСумма в получившемся списке:", summary)
    elif isinstance(var, tuple):
        temp_list = list(var)
        index_max_number = temp_list.index(max(temp_list))
        index_min_number = temp_list.index(min(temp_list))
        temp_list[index_min_number], temp_list[index_max_number] \
            = temp_list[index_max_number], temp_list[index_min_number]
        var = tuple(temp_list)
        print("Теперь кортеж выглядит так:", var)
    elif isinstance(var, int):
        summary = 0
        while var > 0:
            x = var % 10
            if x % 2 != 0:
                summary += x
            var //= 10
        print("Сумма нечетных цифр:", summary)
    elif isinstance(var, str):
        counter = 0
        var = var.split()
        for i in var:
            if len(i) % 2 == 0:
                counter += 1
        print("Количество слов с четной длиной:", counter)
    else:
        print("Ошибка!")


def task2():
    # Напишите функцию, которая будет принимать один аргумент.
    # Если в функцию передаётся список, удалить все отрицательные элементы.
    # Найти в новом списке сумму после первого нулевого элемента.
    # Если кортеж, найти максимальный и минимальный элементы. Поменять их местами.
    # Число – найти сумму нечетных цифр.
    # Строка – подсчитывает количество слов, которые имеют четную длину.
    # Сделать проверку со всеми этими случаями
    variant = input("Что вы хотите создать?\n "
                    "1. Список\n "
                    "2. Кортеж\n "
                    "3. Число\n "
                    "4. Строку\n")
    try:
        variant = int(variant)
    except ValueError:
        print("Введите целочисленное число!")
        return
    except Exception:
        print("Ошибка!")
        return
    input_numbers = input("Введите числа: ")
    match variant:
        case 1:
            try:
                input_numbers = list(map(int, input_numbers.split()))
            except ValueError:
                print("Введите целочисленное число!")
                return
            except Exception:
                print("Ошибка!")
                return
        case 2:
            try:
                input_numbers = tuple(map(int, input_numbers.split()))
            except ValueError:
                print("Введите целочисленное число!")
                return
            except Exception:
                print("Ошибка!")
                return
        case 3:
            try:
                input_numbers = int(input_numbers)
            except ValueError:
                print("Введите целочисленное число!")
                return
            except Exception:
                print("Ошибка!")
                return
        case 4:
            if all(j.isalpha() or j.isspace() for j in input_numbers):
                print("Введены слова")
            else:
                print("Введите слова!")
                return
        case _:
            print("Ошибка!")
    func(input_numbers)


class ZeroMatrixError(Exception):
    pass


def task3():
    # Дана целочисленная прямоугольная матрица.
    # Определить количество столбцов, не содержащих ни одного нулевого элемента
    n = input("Введите количество строк: ")
    try:
        n = int(n)
    except ValueError:
        print("Введите целочисленное число!")
        return
    m = input("Введите количество столбцов: ")
    try:
        m = int(m)
    except ValueError:
        print("Введите целочисленное число!")
        return
    try:
        if n == 0 or m == 0:
            raise ZeroMatrixError
    except ZeroMatrixError:
        print("Нулевая матрица!")
        return
    matrix = []
    for line in range(n):
        column_list = []
        print("Строка #", line + 1, sep='')
        for column in range(m):
            value = input("Введите число: ")
            try:
                value = int(value)
            except ValueError:
                print("Введите целочисленное число!")
                return
            column_list.append(value)
        matrix.append(column_list)
    counter = 0
    is_zero_exist = False
    for j in range(m):
        for i in range(n):
            if matrix[i][j] == 0:
                is_zero_exist = True
                break
        if is_zero_exist:
            is_zero_exist = False
        else:
            counter += 1
    print("Исходная матрица:")
    for line in matrix:
        print(line)
    print("Количество строк, не содержащих нуля:", counter)


class FutureYearError(Exception):
    pass


class TooOldError(Exception):
    pass


def task4():
    # Напишите программу, демонстрирующую работу try\except\finally
    now = datetime.datetime.now()
    year = input("Введите год окончания университета: ")
    try:
        year = int(year)
        if year > now.year:
            raise FutureYearError
        elif year < now.year - 100:
            raise TooOldError
    except ValueError:
        print("Введите целочисленное число!")
    except FutureYearError:
        print("Этот год ещё не наступил!")
    except TooOldError:
        print("Слишком давно!")
    except Exception:
        print("Ошибка!")
    else:
        print("Ваш год окончания университета подтвержден!")
    finally:
        print("До свидания!")


def menu():
    while True:
        print("Список заданий:\n "
              "1. Китайский календарь\n "
              "2. Работа с функцией\n "
              "3. Матрица\n "
              "4. Исключения\n "
              "0. Выход")
        variant = input("Выберите задание: ")
        try:
            variant = int(variant)
        except ValueError:
            print("Введите целочисленное число!")
            continue
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

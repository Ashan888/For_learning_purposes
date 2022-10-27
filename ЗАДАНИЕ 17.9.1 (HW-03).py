def magneto_meme():
    try:
        array = list(input("Введите последовательность целых чисел больше 0  "
                         "через пробел и без запятых, например 1 2 3 5: "))
        # тут должна быть проверка на наличие пробела, но реализовать ее не получилось.
        array = [x for x in array if len(x.strip())]  # убирает пробелы из списка если есть
        arr_to_str = "".join(map(str, array))  # превращение списка в строку-число не изменяя список
        if not arr_to_str.isdigit():  # если строка не число, то
            raise ValueError(arr_to_str)
    except ValueError as error:
        print("Я сказал: 'Введите последовательность целых чисел больше 0 "
              "через пробел и без запятых, например 1 2 3 5.'!",
              error)
        return magneto_meme()
    else:
        print(f'Превосходно! {arr_to_str}')
        return array


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


array = magneto_meme() # array была локальной переменной, теперь глобальная


def sort_by_replace():  # функция сортирует список методом перестановки
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    print(array)
    return array


array = sort_by_replace()


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if int(array[middle]) == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < int(array[middle]):  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


def magneto_meme2():
    try:
        element = int(input("Введите 1 целое число:"))
        if not isinstance(element, int):
            raise ValueError(element)
    except ValueError as error:
        print("Я сказал: 'Введите целое число'!", error)
        return magneto_meme2()
    else:
        print(f'Превосходно! {element}')
        return element


element = magneto_meme2()
# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, len(array)))

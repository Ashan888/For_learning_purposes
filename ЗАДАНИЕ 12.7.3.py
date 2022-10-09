#Программа не считает копейки:
money = int(input("Введите сумму больше 107р (Копейки не считает!) : "))

#per_cent - ГОДОВАЯ процентная ставка
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(per_cent.values())

deposit = [int((deposit[0]) * (money/100)),
           int((deposit[1]) * (money/100)),
           int((deposit[2]) * (money/100)),
           int((deposit[3]) * (money/100))]

print('Накопления за год', deposit)
print('Наибольшее накопление', max(deposit))


#Программа считает копейки, в т. ч. в ответе:
money_float = float(input("Введите сумму в формате рубль.копейка (например 10.08) : "))
deposit_float = list(per_cent.values())
deposit_float = [round(((deposit_float[0]) / 100 * money), 2),
                 round(((deposit_float[1]) / 100 * money), 2),
                 round(((deposit_float[2]) / 100 * money), 2),
                 round(((deposit_float[3]) / 100 * money), 2)]
print('Накопления за год (с копейками)', deposit_float)
print('Наибольшее накопление', max(deposit_float))
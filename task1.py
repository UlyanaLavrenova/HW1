a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a == b or a == c or b == c:
    print("Хотя бы одна пара одинаковых чисел существует")
else:
    print("Ни одной пары одинаковых чисел нет")
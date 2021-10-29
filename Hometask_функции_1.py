# Калькулятор

def calc(num_1, operator, num_2):
    res = 0
    if operator == "+":
        res = num_1 + num_2
    elif operator == "-":
        res = num_1 - num_2
    elif operator == "**":
        res = num_1 * num_2
    elif operator == "/":
        res = num_1 / num_2
    return res
num_1 = int(input("Введите значение 1"))
num_2 = int(input("Введите значение 2"))
operator = input("Введите знак операции (+, -, *, /)")
print(calc(num_1, operator, num_2))

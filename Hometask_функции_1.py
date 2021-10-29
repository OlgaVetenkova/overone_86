# Калькулятор

def calc(num_1, operator, num_2):
    if operator == "+":
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1 * num_2)
    elif operator == "/":
        print(num_1 / num_2)
num_1 = int(input("Введите значение 1"))
num_2 = int(input("Введите значение 2"))
operator = input("Введите знак операции (+, -, *, /)")
print(calc(num_1, operator, num_2))
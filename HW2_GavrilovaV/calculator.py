# %%
"""
Программа должна принимать на вход (через input()) строку
с некоторым математическим выражением и печатать число - результат вычисления этого выражения.

Гарантируется что выражение состоит из двух чисел (int или float) и математического оператора
между ними (один из 4: + - * /). Все указанные элементы разделены пробелами (пример: 5 - 3).

Реализуйте внутри скрипта 5 функций: main и 4 отдельные
функции на каждый из типов математических операций.
Функция main внутри себя должна принимать входное выражение,
отдавать его на вычисление соответствующей функции, получать результат и печатать его на экран.
Каждая из 4 функций лишь принимает определенное выражение от главной функции, вычисляет его и
результат главной функции.

"""


# %%
def sum_func(num1, num2):  # defining summation func
    return num1 + num2

def ded_func(num1, num2): # defining subtraction function
    return num1 - num2

def mult_func(num1, num2):  # defining multiplication function
    return num1 * num2

def div_func(num1, num2):  # defining division function
    res = num1 / num2
    
    return res
# %%
"""
defining MAIN FUNCTION
"""


def main_func():
    """
    accepts the line from the user
    divides into numbers and operation
    sends to a corresponding function
    receives the result from the function
    prints the result
    """
    valid = False
    while not valid:
        user_line = input()  # users enters
        line = str(user_line)
        line_list = line.split(" ")  # return list of len(elements spaced by whitespace)

        # splitting the line into parts
        operator = line_list[1]
        first_num = float(line_list[0])
        second_num = float(line_list[2])

        # sending to the corresponding func
        """
        I assume that the following functions will be accepting two numbers
        The namings of the functions
        
            for deduction: ded_func
            for summation: sum_func
            for multiplication: mult_func
            for division: div_func
        
        """
        # valid = False
        # while not valid:

        if operator == "+":
            valid = True
            res = sum_func(num1=first_num, num2=second_num)

        elif operator == "-":
            valid = True
            res = ded_func(num1=first_num, num2=second_num)

        elif operator == "*":
            valid = True
            res = mult_func(num1=first_num, num2=second_num)

        elif operator == "/":
            valid = True
            res = div_func(num1=first_num, num2=second_num)

        else:
            valid = False
            print("Operation Type Error. Enter the operation again")

    print(res)


# %%
"""
run function
"""

operation_result = main_func()


# %%

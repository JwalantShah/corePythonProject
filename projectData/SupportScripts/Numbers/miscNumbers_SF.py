from projectData.SupportScripts.globalUDFs import *


def factorial(number):
    facto = number
    if number > 0:
        return facto * factorial(facto - 1)
    elif number == 0:
        return 1


def generate_fibonacci(count):
    pass
    fibonacci_list = [0, 1]
    p = 0
    q = 1
    while len(fibonacci_list) <= count:
        temp = p + q
        p = q
        q = temp
        fibonacci_list.append(temp)
    return fibonacci_list


def nth_element_fibonacci(n):
    if n > 2:
        i = 2
        p = 0
        q = 1
        while i < n:
            q = p + q
            p = q - p
            i += 1
        return q
    elif n == 2:
        return 1
    elif n == 1:
        return 0


def palindrome(number):
    com = ''
    if number != ''.join(number[::-1]):
        com = ' NOT'
    print(f'{number} IS{com} A PALINDROME NUMBER')



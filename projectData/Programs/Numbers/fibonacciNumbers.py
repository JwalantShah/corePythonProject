"""DEMONSTRATION OF FIBONACCI NUMBERS"""
from projectData.SupportScripts.Numbers.fibonacciNumbers_SF import *


def main():
    path = 'projectData/Data/Numbers/'
    fib = FibonacciManager(path)
    con = 'Y'
    while con.upper() == 'Y':
        colorPrint('\n----------------------------------------------: WELCOME TO THE LAND OF FIBONACCI NUMBERS '
                   ':----------------------------------------------\n', 'Orange')
        fib.status()
        print('PRESS 1. TO CHECK WHETHER THE NUMBER IS FIBONACCI OR NOT :\n'
              'PRESS 2. TO GENERATE FIRST N FIBONACCI NUMBERS.\n'
              'PRESS 3. TO FIND FIBONACCI NUMBERS BETWEEN TWO NUMBERS.\n'
              'PRESS 4. TO FIND THE N FIBONACCI NUMBERS AFTER A NUMBER.\n'
              'PRESS 5. TO FIND N FIBONACCI NUMBERS BEFORE A NUMBER.\n'
              'PRESS 6. TO FIND THE FIBONACCI NUMBER AT NTH POSITION.\n'
              'PRESS 7. TO FIND THE FIBONACCI NUMBERS BETWEEN MTH AND NTH POSITION IN FIBONACCI SEQUENCE.\n'
              'PRESS 0. TO EXIT.\n')

        choice = rangeInput(0, 8, 'ENTER YOUR CHOICE HERE : ')
        if choice == 1:
            number = rangeInput(0, 0, 'ENTER NUMBER FOR WHICH YOU WANT TO CHECK IT IS FIBONACCI OR NOT : '
                                , category=5)
            result = fib.is_fibonacci(number)
            if result[0]:
                text = ''
            else:
                text = ' NOT'
            colorPrint(f'NUMBER {number} IS{text} A FIBONACCI NUMBER', 'Saffron')
            if result[1] != 0:
                colorPrint(f'IT IS POSITIONED AT THE {result[1]}TH POSITION IN THE FIBONACCI SEQUENCE.', 'Saffron')
        elif choice == 2:
            numbers_to_find = rangeInput(1, 0,
                                         'STARTING FROM FIRST, HOW MANY FIBONACCI NUMBERS YOU WANT TO FIND ? : '
                                         , category=5)
            colorPrint(f"FIRST {str(numbers_to_find)} FIBONACCI NUMBERS ARE : "
                       f"{reset}{' , '.join(map(str, fib.get_n_fibonacci(numbers_to_find)))}",
                       'Saffron')
        elif choice == 3:
            start = fib.take_input_benchmark('FROM')
            end = fib.take_input_benchmark('UPTO')
            numbers_list = fib.find_fibonacci_in_range(start, end)
            colorPrint(f"BETWEEN {start} AND {end} THERE ARE TOTAL {str(len(numbers_list))} FIBONACCI NUMBERS.")
            if numbers_list:
                print(f"THEY ARE {', '.join(map(str,numbers_list))}")
        elif choice == 4:
            number = fib.take_input_benchmark('AFTER')
            numbers_to_find = fib.take_input_n()
            fib.find_fibonacci_before_or_after(number, numbers_to_find, 1)
        elif choice == 5:
            number = fib.take_input_benchmark('BEFORE')
            numbers_to_find = fib.take_input_n()
            fib.find_fibonacci_before_or_after(number, numbers_to_find, -1)
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        elif choice == 0:
            fib.save_fibonacci()
            break

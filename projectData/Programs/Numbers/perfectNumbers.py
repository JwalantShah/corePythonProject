""""DEMONSTRATION OF PERFECT,DEFICIENT AND ABUNDANT NUMBERS."""
from projectData.SupportScripts.Numbers.perfectNumbers_SF import *


def main():
    while True:
        colorPrint('\n---------------------: WELCOME TO THE LAND OF PERFECT,DEFICIENT,ABUNDANT NUMBERS '
                   ':---------------------------------\n', 'Orange')
        print('\nPRESS 1. TO CHECK WHETHER NUMBER IS PERFECT, DEFICIENT OR ABUNDANT.'
              '\nPRESS 2. TO GENERATE SEQUENCE OF FIRST N OF PERFECT,DEFICIENT OR ABUNDANT NUMBERS.'
              '\nPRESS 3. TO GENERATE PERFECT, DEFICIENT AND ABUNDANT NUMBERS IN SPECIFIED RANGE.'
              '\nPRESS 4. TO GENERATE N PERFECT,DEFICIENT OR ABUNDANT NUMBERS WHICH ARE HIGHER THEN A CERTAIN NUMBER'
              '\nPRESS 5. TO GENERATE N PERFECT,DEFICIENT OR ABUNDANT NUMBERS WHICH ARE LOWER THEN A CERTAIN NUMBER')
        choice = valInput('\nENTER YOUR CHOICE HERE : ')
        if choice == 0:
            break
        elif choice == 1:
            number = valInput('\nENTER A NUMBER FOR WHICH YOU WANT TO CHECK HERE : ')
            if number < 1:
                colorPrint('SORRY, WE CAN NOT CHECK FOR THE NEGATIVE INTEGERS OR ZERO (0).BECAUSE THE CONCEPT OF  '
                           'PERFECT,DEFICIENT AND ABUNDANT NUMBERS IS ONLY VALID FOR POSITIVE INTEGERS.', 'Yellow')
            check_perfect(number)
        elif choice == 2:
            number_type, numbers_to_generate = input_choice()
            generate_n_perfect_number(1,numbers_to_generate,number_type,0)
        elif choice == 3:
            start = int(rangeInput(1, 'x', 'ENTER STARTING RANGE :', 'INVALID INPUT', 4))
            end = int(rangeInput(1, 'x', 'ENTER ENDING RANGE :', 'INVALID INPUT', 4))
            generate_perfect_numbers_in_range(start, end)
        elif choice == 4:
            benchmark, number_to_generate, number_type = input_choices2('AFTER')
            generate_n_perfect_number(benchmark, number_to_generate, number_type)
        elif choice == 5:
            benchmark, number_to_generate, number_type = input_choices2('BEFORE')
            generate_n_perfect_number(benchmark, number_to_generate, number_type, -1)

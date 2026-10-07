"""DEMONSTRATION OF HARSHAD(NIVEN) NUMBER"""
from projectData.SupportScripts.Numbers.harshadNumber_SF import *


def main():
    while True:
        colorPrint('\n--------------------------------------: WELCOME TO THE LAND OF HARSHAD NUMBER :-'
                   '--------------------------------------\n', 'Orange')
        print('\nPRESS 1. TO CHECK WHETHER A NUMBER IS HARSHAD OR NOT.'
              '\nPRESS 2. TO GENERATE FIRST N HARSHAD NUMBER.'
              '\nPRESS 3. TO GENERATE HARSHAD NUMBERS IN BETWEEN TWO NUMBERS.'
              '\nPRESS 4. TO GENERATE N HARSHAD NUMBER AFTER A CERTAIN NUMBER.'
              '\nPRESS 5. TO GENERATE N HARSHAD NUMBER BEFORE A NUMBER.'
              '\nPRESS 0. TO GO BACK.')
        choice = valInput('\nENTER YOUR CHOICE HERE : ', category=0)
        if choice == 0:
            break
        elif choice == 1:
            number = valInput('ENTER NUMBER TO CHECK WHETHER IT IS HARSHAD NUMBER OR NOT : ')
            check_harshad(number)
        elif choice == 2:
            number_to_generate = take_input_count()
            generate_n_harshad_number(1, number_to_generate, 0)
        elif choice == 3:
            start = take_input_benchmark('FROM')
            end = take_input_benchmark('UPTO')
            generate_harshad_in_range(start,end)
        elif choice == 4:
            benchmark = take_input_benchmark('AFTER')
            number_to_generate = take_input_count()
            generate_n_harshad_number(benchmark,number_to_generate,1)
        elif choice == 5:
            benchmark = take_input_benchmark('BEFORE')
            number_to_generate = take_input_count()
            generate_n_harshad_number(benchmark,number_to_generate,-1)

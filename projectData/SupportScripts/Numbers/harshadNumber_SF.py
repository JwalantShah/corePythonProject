from projectData.SupportScripts.globalUDFs import *


def generate_harshad_in_range(lower, upper):
    if lower > upper:
        lower = lower + upper
        upper = lower - upper
        lower = lower - upper
    number_list = []
    for i in range(lower, upper):
        if is_harshad(i)[0]:
            number_list.append(i)
    colorPrint(f"TOTAL {str(len(number_list))} HARSHAD NUMBERS ARE FOUND  BETWEEN {lower} AND {upper}.\n"
               f" THEY ARE : {reset}{' , '.join(map(str, number_list))}", 'Saffron')


def is_harshad(number):
    digits = list(map(int, str(number)))
    sum_of_digits = sum(digits)
    harshad = False if number % sum_of_digits != 0 else True
    return harshad, digits, sum_of_digits


def check_harshad(number):
    harshad, digits, sum_of_digits = is_harshad(number)
    result_text = ' NOT' if not harshad else ''

    colorPrint2(
        f"THE NUMBER {number} IS{result_text} A HARSHAD (NIVEN) NUMBER.{reset} "
        f"BECAUSE SUM OF ITS DIGITS IS: {' + '.join(map(str, digits))} = {sum_of_digits}, "
        f"WHICH CAN{result_text} DIVIDE THE NUMBER {number}.", 'Saffron'
    )


def generate_n_harshad_number(benchmark, numbers_to_generate, step=1):
    current_number = benchmark
    count = 0
    con = True
    if step == 0:
        step = 1
        con = False
    elif step == -1:
        text_to_print = 'BEFORE'
    elif step == 1:
        text_to_print = 'AFTER'
    number_list = []
    while current_number > 0:
        if count == numbers_to_generate:
            break
        if is_harshad(current_number)[0]:
            number_list.append(current_number)
            count += 1
        current_number += step
    if con:
        colorPrint(f"{count} HARSHAD NUMBERS {text_to_print} NUMBER {benchmark} ARE :{reset}"
                   f" {' , '.join(map(str, number_list))}", 'Saffron')
    else:
        colorPrint(f"FIRST {numbers_to_generate} HARSHAD NUMBERS ARE : {reset}{' , '.join(map(str, number_list))}",
                   'Saffron')


def take_input_benchmark(text):
    benchmark = rangeInput(1, 0, f'\nENTER A NUMBER {text} WHICH YOU WANT TO GENERATE HARSHAD NUMBER : '
                           , 'PLEASE ENTER A VALID POSITIVE INTEGER GREATER THAN 0', 5)
    return benchmark


def take_input_count():
    number_to_generate = rangeInput(1, 0, '\nENTER TOTAL HARSHAD NUMBERS THAT YOU WANT TO '
                                          'GENERATE : ', 'PLEASE ENTER A VALID POSITIVE '
                                                         'INTEGER GREATER THAN 0', 5)
    return number_to_generate

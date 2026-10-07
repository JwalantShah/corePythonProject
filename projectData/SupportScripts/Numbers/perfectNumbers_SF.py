from projectData.SupportScripts.globalUDFs import *


def input_choice():
    print('PRESS 1. FOR PERFECT NUMBERS.\nPRESS 2. FOR DEFICIENT NUMBER.\nPRESS 3. FOR ABUNDANT NUMBER')
    number_type = rangeInput(1, 4, 'ENTER YOUR CHOICE HERE : ')
    numbers_to_generate = valInput('ENTER THE TOTAL NUMBERS THAT YOU WANT TO GENERATE : ')
    return number_type, numbers_to_generate


def input_choices2(g_or_l):
    benchmark = valInput(f'ENTER BENCHMARK VALUE {g_or_l} WHICH YOU WANT TO GENERATE THE NUMBERS : ')
    number_type, numbers_to_generate = input_choice()
    return benchmark, numbers_to_generate, number_type


def generate_n_perfect_number(benchmark, numbers_to_generate, number_type, step=1):
    number_list = []
    count = 0
    current_number = benchmark
    if step == 1:
        low_or_high = 'AFTER'
    elif step == -1:
        low_or_high = 'BEFORE'
    elif step == 0:
        low_or_high = 0
        step = 1
    while current_number > 0:
        if count == numbers_to_generate:
            break
        total = sum(find_factors(current_number))
        if number_type == 1:
            if total == current_number:
                number_list.append(current_number)
                count += 1
        elif number_type == 2:
            if total < current_number:
                number_list.append(current_number)
                count += 1
        elif number_type == 3:
            if total > current_number:
                number_list.append(current_number)
                count += 1
        current_number += step

    number_type_list = ['PERFECT', 'DEFICIENT', 'ABUNDANT']


    if count != 0:
        if low_or_high == 0:
            colorPrint(f"THE FIRST {count} {number_type_list[number_type - 1]} NUMBERS WHICH ARE ARE : {reset}"
                       f"{' , '.join(map(str, number_list))} ", 'Yellow')
        else:
            colorPrint(f"{count} {number_type_list[number_type - 1]} NUMBERS WHICH ARE {low_or_high} {benchmark} ARE : "
                       f"{reset} {' , '.join(map(str, number_list))} ", 'Yellow')
    else:
        colorPrint('SORRY WE ARE UNABLE TO GENERATE THE DESIRED OUTPUT.','Yellow')


def generate_perfect_numbers_in_range(start, end):
    perfect_list = []
    deficient_list = []
    abundant_list = []
    if start == 1:
        perfect_list.append(10)
    for i in range(start, end + 1):
        total = sum(find_factors(i))
        if total == i:
            perfect_list.append(i)
        elif total < i:
            deficient_list.append(i)
        else:
            abundant_list.append(i)
    colorPrint(f'BETWEEN {start} AND {end} THERE IS/ARE TOTAL {str(len(perfect_list))} PERFECT NUMBERS.',
               'Orange')
    if len(perfect_list) != 0:
        print(f"WHICH ARE : {' , '.join(map(str, perfect_list))} \n")

    colorPrint(f'BETWEEN {start} AND {end} THERE IS/ARE TOTAL {str(len(deficient_list))} DEFICIENT NUMBERS.',
               'Orange')
    if len(deficient_list) != 0:
        print(f"WHICH ARE : {' , '.join(map(str, deficient_list))} \n")

    colorPrint(f'BETWEEN {start} AND {end} THERE IS/ARE TOTAL {str(len(abundant_list))} ABUNDANT NUMBERS.',
               'Orange')
    if len(abundant_list) != 0:
        print(f"WHICH ARE : {' , '.join(map(str, abundant_list))} \n")


def find_factors(number):
    if number == 1:
        return [0, ]
    factor_list = [1]

    # Iterate only upq2 to the square root of the number to find divisors efficiently
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factor_list.append(i)
            # Add the complement divisor if it's different from i
            if i != number // i:
                factor_list.append(number // i)
    return factor_list


def is_perfect(number):
    if number == 1:
        return 1, [0]
    factor_list = find_factors(number)
    total = sum(factor_list)
    if total == number:
        return 0, factor_list
    elif total < number:
        return 1, factor_list
    else:
        return 2, factor_list


def check_perfect(number):
    flag, factor_list = is_perfect(number)
    factor_list.sort()  # Sort the list for better readability
    factor_string = ' + '.join(map(str, factor_list))

    if flag == 0:
        print(f'THE NUMBER {number} IS A PERFECT NUMBER. BECAUSE SUM OF ITS PROPER ALL DIVISORS WITHOUT THE NUMBER '
              f'ITSELF IS, {factor_string} WHICH IS = {number}')
    elif flag == 1:
        print(f'THE NUMBER {number} IS A DEFICIENT NUMBER. BECAUSE SUM OF ITS ALL PROPER ALL DIVISORS WITHOUT THE '
              f'NUMBER ITSELF IS, {factor_string} WHICH IS < {number}')
    elif flag == 2:
        print(f'THE NUMBER {number} IS AN ABUNDANT NUMBER. BECAUSE SUM OF ITS ALL PROPER DIVISORS WITHOUT THE NUMBER '
              f'ITSELF IS, {factor_string} WHICH IS > {number}')

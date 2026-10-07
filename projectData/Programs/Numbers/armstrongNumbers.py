"""THIS PROGRAM DEMONSTRATE ARMSTRONG NUMBERS"""
from projectData.SupportScripts.Numbers.armstrongNumbers_SF import *


def main():
    armObj = ArmstrongNumbers()
    armObj.load_armstrong()
    while True:
        colorPrint('\n-----------------------------------: WELCOME TO THE LAND OF ARMSTRONG NUMBERS'
                   ' :-----------------------------------\n', 'Orange')
        print(
            'PRESS 1. TO CHECK THAT WHETHER GIVEN NUMBER IS ARMSTRONG OR NOT.\nPRESS 2. TO GENERATE FIRST N ARMSTRONG '
            'NUMBER.\nPRESS 3. TO GENERATE THE ARMSTRONG NUMBERS BETWEEN TWO NUMBERS.\nPRESS 4. TO '
            'GENERATE n ARMSTRONG NUMBERS WHICH ARE GREATER THEN CERTAIN NUMBER.\nPRESS 5. TO '
            'GENERATE n ARMSTRONG NUMBERS WHICH ARE LESS THEN A CERTAIN NUMBER.\nPRESS 9. TO SEE STATUS ABOUT '
            'PRECOMPUTED ARMSTRONG NUMBERS.\nPRESS 0.TO GO BACK ')
        choice = valInput('\nENTER YOUR CHOICE HERE :  ',
                          'ENTER ONLY A NUMBER ... !', 0)
        if choice == 1:
            number = valInput('PLEASE ENTER NUMBER : ', 'INVALID INPUT,PLEASE ENTER A WHOLE NUMBER')
            if armObj.is_armstrong(number):
                print(f'{number} IS AN ARMSTRONG NUMBER')
            else:
                print(f'{number} IS NOT AN ARMSTRONG NUMBER')
        elif choice == 2:
            number = valInput('ENTER A TOTAL NUMBER OF ARMSTRONG NUMBERS THAT YOU WANT TO GENERATE : ')
            colorPrint(f"FIRST {number} ARMSTRONG NUMBERS ARE : "
                       f"{', '.join(map(str, armObj.find_n_armstrong_number(number)))}", 'Saffron')
        elif choice == 3:
            start = valInput('ENTER A NUMBER STARTING FROM WHICH YOU WANT TO FIND ARMSTRONG NUMBERS : ')
            end = valInput('ENTER A NUMBER UPTO WHICH YOU WANT TO GENERATE ARMSTRONG NUMBERS : ')
            result = armObj.generate_armstrong_in_range(start, end)
            colorPrint(f"BETWEEN {start} AND {end},THERE ARE {str(len(result))} ARMSTRONG NUMBERS."
                       f"THEY ARE : {reset}{', '.join(map(str, result))}")
        elif choice == 4:
            benchmark = valInput('ENTER NUMBER AFTER WHICH YOU WANT TO GENERATE ARMSTRONG NUMBER : ')
            number = valInput('ENTER A NUMBER OF ARMSTRONG NUMBERS THAT YOU WANT TO GENERATE : ')
            result = armObj.find_n_armstrong_number(number=number, benchmark=benchmark)
            colorPrint(f"{len(result)} ARMSTRONG NUMBERS AFTER {benchmark} ARE : "
                       f"{', '.join(map(str, result))}",'Saffron')
        elif choice == 5:
            benchmark = valInput('ENTER NUMBER BEFORE WHICH YOU WANT TO GENERATE ARMSTRONG NUMBER : ')
            number = valInput('ENTER A NUMBER OF ARMSTRONG NUMBERS THAT YOU WANT TO GENERATE : ')
            result = armObj.find_n_armstrong_number(number=number, benchmark=benchmark,step=-1)
            colorPrint(f"{len(result)} ARMSTRONG NUMBERS BEFORE {benchmark} ARE : "
                       f"{', '.join(map(str, result))}",'Saffron')
        elif choice == 9:
            armObj.status()
        elif choice == 0:
            armObj.save_armstrong()
            colorPrint('THANK YOU FOR VISITING THIS PROGRAM,JAY SHREE RAM.\nHAVE A NICE DAY.\n', 'Orange')
            break
        else:
            print('PLEASE ENTER A VALID NUMBER FROM THE LIST ONLY ... !!!')

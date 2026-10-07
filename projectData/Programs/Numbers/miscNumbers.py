"""DEMONSTRATION OF FACTORIAL, PALINDROME, FIBONACCI, HARSHAD,TRIANGULAR NUMBER """
from projectData.SupportScripts.Numbers.miscNumbers_SF import *


def main():
    con = 'Y'
    while con.upper() == 'Y':
        colorPrint('\n------------------------------------------------- : WELCOME TO THE LAND OF VARIETY OF NUMBERS : '
                   '---------------------------------------------------\n', 'Orange')
        print('PRESS 1. FOR FACTORIAL.\nPRESS 2. FOR PALINDROME.\nPRESS 3. FOR HARSHAD NUMBER.\nPRESS 4. FOR '
              'TRIANGULAR NUMBER.\nPRESS 0. TO GO BACK.')
        choice = rangeInput(0, 5, '\nENTER YOUR CHOICE HERE : ')
        if choice == 1:
            number = int(valInput('ENTER NUMBER FOR WHICH YOU WANT TO FIND FACTORIAL : ', category=0))
            facto = factorial(number)
            print(f"FACTORIAL OF NUMBER '{number}' IS : {facto}")
        elif choice == 2:
            number = str(valInput('ENTER NUMBER TO CHECK WHETHER IT IS PALINDROME OR NOT : '))
            palindrome(number)
        elif choice == 3:
            pass
        elif choice == 4:
            number=valInput('')
        elif choice == 0:
            colorPrint('THANK YOU FOR VISITING THIS PROGRAM,HOPE YOU HAVE GREAT TIME WITH US.JAY SIYA RAM\n'
                       'HAVE A FABULOUS DAY AHEAD.', 'Magenta')
            break
        con = valInput('DO YOU WANT TO CONTINUE PRESS \'Y\' IF YES :', category=2)
        print(con)
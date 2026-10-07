""" PROGRAM TO DEMONSTRATE THE DESIGNING OF VARIOUS SHAPES WITH PATTERN"""

from projectData.SupportScripts.designPattern_SF import *
from projectData.Programs import _wordPattern as word


def main():
    pattern = '$#$'
    number_of_lines = 6
    while True:
        colorPrint('\n---------------------------------------------- : WELCOME TO THE WORLD OF DESIGN PATTERN :'
                   ' ----------------------------------------------\n', 'Orange')
        print('PRESS 1. TO GENERATE TRIANGLE PATTERN\nPRESS 2. TO GENERATE DIAMOND PATTERN.\nPRESS 3. TO GENERATED A '
              'WORD WITH A PATTERN')
        print(
            f'PRESS 8. TO CHANGE ELEMENT OF PATTERN.CURRENT ELEMENT : {pattern}\nPRESS 9. TO CHANGE NUMBER OF LINES '
            f'TO GENERATE,CURRENT NUMBER OF LINES IS {str(number_of_lines)}\nPRESS 0. TO GO BACK TO MAIN MENU.')
        choice = valInput('Enter Your Choice : ', 'Please Enter Number ... !!!', 0)
        if choice == 1:
            drawTriangle(pattern, number_of_lines)
        elif choice == 2:
            drawDiamond(pattern, number_of_lines)
        elif choice == 3:
            word.main()
        elif choice == 8:
            pattern = input('Enter The New Pattern : ')
        elif choice == 9:
            number_of_lines = valInput('Enter Number of Lines That you want to print : ', 'Please Enter a number', 0)
        elif choice == 0:
            colorPrint('THANK YOU FOR USING DESIGN PROGRAM,GOOD BYE,RADHE RADHE.', 'Magenta')
            break
        else:
            colorPrint('PLEASE CHOOSE THE NUMBER FROM THE LIST ONLY.', 2)

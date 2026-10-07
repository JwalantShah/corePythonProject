# from projectData.SupportScripts.wordPattern_SF import *
from projectData.SupportScripts.wordPatternSF1 import *


def main():
    while True:
        word = valInput('PLEASE ENTER A WORD FOR WHICH YOU WANT TO GENERATE PATTERN : ',
                        'KINDLY ENTER A WORD WITHOUT SPACE... !\n ', 2)
        pattern = valInput('\nENTER PATTERN WITH WHICH YOU WANT TO GENERATE WORD :  ', category=2)
        colorPrint2('\nHOW YOU WOULD WANT TO GENERATE THE PATTERN.\nPRESS 1. TO GENERATE FULL OR PARTIALLY '
                    'BROKEN PATTERN.\nPRESS 2. TO GENERATE BROKEN PATTERN.','Black','Bright White')
        broken = rangeInput(1, 2,
                            '\nENTER YOUR CHOICE HERE :   ')
        colorPrint2('\nBOLD OR NORMAL PATTERN.\nPRESS 1. FOR BOLD\nPRESS 2. FOR NORMAL ', 'Black',
                    'Bright White')
        bold = rangeInput(1, 2,
                          '\nENTER YOUR CHOICE HERE :   ')
        color = rangeInput(0, 13, 'ENTER COLOR : \n0. WHITE\t1. CYAN\t2. RED\t3. BLUE\t4. GREEN'
                                  '\t5. YELLOW\t6. Orange\t7. Pink\t8. Purple\t9. MAGENTA\n\t10. BLACK AND WHITE\t11. '
                                  'TRI-COLOR VERTICAL\t12. TRI-COLOR HORIZONTAL\nENTER YOUR CHOICE HERE : ')
        colorPrint2('\nSOLID OR HOLLOW PATTERN .\nPRESS 1. FOR SOLID\nPRESS 2. FOR HOLLOW ', 'Black',
                    'Bright White')
        is_solid = rangeInput(1,3,'\nENTER YOUR CHOICE HERE : ')
        if broken == 1:
            broken = False
        else:
            broken = True
        if bold == 1:
            bold = True
        else:
            bold = False
        word_pattern = createWord(word, pattern, broken, bold, is_solid)
        print_matrix(word_pattern, color,len(word.replace(' ','')))
        choice = valInput('Do You Want to Continue PRESS \'Y\' if yes.press any other key to exit.', category=2)
        if choice != 'Y':
            break

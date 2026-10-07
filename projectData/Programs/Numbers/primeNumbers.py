"""PROGRAM TO DEMONSTRATE PRIME NUMBERS"""

from projectData.SupportScripts.Numbers.primeNumbers_SF import *


def main():
    while True:
        colorPrint('\n--------------------------------------- : WELCOME TO THE LAND OF PRIME NUMBERS :'
                   ' ------------------------------------------\n', 'Orange')
        print('PRESS 1. TO CHECK WHETHER A NUMBER IS PRIME OR NOT.\nPRESS 2. TO GENERATE PRIME NUMBERS UPTO A NUMBER.\n'
              'PRESS 3. TO GENERATE THE PRIME NUMBERS BETWEEN TWO NUMBERS.\nPRESS 4.TO GENERATE A PRIME NUMBERS IN A'
              ' TEXT FILE,OUR AUTOMATED ALGORITHM WILL RUN FOR NUMBERS OF MINUTE YOU ENTERED\n\t AND GENERATE PRIME '
              'NUMBERS IN A TEXT FILE AS WELL AS KEEPS LOGS FOR ALL THE TIMES YOU GENERATE THE ALGORITHM.\nPRESS 5. TO'
              ' SEE LOG FILE IN ABOUT GENERATED PRIME NUMBERS IN A TEXT FILE.\nPRESS 8. TO CHANGE THE NUMBER OF '
              'ELEMENTS TO BE PRINTED IN A SINGLE LINE.THIS OPTION BECOMES VERY HANDY WHILE OPERATING WITH OPTION 2 '
              'AND 3.\nPRESS 9. FOR HELP REGARDING THE PROGRAMS.\nPRESS 0. TO GO BACK.')
        choice = valInput('ENTER YOUR CHOICE HERE : ', 'ENTER VALID CHOICE ...!')
        if choice == 1:
            number = valInput('ENTER A NUMBER TO CHECK WHETHER A NUMBER IS PRIME OR NOT : ',
                              'ENTER VALID NUMBER ...!')
            answer = isPrime(number)
            if answer[0]:
                print(f'{number} is a prime number.')
            else:
                print(f'{number} IS NOT A PRIME NUMBER AS IT IS DIVIDED BY {answer[1]}')
        elif choice == 2:
            prime_in_range(valInput('ENTER THE NUMBER UPTO WHICH YOU WANT TO GENERATE PRIME NUMBERS : '))
        elif choice == 3:
            prime_in_range(valInput('ENTER THE NUMBER UPTO WHICH YOU WANT TO GENERATE PRIME NUMBERS : '),
                           valInput('ENTER THE NUMBER FROM WHICH YOU WANT TO GENERATE PRIME NUMBERS : '))
        elif choice == 4:
            minute = valInput('ENTER NUMBER OF MINUTES UPTO WHICH YOU WANT TO GENERATE PRIME NUMBER :', category=3)
            generate_primes_for_duration(minute)
        elif choice == 5:
            generation_logs()
        elif choice == 8:
            change_number_of_element()
        elif choice == 9:
            pass
        elif choice == 0:
            break

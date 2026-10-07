"""PROGRAM TO DEMONSTRATE THE MULTIPLICATION OF TWO DYNAMICALLY GENERATED MATRIX"""
from projectData.SupportScripts.matrixMultiPlication_SF import *


def main():
    while True:
        # Display main menu
        colorPrint('\n--------------------------------- : WELCOME TO THE WORLD OF MATRIX MULTIPLICATION : '
                   '------- -----------------------------\n','Orange')
        print('PRESS 1. TO MULTIPLY MATRICES\nPRESS 9. TO GET DETAILED INSIGHT OF PROGRAM.\nPRESS 0. TO GO BACK TO '
              'MAIN MENU.')

        # Take user choice and validate input
        choice = valInput('ENTER YOUR CHOICE HERE : ', 'PLEASE ENTER VALID NUMBER ONLY. ', 0)

        # If user chooses matrix multiplication
        if choice == 1:
            while True:
                # Take matrix dimensions with validation
                row1 = valInput('ENTER NUMBER OF ROWS FOR MATRIX 1 : ', 'ENTER NUMBER ONLY', 0)
                col1 = valInput('ENTER NUMBER OF COLUMNS FOR MATRIX 1 : ', 'ENTER NUMBER ONLY', 0)
                row2 = valInput('ENTER NUMBER OF ROWS FOR MATRIX 2 : ', 'ENTER NUMBER ONLY', 0)
                col2 = valInput('ENTER NUMBER OF COLUMNS FOR MATRIX 1 : ', 'ENTER NUMBER ONLY', 0)

                # Validate that matrix multiplication is possible (columns of matrix 1 == rows of matrix 2)
                if col1 != row2:
                    print('WE ARE SORRY WE CAN NOT PERFORM MATRIX MULTIPLICATION,\n'
                          'BECAUSE TO PERFORM MATRIX MULTIPLICATION COLUMN OF MATRIX 1 '
                          'AND ROWS OF MATRIX 2 MUST BE SAME IN NUMBER.')
                else:
                    # Create matrices by taking element inputs from the user
                    print('\n\t--------- ENTER ELEMENT OF MATRIX 1 ----------')
                    matrix1 = create_matrix(row1, col1)
                    print('\n\t--------- ENTER ELEMENT OF MATRIX 2 ----------')
                    matrix2 = create_matrix(row2, col2)

                    # Perform matrix multiplication and display step-by-step results
                    matrix_multiplication(matrix1, matrix2)

                # Ask user if they want to continue
                con = input('PRESS \'Y\' TO CONTINUE PRESS ANY KEY TO GO BACK.')
                if con == 'Y':
                    continue
                else:
                    break

        # Handle other choices
        elif choice == 9:
            # Could be extended for program insights or help section
            pass
        elif choice == 0:
            colorPrint('THANK YOU FOR USING OUR PROGRAM ON MATRIX MULTIPLICATION, HAR HAR MAHADEV','Red')
            break
        else:
            # Handle invalid menu choices
            print('PLEASE ENTER VALID NUMBERS AVAILABLE IN THE MENU.')

from projectData.SupportScripts.globalUDFs import *

# Function to create a matrix based on user input
def create_matrix(rows, cols):
    matrix = []  # Initialize an empty matrix
    for i in range(rows):
        sub_matrix = []  # Create a row for matrix
        for j in range(cols):
            # Get input for each element of the matrix with validation
            sub_matrix.append(valInput(f'ENTER VALUE FOR ROW {str(i + 1)} COLUMN {str(j + 1)} : ',
                                       'PLEASE ENTER NUMBER ONLY', 0))
        matrix.append(sub_matrix)  # Add row to matrix
    display_matrix(matrix)  # Display the matrix after creation
    return matrix

# Function to simulate step 1 of matrix multiplication (expressions)
def step1(matrix1, matrix2):
    row1, row2, col1, col2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])
    temp_matrix = []
    colorPrint('\n--------------------------- :  Step1 : ----------------------------------\n','Yellow')

    # Build the expression for each element in the resulting matrix
    for i in range(row1):
        temp_sub_matrix = []
        for j in range(col2):
            simplify = '['  # Start of expression
            for k in range(col1):
                simplify += f'({str(matrix1[i][k])} X {str(matrix2[k][j])}) + '
            simplify = simplify[:-3] + ']'  # Remove last '+' and close bracket
            temp_sub_matrix.append(simplify)  # Add to sub-matrix
        temp_matrix.append(temp_sub_matrix)  # Add row to temp matrix
    return temp_matrix

# Function to simulate step 2 (show partially computed products)
def step2(matrix1, matrix2):
    row1, row2, col1, col2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])
    temp_matrix = []
    colorPrint('\n------------------------------- : Step2 : -------------------------------------\n','Orange')

    # Perform multiplication, but keep addition as part of the output string
    for i in range(row1):
        temp_sub_matrix = []
        for j in range(col2):
            simplify = '['
            for k in range(col1):
                simplify += f'{str(matrix1[i][k] * matrix2[k][j])} + '
            simplify = simplify[:-3] + ']'  # Remove last '+' and close bracket
            temp_sub_matrix.append(simplify)
        temp_matrix.append(temp_sub_matrix)
    return temp_matrix

# Function to compute the final result of the matrix multiplication
def step3(matrix1, matrix2):
    row1, row2, col1, col2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])
    temp_matrix = []
    colorPrint('\n------------------------------------------- : Final Result : ------------------------------ \n',
              'Green')

    # Perform the actual multiplication and summing for the final matrix
    for i in range(row1):
        temp_sub_matrix = []
        for j in range(col2):
            simplify = 0  # Initialize result for each element
            for k in range(col1):
                simplify += matrix1[i][k] * matrix2[k][j]  # Multiply and accumulate
            temp_sub_matrix.append(simplify)
        temp_matrix.append(temp_sub_matrix)
    return temp_matrix

# Utility function to display any matrix
def display_matrix(matrix):
    for i in range(len(matrix)):
        print('| ', end=' ')
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]), end=' ')  # Print each element in the row
        print('|')  # Close row display with a vertical bar

# Main function to run the matrix multiplication process
def matrix_multiplication(matrix1, matrix2):
    display_matrix(step1(matrix1, matrix2))  # Display expression form (Step 1)
    display_matrix(step2(matrix1, matrix2))  # Display intermediate results (Step 2)
    display_matrix(step3(matrix1, matrix2))  # Display the final result (Step 3)

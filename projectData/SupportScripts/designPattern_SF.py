from projectData.SupportScripts.globalUDFs import *


def trianglePattern1(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(i):
            print(pattern, end=ws)
        print()


def trianglePattern2(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(number_of_lines, 0, -1):
        for j in range(i):
            print(pattern, end=ws)
        print()


def trianglePattern3(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(number_of_lines - i):
            print(ws, end=ws)
        for j in range(i):
            print(pattern, end=ws)
        print()


def trianglePattern4(pattern, number_of_lines):
    ws = ' ' * len(pattern)
    for i in range(number_of_lines, 0, -1):
        for j in range(number_of_lines - i):
            print(ws, end=ws)
        for j in range(i, 0, -1):
            print(pattern, end=ws)
        print()


def trianglePattern5(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(i, number_of_lines):
            print(ws, end='')
        for j in range(i):
            print(pattern, end=ws)
        print()


def trianglePattern6(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(0, number_of_lines):
        for j in range(i):
            print(ws, end='')
        for j in range(number_of_lines - i, 0, -1):
            print(pattern, end=ws)
        print()


def diamondPattern1(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(i, number_of_lines):
            print(ws, end='')
        for j in range(i):
            print(pattern, end=ws)
        print()
    for i in range(number_of_lines - 1, 0, -1):
        for j in range(number_of_lines - i):
            print(ws, end='')
        for j in range(i):
            print(pattern, end=ws)
        print()


def diamondPattern2(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(i, number_of_lines):
            print(pattern, end='')
        print(ws * ((i - 1) + i), end='')
        for j in range(i, number_of_lines):
            print(pattern, end='')
        print()
    for i in range(number_of_lines - 1, 0, -1):
        for j in range(number_of_lines - i):
            print(pattern, end='')
        print(ws * ((i - 1) + i), end='')
        for j in range(number_of_lines - i):
            print(pattern, end='')
        print()


def drawTriangle(pattern, number_of_lines):
    while True:
        print('WE OFFER SIX DIFFERENT PATTERN FOR TRIANGLE.'
              'ENTER ANY NUMBER FROM 1 TO 6 TO GENERATE PATTERN.\nPRESS 0 TO GO BACK\n')
        pt_no = valInput('ENTER YOUR CHOICE : ',
                         'ENTER NUMBER ONLY ... !!', 0)
        if pt_no == 0:
            break

        elif pt_no in range(1, 7):
            fun = 'trianglePattern' + str(pt_no)
            globals()[fun](pattern, number_of_lines)


def drawDiamond(pattern, number_of_lines):
    while True:
        print('UNFORTUNATELY WE ONLY HAVE 2 PATTERN AVAILABLE.PRESS 1 OR TO GENERATE PATTERN'
              '\n PRESS 0. TO GO BACK.')
        pt_no = valInput(
            'ENTER YOUR CHOICE : ',
            'Please Enter Only Number ... !', 0)
        if pt_no == 0:
            break
        elif pt_no in [1, 2]:
            fun = 'diamondPattern' + str(pt_no)
            globals()[fun](pattern, number_of_lines)

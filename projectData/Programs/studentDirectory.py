"""PROGRAM TO DEMONSTRATE CRUD OPERATION ON TEXT FILE.USING STUDENT DATA IN DICTIONARY"""
from projectData.SupportScripts.studentDirectory_SF import *


def main():
    load_student()
    while True:
        colorPrint('\n--------------------------------: WELCOME TO THE WORLD OF STUDENT DATABASE SYSTEM '
                   ':-------------------------------------------- \n','Orange')
        print('1. ADD NEW STUDENT.\n2. UPDATE STUDENT.\n3. DELETE STUDENT.\n4. SHOW STUDENT LIST.\n0. SAVE AND EXIT '
              'TO MAIN MENU')
        ch = rangeInput(0, 4, '\nENTER YOUR CHOICE HERE : ', 'ENTER VALID CHOICES ONLY ', 1)
        if ch == 1:
            addNewStudent()
        elif ch == 2:
            con = True
            while con:
                print('\n1. UPDATE NAME\n2. UPDATE MARKS.\n0. TO CANCEL UPDATE OPERATION')
                ch = valInput('ENTER YOUR CHOICE HERE : ',
                              'ENTER VALID CHOICE ... !!!', 0)
                if ch == 1:
                    con = updateStudentName()
                elif ch == 2:
                    con = updateMarks()
                elif ch == 0:
                    colorPrint('EXITED FROM UPDATE OPERATION', 'Red')
                    break

        elif ch == 3:
            deleteStudent()
        elif ch == 4:
            showStudents()
        elif ch == 0:
            saveData()
            colorPrint('THANK YOU FOR USING OUR PROGRAM ON CRUD OPERATION ON FILE USING DICTIONARY,JAY JAY SHREE '
                       'RADHE.\nHAVE A GREAT DAY', 'Magenta')
            break

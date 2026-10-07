import os
import pickle

from prettytable import PrettyTable
from projectData.SupportScripts.globalUDFs import *

path = ['projectData/Data/StudentData/', '../Data/StudentData/']

studentData = {}


def load_student():
    global studentData
    if os.path.exists(path[0] + 'StudentData.pkl'):
        with open(path[0] + 'StudentData.pkl', 'rb') as file:
            studentData = pickle.load(file)


def addNewStudent():
    no_student = valInput('Enter number of Student', 'Please enter valid Integer', 0)
    for i in range(no_student):
        while True:
            roll_no = input(f'Enter Roll Number for student {str(i + 1)} : ')
            if roll_no == '0':
                break
            if re.search('^[0-9]{2}[A-Z]{3}[0-9]{3}$', roll_no) is None:
                print('please enter roll number in a valid format for example 09DCE212,13BCE171')
                continue
            if roll_no in studentData.keys():
                print('Roll number Already present in the Database.Please Enter different Roll Number')
                continue
            break
        name = valInput(f'Enter Name of Student {str(i + 1)} : ', 'Enter Name without any space ', 1)
        marks = []
        for j in range(1, 4):
            while True:
                mark = valInput(f'Enter marks of subject {j} of Student {i + 1} :',
                                'Enter valid marks in integer or float number', 3)
                if mark > 100 or mark < 0:
                    print('Please Enter Marks in range of 0 to 100.')
                    continue
                break
            marks.append(mark)
        studentData.update({roll_no: {'name': name, 'marks': marks}})



def addMarksToTxt():
    with open(path[0] + 'studentMarks.txt', 'w+') as file:
        for i in studentData.keys():
            marks = '-'.join([str(j) for j in studentData.get(i).get('marks')])
            file.write(i + ' : ' + marks + '\n')
        file.close()


def addStudentInfo():
    with open('studentInfo.txt', 'w+') as file:
        for i in sorted(studentData.keys()):
            file.write(i + ' : ' + studentData[i]['name'] + '\n')
        file.close()


def addGrade():
    srt = sorted(studentData.items(), key=lambda x: sum(x[1]['marks']), reverse=True)
    with open(path[0] + 'AGrade.txt', 'w+') as file1, open(path[0] + 'BGrade.txt',
                                                           'w+') as file2, open(
        path[0] + 'CGrade.txt', 'w+') as file3:
        for i in srt:
            avg = round(sum(i[1]['marks']) / 3, 2)
            if avg >= 80 and avg <= 100:
                file1.write(i[0] + '-' + i[1]['name'] + '-' + str(avg) + '\n')
            elif avg >= 60 and avg < 80:
                file2.write(i[0] + '-' + i[1]['name'] + '-' + str(avg) + '\n')
            elif avg >= 40 and avg < 60:
                file3.write(i[0] + '-' + i[1]['name'] + '-' + str(avg) + '\n')


def updateStudentName():
    while True:
        rollNo = input('ENTER ROLL NUMBER OF A STUDENT : ')
        if rollNo == 0: break
        if re.search('^[0-9]{2}[A-Z]{3}[0-9]{3,}$', rollNo) is None:
            colorPrint('PLEASE ENTER ROLL NO IN VALID FORMAT LIKE 09DCE212,13BCE171', 'Red')
            continue
        if rollNo in studentData.keys():
            name = valInput(f'Enter The updated Name for {rollNo} : ', 'Kindly enter only characters ', 1)
            studentData[rollNo]['name'] = name
            saveData()
            colorPrint(f'SUCCESSFULLY UPDATED NAME TO {name} FOR ROLL NO. {rollNo}', 'Green')
            return False
        else:
            colorPrint('ROLL NUMBER NOT PRESENT IN DATABASE', 'Yellow')


def updateMarks():
    while True:
        rollNo = input('ENTER ROLL NUMBER OF A STUDENT : ')
        if rollNo == 0: break
        if re.search('^[0-9]{2}[A-Z]{3}[0-9]{3,}$', rollNo) is None:
            colorPrint('PLEASE ENTER ROLL NO IN VALID FORMAT LIKE 09DCE212,13BCE171', 'Red')
            continue
        if rollNo in studentData.keys():
            oldMarks = '-'.join([str(j) for j in studentData.get(rollNo).get('marks')])
            colorPrint(f'Current Marks for {rollNo} is {oldMarks} \n Enter Updated Marks\n','Green')
            marks = []
            for j in range(1, 4):
                mark = rangeInput(0, 100, f'Enter marks of subject {j}  :',
                                  'ENTER VALID MARKS IN INTEGER OR DECIMAL NUMBER ... !', 3)
                marks.append(mark)
            studentData[rollNo]['marks'] = marks
            colorPrint(f'SUCCESSFULLY UPDATED THE MARKS OF ROLL NO. {rollNo}.', 'Green')
            return False


def deleteStudent():
    while True:
        rollNo = input('ENTER THE ROLL NO OF STUDENT FOR WHOM YOU WANT TO DELETE DATA.')
        if rollNo == '0':
            print('DELETE OPERATION CANCELED . \n')
            break
        if re.search('^[0-9]{2}[A-Z]{3}[0-9]{3}$', rollNo) is None or rollNo not in studentData.keys():
            print('ROLL NUMBER IS INVALID OR NOT PRESENT IN DATABASE\nTO QUIT OPERATION ENTER 0 \n.')
        else:
            del studentData[rollNo]
            colorPrint(f'STUDENT DATA OF ROLL NO. {rollNo} DELETED SUCCESSFULLY ...! ','Green')
            break


def saveData():
    with open(path[0] + 'StudentData.pkl', 'wb') as file:
        pickle.dump(studentData, file)
    addMarksToTxt()
    addGrade()
    addStudentInfo()

def showStudents():
    table = PrettyTable()
    table.field_names = ['SR. NO', 'ROLL NUMBER', 'NAME', 'MARKS']
    data = [[i, j[0], j[1]['name'], '-'.join([str(k) for k in j[1]['marks']])] for i, j in
            enumerate(studentData.items(), start=1)]

    for row in data:
        table.add_row(row=row)
    print(font_color.get('Green') + '\n')
    print(table)
    print('\n' + reset)
    # print('SR.NO.\t| ROLL NUMBER \t\t| NAME\t\t\t\t| MARKS')
    # for i, j in enumerate(studentData.items(), start=1):
    #     name = j[1]['name']
    #     marks = '-'.join([str(k) for k in j[1]['marks']])
    #     print(f' {i}\t\t\t {j[0]}\t\t {name}\t\t\t {marks}')

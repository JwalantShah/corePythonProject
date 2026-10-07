"""PROGRAM TO DEMONSTRATE VARIOUS NUMBERS LIKE PRIME,ARMSTRONG,PALINDROME NUMBERS"""
import os, importlib, inspect
from projectData.SupportScripts.globalUDFs import *
from time import sleep


def main():
    programs_list = os.listdir('projectData/Programs/Numbers/')
    programs_list = [p.replace('.py', '') for p in programs_list if (p.endswith('.py') and not p.startswith('_'))]
    loaded_scripts = {}

    while True:
        colorPrint('\n----------------------------- : WELCOME TO THE WORLD OF NUMBERS : -----------------------\n',
                   'Orange')
        for i, j in enumerate(programs_list, start=1):
            script_name = 'projectData.Programs.Numbers.' + j

            if script_name not in loaded_scripts:
                try:
                    script = importlib.import_module(script_name)
                    script_doc = inspect.getdoc(script)
                    loaded_scripts[script_name] = {'script': script, 'script_doc': script_doc}
                except ModuleNotFoundError:
                    script_doc = 'Module Not Found ... !'
            else:
                script_doc = loaded_scripts[script_name]['script_doc']
            print(f'PRESS {i}. {script_doc}')
        print('PRESS 0. TO GO TO MAIN MENU')
        choice = valInput('ENTER YOUR CHOICE : ', 'PLEASE ENTER NUMBER ONLY AS CHOICE ..!!', 0)
        if choice in range(1, len(programs_list) + 1):
            script_name = programs_list[choice - 1]
            script = loaded_scripts['projectData.Programs.Numbers.' + script_name]['script']
            script.main()
        elif choice == 0:
            colorPrint('THANK YOU FOR USING OUR NUMBERS PROGRAM.JAY MATAJI.\nHAVE A FABULOUS DAY. ','Red')
            break
        else:
            colorPrint('KINDLY ENTER A NUMBER FROM THE LIST. ', 'Yellow')
            sleep(3)

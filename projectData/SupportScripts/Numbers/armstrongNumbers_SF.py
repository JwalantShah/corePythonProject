from projectData.SupportScripts.globalUDFs import *
from functools import lru_cache
import os
import pickle

path = 'projectData/Data/Numbers/'


class ArmstrongNumbers:
    def __init__(self):
        self.armstrong_list = [0]
        self.last_number_checked = 0
        self.load_armstrong()
        self.miscNumbers = {}

    def load_armstrong(self):
        """Loads the precomputed Armstrong numbers from a file."""
        if os.path.exists(path + 'armstrongList.pkl'):
            with open(path + 'armstrongList.pkl', 'rb') as file:
                self.armstrong_list = pickle.load(file)
        if os.path.exists(path + 'miscNumbers.pkl'):
            with open(path + 'miscNumbers.pkl', 'rb') as file:
                self.miscNumbers = pickle.load(file)
                self.last_number_checked = self.miscNumbers.get('last_armstrong_number_checked')

    def save_armstrong(self):
        """Saves the current Armstrong list to a file."""
        with open(path + 'armstrongList.pkl', 'wb') as file:
            pickle.dump(self.armstrong_list, file)
        with open(path + 'miscNumbers.pkl', 'wb') as file:
            self.miscNumbers.update({'last_armstrong_number_checked': self.last_number_checked})
            pickle.dump(self.miscNumbers, file)

    @staticmethod
    @lru_cache(maxsize=1000)
    def is_armstrong(number):
        """Checks if a number is an Armstrong number."""
        if number < 0:
            return False
        digits = [int(i) for i in str(number)]
        power = len(digits)
        return number == sum(digit ** power for digit in digits)

    def generate_armstrong(self, n=1000000):
        """Generates the next `n` Armstrong numbers."""
        last_element = self.last_number_checked
        colorPrint(f'CHECKING NEXT {str(n)} NUMBERS AFTER {last_element} ')
        for i in range(last_element + 1, last_element + n + 1):
            if self.is_armstrong(i):
                self.armstrong_list.append(i)
            last_element = i
        self.last_number_checked = last_element

    def find_n_armstrong_number(self, number, benchmark=0, step=1):
        """Finds the next or previous `number` Armstrong numbers around a benchmark."""
        # Ensure the list covers the benchmark

        while benchmark > self.last_number_checked:
            self.generate_armstrong()


        # Find the position of the first number >= benchmark
        position = next((i for i, element in enumerate(self.armstrong_list) if element >= benchmark), -1)
        if position == -1:
            if step == 1:
                con = input(f"{font_color.get('Red')}PROCESS OF GENERATING ARMSTRONG NUMBERS MIGHT TAKE HOURS OR DAYS "
                            f"TO COMPLETE.\nDO YOU WANT TO CONTINUE ?"
                            f"\nPRESS Y IF YES ELSE PRESS ANY OTHER KEY TO EXIT : {reset}")
                if con.upper() != 'Y':
                    return []
            else:
                return self.armstrong_list[-1:-(number+1):-1]
            # raise ValueError("Benchmark is higher than the highest precomputed Armstrong number.")

        if step == 1:  # Forward direction
            while position + number > len(self.armstrong_list):
                self.generate_armstrong()
            return self.armstrong_list[position:position + number]

        elif step == -1:  # Backward direction
            if position - number < 0:
                return self.armstrong_list[position:0:-1]
                # raise ValueError("Not enough numbers before the benchmark.")
            return self.armstrong_list[max(0, position - number):position][::-1]

    def generate_armstrong_in_range(self, start, end):
        """Generates Armstrong numbers within a specified range."""
        # Ensure the list covers the end value
        while end > self.last_number_checked:
            self.generate_armstrong()
        return [num for num in self.armstrong_list if start <= num < end]

    def status(self):
        colorPrint2(f'\n\n TOTAL ARMSTRONG NUMBER GENERATED : {str(len(self.armstrong_list))}'
                    f'\n LAST NUMBERS CHECKED FOR ARMSTRONG: {str(self.last_number_checked)}'
                    f"\n GENERATED ARMSTRONG NUMBERS TILL DATE BY US : {', '.join(map(str, self.armstrong_list))}\n",
                    'Black', 'Bright White')

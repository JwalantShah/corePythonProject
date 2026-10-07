import os, pickle
from projectData.SupportScripts.globalUDFs import *


class FibonacciManager:
    def __init__(self, path):
        self.path = path
        self.fibonacci_list = []
        self.load_fibonacci()

    def load_fibonacci(self):
        if os.path.exists(self.path + 'fibonacciList.pkl'):
            with open(self.path + 'fibonacciList.pkl', 'rb') as file:
                self.fibonacci_list = pickle.load(file)
        else:
            self.fibonacci_list = [0, 1]


    def save_fibonacci(self):
        with open(self.path + 'fibonacciList.pkl', 'wb') as file:
            pickle.dump(self.fibonacci_list, file)

    def generate_fibonacci(self, n):
        i = len(self.fibonacci_list)
        while len(self.fibonacci_list) < n:
            self.fibonacci_list.append(
                self.fibonacci_list[-1] + self.fibonacci_list[-2]
            )

    def get_fibonacci_at_nth_position(self, position):
        if position - 1 < len(self.fibonacci_list):
            return self.fibonacci_list[position - 1]
        else:
            self.generate_fibonacci(position)
            return self.get_fibonacci_at_nth_position(position)

    def is_fibonacci(self, number):
        last_element = self.fibonacci_list[-1]
        if number < last_element:
            if number in self.fibonacci_list:
                return True, self.fibonacci_list.index(number) + 1
            else:
                return False, 0
        else:
            self.generate_fibonacci(100)
            return self.is_fibonacci(number)

    def get_n_fibonacci(self, n):
        if n > len(self.fibonacci_list):
            self.generate_fibonacci(n)
        return self.fibonacci_list[:n]

    def find_fibonacci_in_range(self, lower, upper):
        # Ensure the list is large enough to cover the range
        while self.fibonacci_list[-1] < upper:
            self.generate_fibonacci(len(self.fibonacci_list) + 100)

        # Filter Fibonacci numbers within the range
        return [num for num in self.fibonacci_list if lower <= num < upper]

    def find_fibonacci_before_or_after(self, benchmark, number_to_find, step):
        # Ensure the Fibonacci list contains sufficient numbers
        while benchmark > self.fibonacci_list[-1]:
            self.generate_fibonacci(len(self.fibonacci_list) * 2)

        # Find the position of the first element >= benchmark
        position = next((i for i, element in enumerate(self.fibonacci_list) if element >= benchmark), None)

        # If position not found, extend the sequence and retry
        if position is None:
            self.generate_fibonacci(len(self.fibonacci_list) * 2)
            return self.find_fibonacci_before_or_after(benchmark, number_to_find, step)
        result=[]
        # Determine the slice range
        if step == 1:  # Numbers after the benchmark
            end_position = position + number_to_find
            if end_position > len(self.fibonacci_list):
                self.generate_fibonacci(end_position - len(self.fibonacci_list))
            result= self.fibonacci_list[position:end_position]

        elif step == -1:  # Numbers before the benchmark
            start_position = max(0, position - number_to_find)
            result = self.fibonacci_list[start_position:position][::-1]
        text = 'AFTER' if step == 1 else 'BEFORE'
        colorPrint(f"{len(result)} FIBONACCI NUMBERS {text} {benchmark} ARE : "
                   f"{' , '.join(map(str,result))}")

        # If invalid step value, return empty list or raise an error
        # raise ValueError("Step must be either 1 (after) or -1 (before).")

    def take_input_benchmark(self, text):
        benchmark = rangeInput(0, 0, f"ENTER NUMBER {text} WHICH YOU TO FIND FIBONACCI NUMBER : ",
                               'ENTER ANY NON NEGATIVE INTEGER', category=5)
        return benchmark

    def take_input_n(self):
        number_to_generate = rangeInput(1, 0, 'ENTER TOTAL NUMBERS THAT YOU WANT TO FIND : ',
                                        'ENTER ANY NON-NEGATIVE INTEGER : ', 5)
        return number_to_generate

    def status(self):
        print(f'\t\t\tTOTAL FIBONACCI NUMBER GENERATED : {str(len(self.fibonacci_list))}\n'
              f'\t\t\tLAST FIBONACCI  NUMBER IN RECORD : {str(self.fibonacci_list[-1])}')

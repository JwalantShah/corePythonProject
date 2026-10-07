"""This is test PROGRAM JUST TO EXCUTE SEPRATE FUNCTION TO AVOID PROBLEM WHILE EXECUTING THE PROGRAM AS A WHOLE."""
import re
from collections import namedtuple,Counter

from projectData.SupportScripts.globalUDFs import *

# Standard and extended ANSI color codes for foreground colors
colors = {
    "Black": "\033[30m",
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Magenta": "\033[35m",
    "Cyan": "\033[36m",
    "White": "\033[37m",
    "Bright Black": "\033[90m",
    "Bright Red": "\033[91m",
    "Bright Green": "\033[92m",
    "Bright Yellow": "\033[93m",
    "Bright Blue": "\033[94m",
    "Bright Magenta": "\033[95m",
    "Bright Cyan": "\033[96m",
    "Bright White": "\033[97m",
    "Orange": "\033[38;5;208m",
    "Pink": "\033[38;5;213m",
    "Purple": "\033[38;5;129m",
}

# Extended ANSI color codes for background colors
backgrounds = {
    "Black Background": "\033[40m",
    "Red Background": "\033[41m",
    "Green Background": "\033[42m",
    "Yellow Background": "\033[43m",
    "Blue Background": "\033[44m",
    "Magenta Background": "\033[45m",
    "Cyan Background": "\033[46m",
    "White Background": "\033[47m",
    "Bright Black Background": "\033[100m",
    "Bright Red Background": "\033[101m",
    "Bright Green Background": "\033[102m",
    "Bright Yellow Background": "\033[103m",
    "Bright Blue Background": "\033[104m",
    "Bright Magenta Background": "\033[105m",
    "Bright Cyan Background": "\033[106m",
    "Bright White Background": "\033[107m",
    "Orange Background": "\033[48;5;208m",
    "Pink Background": "\033[48;5;213m",
    "Purple Background": "\033[48;5;129m",
}

# Reset color code
reset = "\033[0m"


def zigzagPattern(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(1, number_of_lines + 1):
        for j in range(i):
            print(pattern, end=ws)
        print()
    for i in range(number_of_lines - 1, 0, -1):
        for j in range(i):
            print(pattern, end=ws)
        print()


# Display foreground colors
def invertedRightAngledTriangle(pattern, number_of_lines):
    ws = len(pattern) * ' '
    for i in range(number_of_lines, 0, -1):
        for j in range(number_of_lines - i):
            print(ws, end='')
        for j in range(i):
            print(pattern, end=ws)
        print()


def hourglassPattern(pattern, number_of_lines):
    ws = len(pattern) * ' '

    # Top part of the hourglass
    for i in range(number_of_lines, 0, -1):
        print(ws * (number_of_lines - i), end='')  # Print leading spaces
        for j in range(2 * i - 1):
            print(pattern, end=ws)
        print()

    # Bottom part of the hourglass
    for i in range(2, number_of_lines + 1):
        print(ws * (number_of_lines - i), end='')  # Print leading spaces
        for j in range(2 * i - 1):
            print(pattern, end=ws)
        print()


def main():
    # # Example list
    # my_list = ['a', 'b', 'c', 'd', 'e']
    #
    # # Enumerate with negative indices
    # for index, value in enumerate(my_list[::-1], start=-(len(my_list))):
    #     print(index, value)
    #
    # num = valInput('Enter any number')
    # print(f"is {num} Armstrong Number ? ", num == sum(map(lambda x: x ** len(str(num)), map(int, list(str(num))))))
    #
    # s = 'Jwalant Shah'
    # print([char for word in s.split(' ') for char in word])
    #
    # nested_list = [[1, 2], [3, 4], [5, 6]]
    # print([element for ls in nested_list for element in ls])
    # s = 'apple banana grape'
    # print(list(set(s.split()[0]).intersection(*[set(word) for word in s.split()[1:]])))
    #
    # print([(x, y, x * y) for x in range(1, 6) for y in range(1, 6)])
    #
    # nums = [5, 10, 15, 20, 25, 30]
    # print([x * x for x in nums if x % 5 == 0])
    #
    # m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(sorted(
    #     list(set([m[x][x] for x in range(len(m))] + [m[x][y] for x, y in enumerate(range(len(m) - 1, -1, -1))]))))
    # a= b"jwalant"
    # b = bytearray(a)
    # print(b)
    # b[0] = 74
    # b[3] = 11
    # print(b)
    #
    # ba = bytearray([0,])  # Mutable version of 'ABC'
    # print(ba)  # bytearray(b'ABC')
    # ba[0] = 75  # Change 'A' to 'a' (ASCII 97)
    # print(ba)  # bytearray(b'aBC')
    #
    # for i in range(256):  # ASCII range: 0-127
    #     ba[0]=i
    #     print(f"{i}: {ba} : {chr(i)}")
    data = bytearray(b"jwalant shah")
    view = memoryview(data)

    # Slice without copying
    slice_view = view[7:12]
    print(slice_view.tobytes())
    # Output: b'World'

    # Modify via the view
    slice_view[0] = ord('w')
    print(data)  # Output: bytearray(b'Hello, world!')

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)  # Output: 1 2

    print(type(p))

    cnt=Counter('Hi My Name is Shah. '
                'Hi Jwalant Shah'.replace('.','').split())
    print(cnt.get('Shah'))

    def generate_numbers():
        for i in range(5):
            yield i*i

    p = generate_numbers()
    print(p.__next__())
    print(next(p))
    print(next(p))
    print(next(p))
    print(p)
    from itertools import combinations
    items = ['a', 'b', 'c','d','e']
    for combo in combinations(items, 3):
        print(combo)

    import threading
    import time

    def download_file(file_name):
        print(f"Starting download: {file_name}")
        time.sleep(2)  # Simulate download
        print(f"Finished download: {file_name}")

    files = ["file1.txt", "file2.txt", "file3.txt"]

    threads = []
    for file in files:
        t = threading.Thread(target=download_file, args=(file,))
        threads.append(t)
        t.start()

    for _ in range(3):
        threads[_].join()

    print("All files downloaded!")


# Output: 0, 1, 2, 3, 4

    # h,ourglassPattern('#@#',7)5

    # perfect_numbers = find_perfect_numbers(10)
    # print(perfect_numbers)

    # print("Foreground Colors:")
    # for color_name, color_code in colors.items():
    #     print(f"{color_code}{color_name}{reset}")
    #
    # # Display background colors
    # print("\nBackground Colors:")
    # for bg_name, bg_code in backgrounds.items():
    #     print(f"{bg_code}{bg_name}{reset}")
    #
    # # Display combinations of foreground and background colors
    # print("\nForeground with Background Combinations:")
    # for color_name, color_code in colors.items():
    #     for bg_name, bg_code in backgrounds.items():
    #         print(f"{color_code}{bg_code}{color_name} on {bg_name}{reset}")
    #
    # print('testFile Executed')
    # rangeInput(0.5,5.5,'Please enter into ',category=3)
    # print(isinstance(5.0,int))
    # no = input('Enter Input : ')
    # no = no.replace('-', '')
    # no = no.replace('+', '')
    # number = '0'
    # for i in no:
    #     if i.isnumeric():
    #         number += i
    #     else:
    #         break
    # print('NUMBER IS : ', str(int(number)))


# 3
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_perfect_numbers(limit):
    """Find the first 'limit' perfect numbers using Mersenne primes."""
    count = 0
    p = 2
    perfect_numbers = []

    while count < limit:
        # Check if 2^p - 1 is a Mersenne prime
        mersenne_candidate = 2 ** p - 1
        if is_prime(mersenne_candidate):
            # Calculate the perfect number using the Mersenne prime
            perfect_number = 2 ** (p - 1) * mersenne_candidate
            perfect_numbers.append(perfect_number)
            count += 1
            print(f"Perfect number {count}: {perfect_number}")
        p += 1

    return perfect_numbers

# Find the first 5 perfect numbers as an example

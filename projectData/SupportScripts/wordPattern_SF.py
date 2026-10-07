import textwrap
from projectData.SupportScripts.globalUDFs import *

character_bold_matrix_64 = {
    'a': (
        (3, 4), (2, 3, 4, 5), (1, 2, 5, 6), (1, 2, 5, 6), (1, 2, 3, 4, 5, 6), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7)),
    'b': ((0, 1, 2, 3, 4, 5, 6), (1, 2, 6, 7), (1, 2, 6, 7), (1, 2, 6), (1, 2, 3, 4, 5), (1, 2, 6, 7), (1, 2, 6, 7),
          (0, 1, 2, 3, 4, 5, 6)),
    'c': (
        (2, 3, 4, 5, 6, 7), (0, 1, 2, 7), (0, 1, 2), (0, 1, 2), (0, 1, 2), (0, 1, 2), (0, 1, 2, 7), (2, 3, 4, 5, 6, 7)),
    'd': ((0, 1, 2, 3, 4, 5, 6), (2, 3, 6, 7), (2, 3, 6, 7), (2, 3, 6, 7), (2, 3, 6, 7), (2, 3, 6, 7), (2, 3, 6, 7),
          (0, 1, 2, 3, 4, 5, 6)),
    'e': ((0, 1, 2, 3, 4, 5, 6, 7), (2, 3, 7), (2, 3), (2, 3, 4, 5), (2, 3, 4, 5), (2, 3), (2, 3, 7),
          (0, 1, 2, 3, 4, 5, 6, 7)),
    'f': ((0, 1, 2, 3, 4, 5, 6, 7), (2, 3, 7), (2, 3), (2, 3, 4, 5), (2, 3, 4, 5), (2, 3), (2, 3), (1, 2, 3, 4)),
    'g': ((2, 3, 4, 5, 6), (1, 2, 7), (0, 1), (0, 1), (0, 1, 4, 5, 6, 7), (1, 5, 6), (2, 5, 6), (2, 3, 4, 5, 6)),
    'h': (
        (0, 1, 2, 5, 6, 7), (1, 2, 5, 6), (1, 2, 5, 6), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6), (1, 2, 5, 6),
        (1, 2, 5, 6),
        (0, 1, 2, 5, 6, 7)),
    'i': ((0, 1, 2, 3, 4, 5, 6, 7), (0, 1, 2, 3, 4, 5, 6, 7), (3, 4), (3, 4), (3, 4), (3, 4), (0, 1, 2, 3, 4, 5, 6, 7),
          (0, 1, 2, 3, 4, 5, 6, 7)),
    'j': ((0, 1, 2, 3, 4, 5, 6, 7), (3, 4), (3, 4), (3, 4), (3, 4), (0, 3, 4), (0, 2, 3), (0, 1, 2)),
    'k': (
        (0, 1, 2, 3, 7), (1, 2, 5, 6), (1, 2, 4, 5), (1, 2, 4), (1, 2, 3, 4), (1, 2, 4, 5), (1, 2, 5, 6), (0, 1, 2, 3,
                                                                                                           7)),
    'l': (
        (0, 1, 2, 3,), (0, 1, 2, 3,), (1, 2,), (1, 2), (1, 2), (1, 2, 7), (0, 1, 2, 3, 4, 5, 6, 7),
        (0, 1, 2, 3, 4, 5, 6, 7)),
    'm': ((0, 1, 6, 7), (0, 1, 2, 5, 6, 7), (0, 1, 3, 5, 6, 7), (0, 1, 3, 4, 6, 7), (0, 1, 3, 6, 7), (0, 1, 6, 7),
          (0, 1, 6, 7), (0, 1, 2, 5, 6, 7)),
    'n': ((0, 1, 2, 5, 6, 7), (1, 2, 3, 6), (1, 2, 3, 6), (1, 3, 4, 5, 6), (1, 4, 5, 6), (1, 4, 5, 6), (1, 5, 6),
          (0, 1, 2, 6)),
    'o': ((2, 3, 4, 5), (1, 2, 5, 6), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7),
          (1, 2, 5, 6), (2, 3, 4, 5)),
    'p': ((0, 1, 2, 3, 4, 5), (1, 2, 5, 6), (1, 2, 6, 7), (1, 2, 5, 6), (1, 2, 3, 4, 5), (1, 2), (1, 2), (0, 1, 2, 3)),
    'q': ((1, 2, 3, 4), (0, 1, 4, 5), (0, 1, 4, 5), (0, 1, 4, 5), (0, 1, 4, 5), (1, 2, 3, 4), (5,), (6, 7)),
    'r': ((0, 1, 2, 3, 4, 5), (1, 2, 5, 6), (1, 2, 6, 7), (1, 2, 5, 6), (1, 2, 3, 4, 5), (1, 5, 2), (1, 2, 5, 6),
          (0, 1, 2, 3, 6, 7)),
    's': ((3, 4, 5, 6), (2, 3, 7), (1, 2), (1, 2, 3), (4, 5), (5, 6), (0, 5, 6), (1, 2, 3, 4)),
    't': ((1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 4, 7), (3, 4), (3, 4), (3, 4), (3, 4), (2, 3, 4, 5)),
    'u': ((0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7),
          (1, 2, 5, 6), (2, 3, 4, 5)),
    'v': ((0, 1, 2, 5, 6, 7), (0, 1, 2, 5, 6, 7), (1, 2, 5, 6), (1, 2, 5, 6), (1, 2, 4), (1, 2, 4), (2, 3), (3, 4)),
    'w': ((0, 1, 2, 7), (1, 2, 7), (1, 2, 5, 7), (1, 2, 4, 5, 7), (1, 2, 4, 5), (2, 3, 5, 6), (2, 3, 5, 6),
          (2, 3, 5, 6)),
    'x': ((0, 1, 6, 7), (0, 1, 6, 7), (1, 2, 5, 6), (3, 4), (3, 4), (1, 2, 5, 6), (0, 1, 6, 7), (0, 1, 6, 7)),
    'y': ((0, 1, 2, 5, 6, 7), (1, 2, 5, 6), (1, 2, 5, 6), (2, 3, 4, 5), (3, 4), (3, 4), (3, 4), (2, 3, 4, 5)),
    'z': ((0, 1, 2, 3, 4, 5, 6, 7), (0, 5, 6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2, 3, 7),
          (0, 1, 2, 3, 4, 5, 6, 7)),

}

character_matrix_64 = {
    'a': (
        (3, 4), (2, 3, 4, 5), (2, 5), (1, 6), (1, 2, 3, 4, 5, 6), (1, 6), (0, 7), (0, 7)),
    'b': ((0, 1, 2, 3, 4, 5, 6), (1, 7), (1, 7), (1, 6), (1, 2, 3, 4, 5), (1, 7), (1, 7),
          (0, 1, 2, 3, 4, 5, 6)),
    'c': ((2, 3, 4, 5, 6, 7), (0, 1, 7), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1, 7), (2, 3, 4, 5, 6, 7)),
    'd': ((0, 1, 2, 3, 4, 5, 6), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (0, 1, 2, 3, 4, 5, 6)),
    'e': ((0, 1, 2, 3, 4, 5, 6, 7), (2, 7), (2,), (2, 3, 4, 5), (2,), (2,), (2, 7), (0, 1, 2, 3, 4, 5, 6, 7)),
    'f': ((0, 1, 2, 3, 4, 5, 6, 7), (2, 3, 7), (2,), (2, 3, 4, 5), (2,), (2,), (2,), (1, 2, 3, 4)),
    'g': ((2, 3, 4, 5, 6), (1, 7), (0,), (0,), (0, 5, 6, 7), (1, 6), (2, 6), (3, 4, 5, 6)),
    'h': ((0, 1, 2, 5, 6, 7), (1, 6), (1, 6), (1, 2, 3, 4, 5, 6), (1, 6), (1, 6), (1, 6), (0, 1, 2, 5, 6, 7)),
    'i': ((0, 1, 2, 3, 4, 5, 6, 7), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (0, 1, 2, 3, 4, 5, 6, 7)),
    'j': ((0, 1, 2, 3, 4, 5, 6, 7), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (0, 3, 4), (0, 1, 2, 3)),
    'k': ((0, 1, 2, 6, 7), (1, 5), (1, 4), (1, 3), (1, 3), (1, 4), (1, 5), (0, 1, 2, 6, 7)),
    'l': ((0, 1, 2,), (1,), (1,), (1,), (1,), (1,), (1, 7), (0, 1, 2, 3, 4, 5, 6, 7)),
    'm': ((0, 7), (0, 1, 6, 7), (0, 2, 5, 7), (0, 3, 4, 7), (0, 3, 4, 7), (0, 7),
          (0, 7), (0, 1, 6, 7)),
    'n': ((0, 6, 7), (0, 1, 7), (0, 2, 7), (0, 3, 7), (0, 4, 7), (0, 5, 7), (0, 6, 7), (0, 1, 7)),
    'o': ((2, 3, 4, 5), (1, 6), (0, 7), (0, 7), (0, 7), (0, 7),
          (1, 6), (2, 3, 4, 5)),
    'p': ((0, 1, 2, 3, 4, 5), (1, 6), (1, 7), (1, 6), (1, 2, 3, 4, 5), (1,), (1,), (0, 1, 2)),
    'q': ((1, 2, 3, 4), (0, 5), (0, 5), (0, 5), (0, 5), (1, 2, 3, 4), (5,), (6, 7)),
    'r': ((0, 1, 2, 3, 4, 5), (1, 6), (1, 7), (1, 6), (1, 2, 3, 4, 5), (1, 5), (1, 6), (0, 1, 2, 7)),
    's': ((3, 4, 5, 6), (2, 7), (1,), (2, 3), (4,), (5,), (0, 5,), (1, 2, 3, 4)),
    't': ((0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 4, 7), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (2, 3, 4, 5)),
    'u': ((1, 6), (1, 6), (1, 6), (1, 6), (1, 6), (1, 6), (1, 6),
          (2, 3, 4, 5)),
    'v': ((0, 1, 6, 7), (0, 1, 6, 7), (1, 6), (1, 6), (2, 5), (2, 4), (3,), (3,)),
    'w': ((0, 7), (0, 4, 7), (0, 3, 5, 7), (0, 2, 4, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 1, 6, 7), (0, 7)),
    'x': ((0, 7), (1, 6), (2, 5,), (3, 4), (3, 4), (2, 5,), (1, 6), (0, 7)),
    'y': ((1, 7), (1, 6), (1, 6), (2, 5), (3, 4), (3, 4), (3, 4), (3, 4)),
    'z': ((0, 1, 2, 3, 4, 5, 6, 7), (0, 6,), (5,), (4,), (3,), (2,), (1, 7), (0, 1, 2, 3, 4, 5, 6, 7))
}


def createMatrix(row, col, type=0):
    if type == 0:
        return [[' ' for _ in range(col)] for _ in range(row)]
    else:
        return [['#' for _ in range(col)] for _ in range(row)]


def slicing_list(char, ls, pattern):
    x = 0
    lp = len(pattern)
    for tp in ls:
        ot = tp[0]
        it = tp[1]
        for i in range(ot[0], ot[1]):
            for j in range(it[0], it[1]):
                char[i][j] = pattern[x % lp]
                x += 1
    return char


def allocate_matrix1(allocation_list, pattern, multiplier, type=0):
    char = createMatrix(8 * multiplier, 8 * multiplier, type)
    temp_pattern = ['#', ' ']
    next_pattern_pointer = 0
    length_of_pattern = len(pattern)
    for i, row in enumerate(allocation_list):
        for col in row:
            for x in range(multiplier):
                for y in range(multiplier):
                    char[(i * multiplier) + x][(col * multiplier) + y] = temp_pattern[type]
    for i, row in enumerate(char):
        for j, col in enumerate(row):
            if char[i][j] == '#':
                char[i][j] = pattern[next_pattern_pointer % length_of_pattern]
                next_pattern_pointer += 1
    return char


def allocate_matrix(allocation_list, pattern, multiplier):
    char = createMatrix(8 * multiplier, 8 * multiplier)
    next_pattern_pointer = 0
    length_of_pattern = len(pattern)
    for i, row in enumerate(allocation_list):
        for col in row:
            for x in range(multiplier):
                for y in range(multiplier):
                    char[(i * multiplier) + x][(col * multiplier) + y] = pattern[
                        next_pattern_pointer % length_of_pattern]
                    next_pattern_pointer += 1
    return char


def copy_matrix(arr, ls, temp_matrix):
    x = 0
    for i in range(ls[0][0], ls[0][1]):
        y = 0
        for j in range(ls[1][0], ls[1][1]):
            arr[i][j] = temp_matrix[x][y]
            y += 1
        x += 1


def print_matrix(char, color, word_length):
    if color in range(0, 10):
        print('\n\n\n\n\n')
        for row in char:
            colorPrint2(textwrap.fill(''.join(row), width=512), index_to_color.get(color))
        print('\n\n\n')
    elif color == 10:
        char_color_change = len(char[0]) // word_length
        colorPrint2('\n\n\n\n\n', 'Bright White', 'Black')
        for row in char:
            for i in range(word_length):
                if i % 2 == 0:
                    colorPrint2(''.join(row[i * char_color_change:(i + 1) * char_color_change]),
                                'Bright White', 'Black', end_line='')
                else:
                    colorPrint2(
                        ''.join(row[i * char_color_change:(i + 1) * char_color_change]),
                        text_color='Black', bg_color='Bright White', end_line=' ')
            print()
        colorPrint2('\n\n\n', 'Bright White', 'Black')

    elif color == 12:
        total_row = len(char) - 4
        changepoint = [2 + (total_row // 3), 2 * total_row // 3]
        colorPrint2('\n\n\n', 'Bright White', 'Black')
        for i, row in enumerate(char):
            if i <= changepoint[0]:
                colorPrint2(textwrap.fill(''.join(row), width=512), 'Orange')
            elif i <= changepoint[1]:
                colorPrint2(textwrap.fill(''.join(row), width=512), 'Bright White', )
            elif i > changepoint[1]:
                colorPrint2(textwrap.fill(''.join(row), width=512), 'Green', )
        colorPrint2('\n\n\n', 'Bright White', 'Black')


def changeMultiplier(multiplier):
    extra_character = 0
    while True:
        if multiplier % 5 == 0:
            return extra_character, 5
        elif multiplier % 4 == 0:
            return extra_character, 4
        elif multiplier % 3 == 0:
            return extra_character, 3
        else:
            multiplier += 1
            extra_character += 1


def createWord(word, pattern, broken=True, bold=True, type=0):
    if bold:
        matrix_64 = character_bold_matrix_64
    else:
        matrix_64 = character_matrix_64

    if broken:
        multiplier = 1
    else:
        pattern = pattern.replace(' ', '')
        multiplier = len(pattern)
        if multiplier > 5:
            extra_character, multiplier = changeMultiplier(multiplier)
            if extra_character == 1:
                pattern = '#' + pattern
            elif extra_character == 2:
                pattern = '#' + pattern + '#'
    letter_list = [i for i in word.lower()]
    word_length = len(word)
    letter_matrix = createMatrix((8 * multiplier) + 4, (multiplier * word_length * 10))
    temp_matrix = []
    for i in range(word_length):
        temp_matrix.append(allocate_matrix1(matrix_64.get(letter_list[i]), pattern, multiplier, type))
    counter = 0
    start = 0
    while counter < word_length:
        copy_matrix(letter_matrix, ((2, (8 * multiplier) + 2), (start + 2, start + 2 + (8 * multiplier))),
                    temp_matrix[counter])
        counter += 1
        start = multiplier * counter * 10
    if type == 1:
        for i in (0, 1, len(letter_matrix) - 1, len(letter_matrix) - 2):
            for j, k in enumerate(letter_matrix[i]):
                letter_matrix[i][j] = '#'
        for i, k in enumerate(letter_matrix[2:-2]):
            for j in range(0, 10 * word_length * multiplier, 10 * multiplier):
                letter_matrix[i][j] = '#'
                if j > 0:
                    letter_matrix[i][j - 1] = '#'
    return letter_matrix

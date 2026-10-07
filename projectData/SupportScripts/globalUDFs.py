import re


def valInput(suggest='\nPlease Enter Input', invalid='Please Enter Valid input ... !', category=0):
    while True:
        inp = input("\033[94m" + suggest + reset)
        if category == 0 and inp.isnumeric():
            return int(inp)
        elif category == 4 and re.search('^\d*.?\d*$', inp):
            return float(inp)
        elif category == 3 and inp.isnumeric():
            return int(inp)
        elif category == 3 and re.search('^\d+.\d+$', inp) is not None:
            return float(inp)
        elif category == 1 and re.search('^[A-Za-z]+\s*[A-Za-z]+$', inp) is not None:
            pass
        elif category == 2 and inp.strip().isalpha():
            pass
        else:
            print("\033[31m" + invalid + reset)
            continue
        return inp


import re


def rangeInput(low, high, suggest, invalid='KINDLY ENTER INTEGER OR DECIMAL VALUE  ...!',
               category=1):
    while True:
        inp = input("\033[94m" + suggest + "\033[0m")  # Suggest with ANSI color code
        try:
            if category == 1:  # Integer only
                value = int(inp)
                if low <= value <= high:
                    return value
                else:
                    colorPrint(f'PLEASE ENTER INTEGER IN RANGE OF {str(low)} TO {str(high)} ONLY ...!', 'Yellow')
            elif category == 2:  # Decimal only
                if re.match(r'^[0-9]+\.[0-9]+$', inp):
                    value = float(inp)
                    if low <= value <= high:
                        return value
                    else:
                        colorPrint(f'PLEASE ENTER A DECIMAL IN RANGE OF {str(low)} TO {str(high)} ONLY ...!', 'Yellow')
            elif category == 3:  # Integer or Decimal
                value = float(inp)  # Automatically allows both int and float input
                if low <= value <= high:
                    return value
                else:
                    colorPrint(f'PLEASE ENTER A VALUE IN RANGE OF {str(low)} TO {str(high)} ONLY ...!', 'Yellow')
            elif category == 4:  # Greater than or equal check for integers and decimals
                value = float(inp)
                if low <= value:
                    return value
                else:
                    colorPrint(f'PLEASE ENTER A VALUE GREATER THAN OR EQUAL TO {str(low)} ONLY ...!', 'Yellow')
            elif category == 5:  # Greater than or equal check for integers and decimals
                if not str(inp).isnumeric():
                    raise ValueError
                value = int(inp)
                if low <= value:
                    return value
                else:
                    colorPrint(f'PLEASE ENTER A VALUE GREATER THAN OR EQUAL TO {str(low)} ONLY ...!', 'Yellow')
        except ValueError:
            colorPrint(invalid, 'Red')


font_color = {
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
    "Saffron": "\033[38;5;214m"
}

# Extended ANSI color codes for background colors
background_color = {
    "Black": "\033[40m",
    "Red": "\033[41m",
    "Green": "\033[42m",
    "Yellow": "\033[43m",
    "Blue": "\033[44m",
    "Magenta": "\033[45m",
    "Cyan": "\033[46m",
    "White": "\033[47m",
    "Bright Black": "\033[100m",
    "Bright Red": "\033[101m",
    "Bright Green": "\033[102m",
    "Bright Yellow": "\033[103m",
    "Bright Blue": "\033[104m",
    "Bright Magenta": "\033[105m",
    "Bright Cyan": "\033[106m",
    "Bright White": "\033[107m",
    "Orange": "\033[48;5;208m",
    "Pink": "\033[48;5;213m",
    "Purple": "\033[48;5;129m",
}

reset = "\033[0m"

index_to_color = {0: 'White', 1: 'Cyan', 2: 'Red', 3: 'Blue', 4: 'Green', 5: 'Yellow', 6: 'Orange', 7: 'Pink',
                  8: 'Purple', 9: 'Magenta'}


def colorPrint2(statement, text_color='Bright White', bg_color='Black', end_line='\n'):
    print(background_color.get(bg_color) + font_color.get(text_color) + statement + reset, end=end_line)


def colorPrint(statement, text_color="Bright White"):
    print(font_color.get(text_color) + statement + reset)

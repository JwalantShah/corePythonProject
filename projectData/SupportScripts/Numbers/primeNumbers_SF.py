from projectData.SupportScripts.globalUDFs import *
from tabulate import tabulate
import time
import math

path = ['projectData/Data/Numbers/', '../../Data/Numbers/']
number_of_elements_in_line = 20



def isPrime(number):
    if number <= 1:
        return False, None  # 0 and 1 are not prime numbers
    if number == 2:
        return True, None  # 2 is the only even prime number
    if number % 2 == 0:
        return False, 2  # No need to check further if it's divisible by 2

    limit = int(math.sqrt(number)) + 1  # Only check up to the square root of the number
    for i in range(3, limit, 2):  # Check only odd numbers starting from 3
        if number % i == 0:
            return False, i  # Return the divisor if found
    return True, None  # If no divisors were found, it's prime


def change_number_of_element():
    global number_of_elements_in_line
    number_of_elements_in_line = valInput('ENTER THE NUMBER OF ELEMENT IN A LINE THAT YOU WANT TO SEE.')




def prime_in_range(highest, lowest=0):
    print(time.asctime(time.localtime(time.time())))
    primelist = []
    if lowest == 0:
        primelist.append(2)
    ranges = range(lowest, highest + 1)
    for current_element in ranges:
        # check = isPrime(current_element)
        # print(check)
        if (isPrime(current_element))[0]:
            primelist.append(current_element)
    printRangePrime(lowest, highest, primelist)
    print(time.asctime(time.localtime(time.time())))


def printRangePrime(low, high, list):
    div = int(len(list) / number_of_elements_in_line)
    i = 0
    while i <= div:
        print(list[(i * number_of_elements_in_line): (i + 1) * number_of_elements_in_line])
        i = i + 1
    print('\n\t\t\t\t\tTHERE ARE TOTAL ', len(list), 'PRIME NUMBERS  BEETWEEN ', low, ' and ', high)


def generate_primes_for_duration(minutes):
    try:
        with open(path[0]+'PrimeNumberLog.txt', 'r+') as file:
            last_log = file.readlines()[-1]
            last_prime = int(str.split(last_log, ' :: ')[1])
            print('last prime no processed : ', last_prime)
            file.close()

        lastlist = []
        lastPrime = 0
        current_second = int(time.time())
        end_sec = int(time.time()) + (minutes * 60)
        start_time = time.asctime(time.localtime(time.time()))
        print(start_time)
        number = last_prime + 1
        duration_sec = (end_sec - current_second) % 60
        duration_min = int((end_sec - current_second) / 60)
        duration = ' :: Minutes : ' + str(duration_min) + ' || Seconds : ' + str(duration_sec)

        while (end_sec > current_second):
            current_second = int(time.time())
            if isPrime(number)[0]:
                lastlist.append(number)
                lastPrime = number
            number = number + 1
        end_time = time.asctime(time.localtime(time.time()))
        print('The Algorithms Has Started at : ', start_time, '\nAnd Ended on : ', end_time,
              '\nTotal Prime Number Genereted : ', len(lastlist))
        with open(path[0]+'primeNumberList.txt', 'a') as file:
            for i in lastlist:
                file.write(str(i))
                file.write('\n')
            file.close()
        strigLog = 'Last Prime :: ' + str(lastPrime) + ' :: Total Generated Primes :: ' + str(
            len(lastlist)) + ' :: ' + start_time + ' :: ' + end_time + ' :: Total run time' + duration
        # listtemp=str.split(strigLog,' :: ')
        # print(listtemp)
        with open(path[0]+'PrimeNumberLog.txt', 'a') as file:
            file.write('\n')
            file.write(strigLog)
            file.close()
    finally:
        print()

def generation_logs():
    with open(path[0]+'PrimeNumberLog.txt', 'r') as file:
        logs = file.readlines()
        data=[]
        headers=['SR NO.','LAST GENERATED PRIME','TOTAL GENERATED PRIMES ','ALGORITHMS STARTED ON','ALGORITHM ENDED ON',
                 'TOTAL RUN TIME']
        for i,log in enumerate(logs,start=1):
            log = log.split(' :: ')
            data.append([i,log[1],log[3],log[4],log[5],log[7]])
        print('\n\n\n')
        colorPrint(tabulate(data,headers=headers,tablefmt='fancy_grid'),'Bright Green')
        print('\n\n\n')

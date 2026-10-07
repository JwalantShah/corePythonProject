"""This program for demo """
import threading

counter = 0


class MultiplicationTable(threading.Thread):
    def __init__(self, name, n, m):
        super().__init__()
        self.name = name
        self.multiplier = m
        self.multiplicand = n

    def run(self):
        global counter
        print(f'Thread {self.name} started')
        for i in range(1, self.multiplicand + 1):
            print(f'{self.name} : {str(self.multiplier)} X {str(i)} = {str(self.multiplier * i)}')
            counter += 1
        print(f'Thread {self.name} Complete : ')


def counterFun():
    global counter
    for _ in range(1000):
        temp = counter
        time.sleep(0.00001)
        counter =temp+1
import threading
import time

# Shared resource: bank account balance
balance = 1000  # Initial balance

import threading
import time

# Shared resource: bank account balance
balance = 1000  # Initial balance

lock = threading.Lock()
def deposit(amount):
    global balance
    for _ in range(1000):
        with lock:
            temp = balance
            time.sleep(0.0001)  # Simulate computation delay
            balance = temp + amount

def withdraw(amount):
    global balance
    for _ in range(1000):
        with lock:
            temp = balance
            time.sleep(0.0001)  # Simulate computation delay
            balance = temp - amount



def main():
    # t1 = MultiplicationTable('Mars', 10, 991547896549799874573363214568)
    # t2 = MultiplicationTable('Rahu', 10, 8741265479821643611275654649494)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print('Both threads archived', counter)

    t1 = threading.Thread(target=counterFun)
    t2 = threading.Thread(target=counterFun)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Counter : ',counter)

    # Create threads for deposit and withdrawal
    thread1 = threading.Thread(target=deposit, args=(5,))
    thread2 = threading.Thread(target=withdraw, args=(5,))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print(f"Final Balance: {balance}")


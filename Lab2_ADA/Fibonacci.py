from threading import Thread
import threading
import time
from enum import Enum
import numpy as np
import math



class ProcesType(Enum):
    sleepy = "sleepy"
    busy = "busy"
    unknown = 99


class FibonacciCalc:

    def Calculate(self, num, ProcessType):

        if ProcessType == ProcesType.busy:
            return self.busy_fibonacci(num)
        elif ProcessType == ProcesType.sleepy:
            return self.sleepy_fibonacci(num)

        raise TypeError("Unsuported processing type")

    def get_procesing_type(self):
        print("Choose Processing Type (s - sleepy b - busy): ")
        choice = input()
        procesType = ProcesType.unknown

        if choice == 'b':
            procesType = ProcesType.busy
        elif choice == 's':
            procesType = ProcesType.sleepy
        else:
            print("Unsuported Type!")

        return procesType

    def sleepy_fibonacci(self, num):
        self.keep_cpu_asleep()
        return self.compute_fibonacci(num)

    def busy_fibonacci(self, num):
        self.keep_cpu_busy()
        return self.compute_fibonacci(num)

    def keep_cpu_asleep(self):

        sleep_milisec = 25 / 1000
        time.sleep(sleep_milisec)

    def keep_cpu_busy(self):

        iterations_count = 1300
        k = 0

        for i in range(0, iterations_count):
            for j in range(0, iterations_count):
                k = k + 1

        return k

    def compute_fibonacci(self, num):

        number1 = 0
        number2 = 1
        fib = 0

        if num <= 0:
            print("Error! This number is negative.")

        elif num == 0:
            return number1
        elif num == 2:
            return number2

        for element in range(2, num):
            fib = number1 + number2
            number1 = number2
            number2 = fib
        return fib

# if __name__ == '__main__':
#
#     f_input = "E:\\master\\ADA\\input.txt"
#     f_otput = "E:\\master\\ADA\\test.txt"
#
#     test = FibonacciCalc()
#     test.sleepy_fibonacci()
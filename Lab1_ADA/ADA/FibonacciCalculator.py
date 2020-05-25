from threading import Thread
import time
from enum import Enum
import numpy as np


class ProcesType(Enum):
    sleepy = "sleepy"
    busy = "busy"
    unknown = 99


class FibonacciCalc:


    def Calculate(self, num, ProcesType):

        if ProcesType == ProcesType.busy:
            return self.busy_fibonacci(num)
        elif ProcesType == ProcesType.sleepy:
            return self.sleepy_fibonacci(num)

        raise TypeError("Unsuported processing type")

    def get_procesing_type(self):
        print("Choose Procesing Type (s - sleepy b - bussy): ")
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
        return  self.compute_fibonacci(num)


    def keep_cpu_asleep(self):
        sleep_milisec = 250/1000
        time.sleep(sleep_milisec)


    def keep_cpu_busy(self):

        iterations_count = 13000
        k = 0

        for i in range(0, iterations_count):
            for j in range(0, iterations_count):
                k = k + 1

        return k


    def compute_fibonacci(self, num):
        file = open("E:\\master\\ADA\\input.txt", 'r')
        content = file.readlines()
        num = np.size(content)

        number1 = 0
        number2 = 1

        if num <= 0:
            print("Error! This number is negative.")

        elif num == 0:
            return number1
        elif num == 2:
            return number2

        with open("E:\\master\\ADA\\test.txt", 'w') as f:
            for element in range(2, num):
                fib = number1 + number2
                number1 = number2
                number2 = fib
                f.write('%d\n' % fib)
                #self.fibonacci_result(fib)
        return fib

    def fibonacci_result(self, num):
        t = time.time()
        t1 = Thread(target=self.sleepy_fibonacci, args= (num,))
        t1.start()
        print("t1", time.time() - t)
        t2 = Thread(target=self.busy_fibonacci, args=(num,))
        t2.start()
        print("t2",time.time() - t)



    # def fibo_proces(self, num, numTask, ProcesType):
    #     #l = list(numTask)
    #
    #     for i in range(0, numTask):
    #
    #         taskIndex = i
    #
    #         fibCalc = FibonacciCalc()
    #         numPerTask = np.size(num) / numTask
    #         numToProces = 0
    #
    #         if taskIndex == numTask - 1:
    #             numToProces = np.size(num) - (numPerTask * (numTask - 1))
    #         else:
    #             numToProces = numPerTask
    #
    #         for i in range(0, numToProces):
    #             numIndex = taskIndex * numPerTask + i
    #             result = fibCalc.Calculate(num[numIndex], ProcesType)


if __name__ == '__main__':
    test = FibonacciCalc()



    # i = 1
    # while i<=32:
    #     print("Runing Threads")
    #     result = test.fibo_proces(50, i, proces.sleepy)
    #     print(result)
    #     i = i * 2
    test.fibonacci_result(50)
    #test.fibo_proces(50, 2, proces.sleepy)
    #test.get_procesing_type()
    #proces = ProcesType
    #print(test.Calculate(50, proces.sleepy))
    #test.compute_fibonacci(50)

# class Program:
#
#     INPUT_FILE = "E:\\master\\ADA\\input.txt"
#     OUTPUT_FILE = "E:\\master\\ADA\\test.txt"
#
#
#
#
#





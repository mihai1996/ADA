import numpy as np


class FileUtility:

    def read_numbers_from_file(self, fileName):
        file = open(fileName, 'r')
        content = file.read().split('\n')
        content = list(map(int, content))
        return  content

    def write_numbers_in_file(self, fileName, numbers):
        file = open(fileName, 'w')
        if numbers != None:
            file.write('%s\n' %numbers)


test = FileUtility()
test.read_numbers_from_file("E:\\master\\ADA\\input.txt")
#test.write_numbers_in_file("E:\\master\\ADA\\test.txt", 3)
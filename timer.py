import time
from matrixFib import matrixFib
from iterativeFib import iterativeFib
from recursiveFib import recursiveFib

mat = matrixFib

file = open('matTimes.txt', 'r+')

for i in range (0,1000000,10000):
    a = time.time()
    #recursiveFib(i)
    b = time.time()

    c = time.time()
    iterativeFib(i)
    d = time.time()

    e = time.time()
    matrixFib(i)
    f = time.time()

    writeStr = str(i) + ',' + str(b-a) +',' + str(d-c) + ',' + str(f-e) + ',' + '\n'
    file.write(writeStr)

import random
import numpy
# from numpy import linalg as lin

def main():

    a = numpy.zeros([3,3])

    a[0,0] = 1
    a[1,1] = 1
    a[2,2] = 1

    print(a)
   # for i in range(3):
    #    for j in range(3):
    #        a[i][j] = random.random()

    print(numpy.linalg.eig(a))

if __name__ == '__main__':
    main()

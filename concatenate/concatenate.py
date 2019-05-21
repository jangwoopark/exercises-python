import numpy

a, b, c = map(int,input().split())
arrA = numpy.array([input().split() for _ in range(a)],int)
arrB = numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((arrA, arrB), axis = 0))


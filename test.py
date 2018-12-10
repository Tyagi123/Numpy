import numpy as np

a = np.array([(1, 2, 3, 4), (9.8, 8, 7, 6)])

'''Printing array'''
print(a)

'''print memory address'''
print(a.data)

'''data type ex: float'''
print(a.dtype)

'''number of elements '''
print(a.itemsize)

mat = np.random.randint(0, 6, (5, 5))
print(mat)

print(mat[2:5, 3:6])

'''zero array of size 10 '''
print(np.zeros(10))

'''Reverse a above created array'''
r = np.random.randint(4, 7, (10))
print(r)
print(r[-1:0:-1])
print(r[9:0:-1])

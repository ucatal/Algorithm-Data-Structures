import sys

# set n 10
n = 100

data = []

for i in range(n):

    #number of elements
    a = len(data)

    #actual size in bytes
    b = sys.getsizeof(data)

    print('Lenght: {0:3d};size in bytes:{1:4d}'.format(a,b))

    #increase length by one
    data.append(n)

    
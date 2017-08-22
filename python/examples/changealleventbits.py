def changeAllEvenBits(n):
    binary = '{0:b}'.format(n)
    # print(n & 0xaaaaaaaa)
    length = len(binary)
    array = binary.split()
    for i in range(0,length,2):
        array[i] =0
    
    print("".join(array))

changeAllEvenBits(30)
import math

def power_two(n):
    return int(math.log(n, 2))


def convetToBaseTwo(number):
    K = 2
    digit = []
    
    while(number!=0):
        reminder = int(number % K) 
        number = int(number / K)
        digit.append(str(reminder))
    
    return "".join(digit)        

res = convetToBaseTwo(21)


print(res)
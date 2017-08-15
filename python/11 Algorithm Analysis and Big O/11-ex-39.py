def sum1(n):
    final_sum = 0

    for x in range(n+1):
        final_sum += x
    
    return final_sum

res =  sum1(10)
print(res)
#The slowest run took 5.15 times longer than the fastest. This could mean that an intermediate result is being cached 
#100000 loops, best of 3: 4.86 µs per loop


def sum2(n):
    return (n*(n+1))/2

res =sum2(10)
print(res)
    
#The slowest run took 16.54 times longer than the fastest. This could mean that an intermediate result is being cached 
#10000000 loops, best of 3: 173 ns per loop

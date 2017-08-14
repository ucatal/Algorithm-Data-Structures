def method1():
    l = []
    for c in range(10000):
        l = l +[c]

def method2():
    l = []
    for c in range(10000):
        l.append(c)


def method3():
    l = [n for n in range(10000)]

    
def method4():
    l = range(10000)

method1()
method2()
method3()
method4()
# 10 loops, best of 3: 162 ms per loop
# 1000 loops, best of 3: 820 µs per loop
# 1000 loops, best of 3: 307 µs per loop
# 10000 loops, best of 3: 77.7 µs per loop

#dictionary
d = {'k1':1,'k2':2}
d['k1']
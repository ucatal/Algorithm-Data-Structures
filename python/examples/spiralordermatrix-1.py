# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
# a= [    
#   [ 1, 2, 3 ],    
#   [ 4, 5, 6 ],    
#   [ 7, 8, 9 ]
# ]

# expextedReturnValue = [1, 2, 3, 6, 9, 8, 7, 4, 5]


def spiralOrderMatrix(A):
    m = len(A)
    if m == 0:
        return A

    n = len(A[0])
    if n == 0:
        return A
    T=0  #top
    B=m-1 #botton
    L=0 #left
    R=n-1 #right
    direction = 0 #0=> 1(down) 2<= 3(up)
    result =[]
    while(T<=B and L<=R):
        if(direction==0):
            for k in range(T,R+1):
                result.append(A[T][k])
            T +=1
            direction = 1
        elif(direction==1):
            for k in range(T,B+1):
                result.append(A[k][R])
            R -=1
            direction = 2
        elif(direction == 2):
            for k in reversed(range(L,R+1)):
                result.append(A[B][k])
            B -=1
            direction = 3
        elif(direction == 3):
            for k in reversed(range(T,B+1)):
                result.append(A[k][L])
            L +=1
            direction = 1
            
    return result



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class spiralOrderMatrixTest(object):
    
    def test(self,sol):
        assert_equal(sol([[ 1, 2, 3 ],[ 4, 5, 6 ], [ 7, 8, 9 ]]),[1, 2, 3, 6, 9, 8, 7, 4, 5])
        print("ALL TEST CASES PASSED")

# Run Tests
t = spiralOrderMatrixTest()
t.test(spiralOrderMatrix)
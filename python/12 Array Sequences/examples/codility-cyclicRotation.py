#https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

# Write a function:

# def solution(A, K)
# that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

def rightrotation(A, K):
    l = len(A)
    if l == 0:
        return A
    if K>=l:
        K%=l
    
    return A[-K:] + A[:-K]

def leftRotation(A, K):
    l = len(A)
    if l == 0:
        return A
    if K>=l:
        K%=l
    
    return A[K:] + A[:K]

#TODO find second solution
 
A = [1,2,3,4,5]
K = 6
print(rightrotation(A, K))
print(leftRotation(A, K))
print(A[-K:]) 
print(A[:-K])
print(A[K:]) 
print(A[:K])

# print(solution2(A, K))
# print(A[-K:])
# print(A[:-K])
     #         if (l == 0 || K == 0)
    #         {
    #             return A;
    #         }
    #         if (start < 0)
    #         {
    #             start = -(start - 1);
    #         }
    #         for (int i = start; i < l; i++)
    #         {
    #             outA[j] = A[i];
    #             j++;
    #         }
    #         for (int m = 0; m < start; m++)
    #         {
    #             outA[j] = A[m];
    #             j++;
    #         }
    #         return outA;

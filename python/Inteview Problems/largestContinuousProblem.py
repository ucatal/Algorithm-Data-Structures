# Largest Continuous Sum
#Kadane's algorithm[edit]

# Problem
# Given an array of integers (positive and negative) find the largest continuous sum.
# Solution
# Fill out your solution below:


def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum

res = large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
print(res)

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)
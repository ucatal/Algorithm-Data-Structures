# Array Pair Sum¶
# Problem
# Given an integer array, output all the unique pairs that sum up to a specific value k.
# So the input:
# pair_sum([1,3,2,2],4)

# would return 2 pairs:
#  (1,3)
#  (2,2)

#NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

def pair_sum(arr,k):
    pairedCount = 0 
    pairedItemIndexes = {}
    i = 0
    j = 1
    length = len(arr)
    
    while i < length:
        x = arr[i]
        if i in pairedItemIndexes:
            i +=1               
            continue
        j = i+1         
        while j < length:
            y = arr[j]
            if j in pairedItemIndexes:
                j +=1
                continue
            if x+y == k:
                pairedItemIndexes[i] = 1
                pairedItemIndexes[j] = 1
                pairedCount +=1
                j+=1
                break
            j+=1
        
        i+=1 
    return pairedCount
    pass
    


def pair_sum2(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

    
res = pair_sum2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
print(res)
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)
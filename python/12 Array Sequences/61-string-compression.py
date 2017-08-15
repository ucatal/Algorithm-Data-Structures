# String Compression
# Problem
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compressMy(s):
    if not s:
        return ''   
    l = len(s)
    if l is 1:
        return s+"1"
    # charDic = {}
    counter = 1
    r=""
    i = 1
    while i<l:
        if s[i] == s[i-1]:
            counter+=1
        else:
            r = r+s[i-1]+str(counter)
            counter = 1
        i+=1
    #my wrong solution
    # for c in s:
    #     if c in charDic:
    #         charDic[c] +=1
    #     else:
    #         charDic[c] = 1

    # result = ''.join('{}{}'.format(key, val) for key, val in charDic.items())
    r = r + s[i - 1] + str(counter)

    print(r)
    return r
    pass


def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    print(r)
    return r

compress('AAAAABBBBCCCAAC')



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('A'), 'A1')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compressMy)
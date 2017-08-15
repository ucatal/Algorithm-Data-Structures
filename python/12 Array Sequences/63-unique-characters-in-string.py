
# Unique Characters in String
# Problem
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

def uni_charMy(s):
    if not s:
        return True   
    charDic = {} 
    for c in s:
        if c in charDic:
            return False
        else:
            charDic[c] = 1
    return True
    pass

def uni_char(s):
    
    return len(set(s)) == len(s)
    pass


def uni_char2(s):
    chars = set() 
    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True
    pass

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char2)
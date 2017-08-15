def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    splitted2 = list(s2)
    splitted1 = list(s1)

    isAnagram = False    
    
    isCountSame = len(splitted1) == len(splitted2)
    if isCountSame :
        listSame = any(map(lambda v: v in splitted2, splitted1))
        isAnagram = (isCountSame and (listSame))

    return isAnagram

def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
 
    return sorted(s1) == sorted(s2)

# def anagram2(s1,s2):
#     s1 = s1.replace(' ','').lower()
#     s2 = s2.replace(' ','').lower()
     
#     isAnagram = False    
    
#     if len(s1) == len(s2):
#         isAnagram = True
    
#     count = {}
 
#     for letter in s1:
#         if letter in count:
#             count[letter] +=1
#         else:
#             count[letter] =1
    
#     for letter in s2:
#         if letter in count:
#             count[letter] = count[letter]-1
#         else:
#             count[letter] = 1
    
#     for k in count:
#         if count[k] != 0:
#             isAnagram = False
#             return isAnagram
#         else:
#             isAnagram = True
#             return isAnagram
    
#     return isAnagram 




"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','agggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
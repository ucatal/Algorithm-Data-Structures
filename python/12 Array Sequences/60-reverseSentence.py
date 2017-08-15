def rev_word(s): 
    print(" ".join(s.split()[::-1]))
    pass

def rev_word2(s):
    print(' '.join(list(reversed(s.split())))) 
    pass

def rev_word(s):
    spaces = [' ']
    words = []
    length  = len(s)

    i = 0
    while i<length:
        if s[i] not in spaces:
            word_start = i
        
            while i< length and s[i] not in spaces:
                i+=1

            words.append(s[word_start:i])
        i+=1 
    
    # return ' '.join(reversed(words))
    return final_output(words)

    pass

def final_output(words):
    lenght = len(words)
    i = lenght-1

    result =""
    while i>-1:        
        result += words[i]
        if i != 0:
            result += ' '
        i-=1
    
    return result 
    pass
    
res = rev_word("hi john,     are you ready to go?")
print(res)
#go? to ready you are John,Hi


print(rev_word("    space before"))
#before space


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)
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
    return words

    pass

def final_output(words):
    lenght = len(words)
    i = lenght-1

    result =""
    while i>-1:        
        result +=words[i] + ' '
        i-=1
    
    return result 
    pass
    
res = rev_word("hi john,     are you ready to go?")
print(final_output(res))
#go? to ready you are John,Hi


rev_word("    space before")
#before space
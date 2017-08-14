#int float
pi = 3.14129
number = 5  
print (pi)
total = number+pi

#boolean None
isPython = True
isJava = False
nullObject = None
if isPython:
    print("python")

if not isJava:
    print("is not java")

if nullObject:
    print("is not null")
else:  
    print("is null")

#text
str1 = 'str1'
str2 = """str2""".capitalize()
text = f"test {str1} {str2}"
textformat ="test textformat {0}".format(str1)

if text:
    print("text is not null =>" + text)
else:
    print("text is null")

print(textformat)

#array
splittext = "1,2,3,4,5"
numbersArray = splittext.split(",")
firstItem = numbersArray[0];
lastItem = numbersArray[-1];
slicedList =numbersArray[1:] #1234
slicedList =numbersArray[-1:] #5
slicedList =numbersArray[1:-1] #234 just ignored our first and our last elements in the list 
slicedList =numbersArray[-1:1] #

length = len(numbersArray)

#a[start:end] # items start through end-1
#a[start:]    # items start through the rest of the array
#a[:end]      # items from the beginning through end-1
#a[:]         # a copy of the whole array
#a[start:end:step] # start through not past end, by step
#a[-1]    # last item in the array
#a[-2:]   # last two items in the array
#a[:-2]   # everything except the last two items

#if conditions
if numbersArray:
    print(numbersArray)

result = "Bigger" if 5<4 else "Smaller"

print(result)
print(text)
 
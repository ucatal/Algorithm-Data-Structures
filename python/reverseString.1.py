# Reverse a String
#http://practice.geeksforgeeks.org/problems/reverse-the-string/0
# Given a string S as input. You have to reverse the given string.

# Input: First line of input contains a single integer T which denotes the number of test cases. T test cases follows, first line of each test case contains a string S.

# Output: Corresponding to each test case, print the string S in reverse order.

# Constraints:

# 1<=T<=100
# 3<= length(S) <=1000

# Example:

# Input:
# 3
# Geeks
# GeeksforGeeks
# GeeksQuiz

# Output:
# skeeG
# skeeGrofskeeG
# ziuQskeeG

# **For More Examples Use Expected Output**

###############################Solution1

x = int(input())
while x > 0:
    string = input()
    print(string[::-1])
    x = x - 1


################# MySolution
def reverse(text):
    charArray = list(text)
    length = len(charArray)
    reversedText = ""
    for s in range(length - 1, -1, -1):
        reversedText = reversedText + str(charArray[s])

    print(reversedText)


n = int(input())
for i in range(n):
    reverse(input())

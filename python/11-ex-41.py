def create_list(n):
    new_list = []
    
    for num in range(n):
        new_list.append('new')
    
    return new_list

# def func_constant(values): 

#     print(values[0]) 

# def func_linear(lst):

#     for val in lst:
#         print(val)

# def func_quad(lst):
#     for item1 in lst:
#         for item2 in lst:
#             print(item1,item2)

# def print_once(lst):
#     '''
#     O(n) Prints all items once
#     '''
#     for val in lst:
#         print(val)

# def print_2(lst):
#     '''
#     O(n)
#     '''
#     for val in lst:
#         print(val)

#     for val in lst:
#         print(val)

# def comp(lst):
#     '''
#     This function prints the first item O(1)
#     Then is prints the first 1/2 of the list O(n/2)
#     Then prints a string 10 times O(10)
#     O(1 + n/2 + 10)
#     as a result O(n)
#     '''
#     print(lst[0])
    
#     midpoint = len(lst)/2 
    
#     for val in lst[:int(midpoint)]:
#         print(val)
        
#     for x in range(10):
#         print('number')


# def matcher(lst,match):
#     '''
#     Given a list lst, return a boolean indicating if match item is in the list
#     '''
#     for item in lst:
#         if item == match:
#             return True
#     return False
# def printer(n=10):
#     '''
#     Prints "hello world!" n times
#     '''
#     for x in range(n):
#         print('Hello World!')
#Note how we only assign the 'hello world!' variable once, not every time we print. 
# So the algorithm has O(1) space complexity and an O(n) time complexity.

#func_constant(list)#O(1)
#func_linear(list)#O(n)
#func_quad(list)#O(n^2)
#print_once(list)
#print_2(list)

#comp(list)
#matcher(list,1) #O(1)
#matcher(list,11) #O(n)

#list = [1,2,3,4,5,6,7,8,9,10]
# printer()

print(create_list(5))
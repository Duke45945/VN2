
#program to write a table for a given number
def table_writer(num):
    print(f'The table of {num} : \n{num} * 1 = {num*1} \n{num} * 2 = {num*2} \n{num} * 3 = {num*3} \n{num} * 4 = {num*4} \n{num} * 5 = {num*5} \n{num} * 6 = {num*6} \n{num} * 7 = {num*7} \n{num} * 8 = {num*8} \n{num} * 9 = {num*9} \n{num} * 10 = {num*10}')
    return f'{num} * 1 = {num*1} \n{num} * 2 = {num*2} \n{num} * 3 = {num*3} \n{num} * 4 = {num*4} \n{num} * 5 = {num*5} \n{num} * 6 = {num*6} \n{num} * 7 = {num*7} \n{num} * 8 = {num*8} \n{num} * 9 = {num*9} \n{num} * 10 = {num*10}'
table_writer(15)

#Sum of all numbers
def adder(x):
    num = 0
    for eac_num in x:
        num = num + eac_num
    print("\n\nadding the elements: \t",x)
    print("\nthe final sum is : \t", num)
    return num 
adder([55,6,25])

#Multiply all the elements
def Multiplier(x):
    num = 1
    for eac_num in x:
        num = num * eac_num
    print("\n\nMultiplying the elements: ",x)
    print("\nthe final number is : \t", num)
    return num 
Multiplier([5,6,25])

#calculate all the upper and lower charecters of a string
def upper_lower(x):
    upper_list = []
    lower_list = []
    for each_letter in x:
        if each_letter.isupper():
            upper_list.append(x)
        else :
            lower_list.append(x)
    print(f"The number of uppercase letters : {len(upper_list)}\nThe number of lower case letters : {len(lower_list)}")
    return len(upper_list) , len(lower_list)
upper_lower('hohohoHEHE')

#Get uniqu elements of a list :
def uniq_lst(x):
    list_2 = list(set(x))
    print('Entered list ',x)
    print(f"Unique elements in the list are \n{list_2}")
    return list_2

uniq_lst([10,11,10,12,10,12,11,12,1,11,12,12,33,54,15,12])

#Pascals Triangle
from math import factorial
def pascal_triangle(num): 
    for i in range(num):
        for j in range(num-i+1):
            # for left spacing
            print(end=" ")   
        for j in range(i+1):
            # Formula : nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        # for new line
        print() 
pascal_triangle(6)

#Palindrome check:
def palindrome_check(x:str):
    if x == x[::-1]:
        print(f'The string {x} is a palindrome')
        return f'The string {x} is a palindrome'

palindrome_check('kayak')

#range check

def range_check(num,low,high):
    if num > low and num < high :
        print(f"the number {num} is in between {low} and {high}")
        return True
    else:
        print(f"the number {num} is not in between {low} and {high}")
        return False

range_check(7,5,10)
range_check(12,15,35)


#sqaure of a number
def square_num(x):
    print(f"The square of {x} is {x**2}")
    return x**2
square_num(11)

#return funcs

def even_check(x):
    if x % 2 == 0 :
        print(f"{x} is even")
        return True
    else :
        print(f"{x} is odd")
        return False
    
even_check(35.236)

def factorial_func(num):
    x = 1
    for i in range(1, num + 1):
       x = x*i
    print(f"The factorial of {num} is {x}")
    return x
factorial_func(5)

def add_me(x,y):
    print(f"The addition of {x} and {y} is : {x + y}")
    return x + y 

add_me(33,153)

def sum_diff(x,y):
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    return x+y, x-y

sum_diff(96,44)


    

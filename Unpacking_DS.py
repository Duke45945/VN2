# Unpacking a List
roll_nums = [1,2,6,88,153,456]

# Basic Unpacking by assigning variables
print('List unpacking using without any loops and variable assignment')

harsha,dinesh,*others = roll_nums

print('The List is ' ,roll_nums)
print('Harsha -- ' ,harsha)
print('dinesh -- ' ,dinesh)
print('all the other Variables -- ' ,others)


print('\n\nList unpacking using For loops')

# Iterating through a For loop
for i in roll_nums:
    print(i)
obj1 = 0 

# Iterating through a While Loop
print('\n\nList unpacking using While loops')

while obj1 < len(roll_nums):
    print(roll_nums[obj1])
    obj1 = obj1 + 1 


# Tuple Unpacking
tup1 = (9, 5, 'hello', 6.33)
print('\n\ntuple unpacking  without any loops and variable assignment')
a,b,*ot33 = tup1
print('a -- ', a)
print('b --',b)
print('ot33 --',ot33)
print('\n\ntuple unpacking using for loop')
for i in tup1:
    print(i)
print('\n\ntuple unpacking using While loop')
m = 0
while m < len(tup1):
    print(tup1[m])
    m += 1

dict1 = {'k1' : "kelly", 'k2' : "Sun ", 'k3' : 556, 'k9' : 'Coco', 'k5' : 600.236}
d1,d2,d3,*ot55 = dict1.items()
print('\n\n Dictionary unpacking  without any loops and variable assignment')
print(d1)
print(d2)
print(d3)
print(ot55)

print('\n\n Dictionary unpacking Using For loops ')

for i in dict1.items():
    print(i)
print('\n\n Dictionary unpacking Using While loops ')

i = 0
while i < len(list(dict1.items())):
    print(list(dict1.items())[i])
    i += 1
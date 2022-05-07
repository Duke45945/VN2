# Program 5 
# finding and printing the duplicate keys

sample_dict = { 'k1' : 'Val1', 'k1' : 'Val2', 'k1' : 'Val3', 'k2' : 'Val1','k2' : 'Val1','k3' : 'Val1' }
key_list = []
#Need you help, Harsha. Cannot figure out this one 
print(sample_dict.items())
print(key_list)

#program 6
#user inputs a database of names and IDs 
list_sample = []
i = 0
while i < 5:
    name = input('enter the name : ')
    id = input('enter the ID : ')
    dict_1 = {'name':name, 'ID' : id }
    list_sample.append(dict_1)
    i = i + 1   
print(list_sample)

#Program 7
#Print out ony the values:
my_own = {'1':'harsha','name':{'location':{'bangalore':{'marath','white'},'che':{1:{'hy','ra'}}}}}

def str_check(value):
    if type(value) == str or type(value) == int:
        print(value)
def dict_check(value):
    if type(value) == dict:
        for key,val in value.items():
            str_check(val)
            dict_check(val)
    elif type(value) == set:
        for i in value:
            print(i)
for values in my_own.values():
    #checking for the values
    str_check(values)
    dict_check(values)


            


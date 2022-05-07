#Program 1
#return the iteration of a nested list
#you can add a custom list, if you do not like the sample list
sample_list = [1,2,3,4,5,[ 'hello', 11.023, 45 ]]
#creating a place holder for the nested list
nest_list = []
for each_item in sample_list:
    #checking if the item in the list is a nested list
    if type(each_item) == list :
        #appending the results
        nest_list.extend(each_item)
print('\n\nThe items in the nested list are : \n\n')
#looping the output list for desired output
for item in nest_list:
    print(item)

#Program 2
#return the value of a certain key and count the number of occurences in it.
sample_dict = {'k1':'dinesh', 'k2':'harsha', 'k3':'superman'}
    # you can also change the dictionary to add more content!!
keyword_value = ''
for i in sample_dict.values():
    if i == 'harsha':
        keyword_value = i
lst1 = list(set(keyword_value))
dict_1 = {lst1[a]:keyword_value.count(lst1[a]) for a in range(0,len(lst1))}
print('The retrieved value string is ---- ', keyword_value)
print(dict_1)

#program 3
#Transpose a given matrix
def transpose(Input_matrix ,Output_matrix):
    for i in range(0,3):
        for j in range(0,3):
            Output_matrix[i][j] = Input_matrix[j][i]
    print(Output_matrix) 
    #Defining the input
sample_matrix = [['haa' ,'hii' ,'hoo'], [9, 8, 7], ['mmm', 'nnn', 'ooo']]
desired_output = sample_matrix[:][:]
transpose(sample_matrix, desired_output)  
print("Result matrix is")
for i in range(0,3):
    for j in range(0,3):
        print(desired_output[i][j], " ", end='')
    print()

#Program 4
#Addition of Two Matrices
X = [[1,22,33],[11,10,0.33]]
Y = [[66,2,31],[55,33,0.23]]
result = [[0,0,0],[0,0,0]]
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)

#Program 5



    

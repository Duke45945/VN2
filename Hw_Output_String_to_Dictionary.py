# The Repeating Dictionary
from operator import itemgetter
from collections import OrderedDict
#Retrieving all the unique letters in the string
str1 = input ('Enter your string')
str2 = str1.lower()
def diction_builder(str2):
    final_dict = {}
#counting all the items
    for each_item in str2:
        if each_item in final_dict: 
            final_dict[each_item] = final_dict[each_item] + 1 
        else:
            final_dict[each_item] = 1
    altered_final_dict = sorted(final_dict.items(), key=itemgetter(1))
    ordered_final_dict = OrderedDict(sorted(final_dict.items(), key=lambda t: t[1] , reverse=True))
    print( ' The Ordered_final_dict method is', ordered_final_dict )
    print( ' The Alter_final_dict method is', altered_final_dict )
print(diction_builder(str2))





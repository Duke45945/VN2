
from collections import OrderedDict
str1 = input('Enter a string here : ')
lst1 = list(set(str1))
dict_1 = {lst1[a]:str1.count(lst1[a]) for a in range(0,len(lst1))}
ordered_final_dict = OrderedDict(sorted(dict_1.items(), key=lambda t: t[1] , reverse=True))
print(ordered_final_dict)




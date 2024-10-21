#each element in an array T, displays that element if its square is also present in the array
from random import randint
def filter_list(list_T):
    list_number=[]
    for x in list_T:
        if x**2 in list_T:
            list_number.append(x)
    return list_number
list_T=[randint(1,10)  for x in range(10) ]
print(list_T)


result=filter_list(list_T)
if result:
 print("element if its quare is also present in the array : %s"% result)
else:
 print("nothing")

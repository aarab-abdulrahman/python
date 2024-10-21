#display the examination schedule

while True:
    a=input("enter exam date: ").replace(',',' ').replace(':',' ').split(' ')
    a_edit=[]
    zero=0
    for x in a:
        if x.isdigit():
            a_edit.append(int(x))
            zero+=1
        else:
            zero+=-1

    if zero==len(a_edit):
       break
    
    else:
        print("something is wrong , try again.\n")

a_edit=tuple(a_edit)
print("The examination will start from : %d/%d/%d" % a_edit)

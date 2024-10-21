#calculate the area of a circle

from math import pi

while True:
    a=input("type <r> : ").replace(' ','')
    if a.replace('.','').isdigit() : 
        break
    else:
        print("error try again")

area=(float(a)**2)*pi
print("the area of the circle is : "+str(area))
try: 
     digits=[]
     min=0
     max=0

     x=int(input("Write the number of times you entre : ").strip())
     for i in range(x):
       while True:
        n=input("entre number {} : ".format(i+1)).strip()
        if not n.replace('-','').isdigit(): print("try again ...\n")
        else:
            digits.append(int(n))
            break
     
     min=digits[0]
     max=digits[0]

     for i in digits:
        if i < min : min=i
        elif i> max : max=i
      
     print("max ---> ",max)
     print("\nmin ---> ",min)

except:
     print("error")
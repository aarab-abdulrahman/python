stock=[]
ask1=input("enter th efirst ans last name of your friends(add comma or space):")
stock+=ask1.replace(' ',',').split(',')
for x in range(0,len(stock),2):
 print(stock[x:x+2])
print("abbreviated names:")
for i in range(0,len(stock),2):
 print((f"{stock[i][0]}.{stock[i+1:i+2][0][0]}").upper())
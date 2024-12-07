def check_number_flouat(x):
 if x.replace('.','').isdigit() and x.count('.')<=1:
   return 1
 else : 
   return 0
 

# Demandez à l'utilisateur de saisir deux dates au format DD-MM-YYYY
# et calculez la différence en jours entre les deux dates.


from datetime import datetime
try :
    date1=input("type a date 1 'Y/M/D':")
    date2=input("type a date 2 'Y/M/D' :")

    date1_obj=datetime.strptime(date1,'%Y/%m/%d')
    date2_obj=datetime.strptime(date2, '%Y/%m/%d')

    if date2_obj>date1_obj :
        difference=(date2_obj - date1_obj)
        difference=difference.days
        print(" le difference est : {} day".format(difference))
    else:
        print('invalide')

except: print("error")
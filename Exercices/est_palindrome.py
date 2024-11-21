def is_date_palindrome(date):
    date_without_hyphens = date.replace("-", "")
    
    return date_without_hyphens == date_without_hyphens[::-1]

try: 
    date1=input("entre date , format('Y'-'M'-'d') ").strip()
    print(" is palindrome ? ----> ",is_date_palindrome(date1)) 
except : print("error")
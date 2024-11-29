import time
import sys

def moving_slash():
    slashes = ['-','/','|','\\']  
    duration = 10  
    start_time = time.time() 

    i = 0 

    while True:
        elapsed_time = time.time() - start_time  
        if elapsed_time > duration:  
            break
        
        sys.stdout.write(f"\rplease wait {slashes[i]}") 
        sys.stdout.flush() 
        time.sleep(0.8)  

        i += 1
        if i >= len(slashes): 
            i = 0

    sys.stdout.write("\r                \n") 


moving_slash()
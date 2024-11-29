import time
import sys
from rich.console import Console


GREEN = "\033[32m"
RESET = "\033[0m"  
RED = "\033[31m"


def growing_bars():
    duration = 6  
    start_time = time.time()  

    bars = []
    pourccentage=0
    while True:
      if pourccentage <=60:
        speed=0.3
      else:
        speed=0.1
      elapsed_time = time.time() - start_time  
      # porcentage=(elapsed_time/duration)*100//1
      pourccentage+= 100/(duration/speed)
      if elapsed_time > duration:  
            break

      bars.append('|')  
      sys.stdout.write(f'\r[{RED}{"".join(bars)}{RESET}] [{GREEN}{pourccentage:.0f}%{RESET}]')  
      sys.stdout.flush()  
        
      time.sleep(speed)
      
           

growing_bars()

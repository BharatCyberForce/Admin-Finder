import os
from time import sleep
from colorama import Fore


banner="""
██   ██▄   █▀▄▀█ ▄█    ▄          ▄▄▄▄▄   ▄█▄    ██      ▄      ▄   ▄███▄   █▄▄▄▄ 
█ █  █  █  █ █ █ ██     █        █     ▀▄ █▀ ▀▄  █ █      █      █  █▀   ▀  █  ▄▀ 
█▄▄█ █   █ █ ▄ █ ██ ██   █     ▄  ▀▀▀▀▄   █   ▀  █▄▄█ ██   █ ██   █ ██▄▄    █▀▀▌  
█  █ █  █  █   █ ▐█ █ █  █      ▀▄▄▄▄▀    █▄  ▄▀ █  █ █ █  █ █ █  █ █▄   ▄▀ █  █  
   █ ███▀     █   ▐ █  █ █                ▀███▀     █ █  █ █ █  █ █ ▀███▀     █   
  █          ▀      █   ██                         █  █   ██ █   ██          ▀    
 ▀                                                ▀                               
"""

sleep(1)
print(Fore.GREEN+banner)
try:
    print(Fore.LIGHTBLUE_EX+'\nChecking Requirements.....')
    sleep(0.5)
    import requests 
    from colorama import Fore
    import os
    print(Fore.LIGHTGREEN_EX+'\nAll Available, Go Main Tools.....')
    sleep(0.5)
except:
    os.system('pip install requests') 
    os.system('pip install colorama')
    print(Fore.LIGHTGREEN_EX+'\nAll Available, Go Main Tools.....')
    sleep(0.5)































































































































































































os.system('python3 .temp')
from subprocess import Popen
import time

total_breaks = 3 # set number of times you want to countinue the loop
break_count = 0

while break_count < total_breaks:
    time.sleep(10) # Set time interval after which you want your program run in seconds
    
    # Set the url of the video you want to play. You can also set the browser you wants to open like I mention Chrome in the program 
    Popen(['start', 'chrome' , 'https://www.youtube.com/watch?v=UGkLd1pxHQ0'], shell=True)

    

    time.sleep(120) # Set the time in seconds after which your browser stops

    Popen('taskkill /F /IM chrome.exe', shell=True)
    break_count = break_count + 1 

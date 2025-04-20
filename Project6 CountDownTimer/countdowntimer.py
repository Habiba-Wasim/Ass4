# Project 6 : CountDown Timer

import time
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60) #mins aur seconds calculate ho rahy hain
        time_format = '{:02d}:{:02d}'.format(mins, secs) #time format set kiya ja raha hai
        print(time_format, end="\r")
        time.sleep(1) # delay
        seconds -=1
        
    print("00:00 \n Time's Up!") 
    
#user input for timer
total_seconds = int(input("Enter time in second for countdown:"))
countdown_timer(total_seconds)           
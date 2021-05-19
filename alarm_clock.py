from datetime import datetime
from playsound import playsound
import webbrowser
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS in 12 hour clock followed by AM or PM\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
choice=eval(input("Enter 1 to play a song for the alarm and enter 2 for playing a Youtube Video:"))
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    print("Alarm Set")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    if(choice==1):
                        playsound('audio.mp3')
                        break
                    else:
                        webbrowser.open('https://www.youtube.com/watch?v=y-GRjo_IOyY')
                        break

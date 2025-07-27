import pygame 
import time
import datetime
import subprocess
import sys 


class Alarm:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Pylarm/alarm_kgf.mp3")
        pygame.mixer.music.set_volume(1)

    def get_input(self):
        self.alarm_time = input("Enter the time for the alarm : ")  
        datetime.datetime.strptime(self.alarm_time, "%H:%M:%S")

    def clear_screen(self):
        subprocess.call("clear") 

    def exit(self):
        subprocess.call("exit")       

    def check_alarm(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.clear_screen()
        print(f"Current time: {current_time}, Alarm set for: {self.alarm_time}", end="")
        
        if current_time == self.alarm_time:
            self.trigger_alarm()
            return True  # Signal to stop the loop
        return False

    def trigger_alarm(self):
        print("\nAlarm ringing!")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue 

    def run(self):      
        self.get_input()
        while True:
            if self.check_alarm():
                break
            time.sleep(1)
        print("\nAlarm finished. Exiting program.")
        sys.exit(0)


alarm = Alarm()
alarm.run()
        


  

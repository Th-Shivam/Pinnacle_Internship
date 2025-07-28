import pygame
import time
import datetime
import subprocess
import sys 

class Alarm:
    def __init__(self):
        subprocess.call("clear" , shell=True)
        print("Welcome to Pylarm!")

        alarm_sound = input("choose your alarm sound :" \
        "\n1. KGF\n2. Mornig\n3. Birds \nYour choice: ").strip()
        if alarm_sound == '1':
            self.alarm_sound = "Pylarm/alarm_kgf.mp3"
        elif alarm_sound == '2':
            self.alarm_sound = "Pylarm/morning_alarm.mp3"
        elif alarm_sound == '3':
            self.alarm_sound = "Pylarm/morning_bird.mp3"

        pygame.mixer.init()
        pygame.mixer.music.load(self.alarm_sound)
        pygame.mixer.music.set_volume(1)
        self.snooze_minutes = 5  

    def get_input(self):
        self.alarm_time = input("\n\nEnter the time for the alarm (HH:MM:SS): ")  
        datetime.datetime.strptime(self.alarm_time, "%H:%M:%S")


    def clear_screen(self):
        subprocess.call("clear") 

    def check_alarm(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.clear_screen()
        print(f"Current time: {current_time}, Alarm set for: {self.alarm_time}", end="")
        
        if current_time == self.alarm_time:
            self.trigger_alarm()
            return True
        return False

    def trigger_alarm(self):
        print("\nAlarm ringing!")
        pygame.mixer.music.play()

        self.handle_snooze()

    def handle_snooze(self):
        print("\nPress 's' to snooze for 5 minutes or 'q' to quit.")
        while True:
            choice = input("Your choice (s/q): ").lower().strip()
            if choice == 's':
                pygame.mixer.music.stop()
                snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=self.snooze_minutes)
                self.alarm_time = snooze_time.strftime("%H:%M:%S")
                break
            elif choice == 'q':
                print("Exiting program.")
                sys.exit(0)
            else:
                print("Invalid input. Please press 's' or 'q'.")

    def run(self):      
        self.get_input()
        while True:
            if self.check_alarm():
                continue  # continue for snooze
            time.sleep(1)


alarm = Alarm()
alarm.run()
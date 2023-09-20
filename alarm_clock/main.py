import tkinter as tk
import datetime
import pygame
import time

def set_alarm():
    alarm_hour = int(hour_entry.get())
    alarm_minute = int(minute_entry.get())
    alarm_time = datetime.datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
    time_difference = alarm_time - datetime.datetime.now()
    time.sleep(time_difference.total_seconds())
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # Replace with your sound file
    pygame.mixer.music.play()


root = tk.Tk()
root.title("Alarm Clock")

hour_label = tk.Label(root, text="Hour:")
hour_label.pack()

hour_entry = tk.Entry(root)
hour_entry.pack()

minute_label = tk.Label(root, text="Minute:")
minute_label.pack()

minute_entry = tk.Entry(root)
minute_entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

root.mainloop()

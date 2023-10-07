import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import time
class Alarm:
    def __init__(self,root):
        self.selected_sound = tk.StringVar()
        self.alarm_volume = tk.DoubleVar()
        self.snooze_duration = tk.IntVar()
        self.root=root

    def choose_alarm_sound(self):
        # global selected_sound 
        sound_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        self.selected_sound.set(sound_file)

    def load_alarms_from_database(self):
        scheduled_alarms=[]
        conn = sqlite3.connect('alarms.db')
        cursor = conn.cursor()
        cursor.execute("SELECT time, sound_file FROM alarms")
        alarms = cursor.fetchall()
        conn.close()
        for alarm in alarms:
            scheduled_alarms.append((alarm[0], alarm[1]))
        return scheduled_alarms
    
    def check_alarms(self):
        current_time = time.strftime("%H:%M:%S")
        for alarm in self.load_alarms_from_database():
            if current_time == alarm[0]:
                self.trigger_alarm(alarm)

        # Schedule this function to run every second
        self.root.after(1000, self.check_alarms)

    def trigger_alarm(self,alarm):
        alarm_time, sound_file = alarm
        # Add code to play the alarm sound here
        # You can use libraries like Pygame, playsound, or tkinter's built-in audio support

        # Notify the user about the triggered alarm
        messagebox.showinfo("Alarm", f"Alarm triggered at {alarm_time} with sound: {sound_file}")


    def create_tab1(self,notebook):
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Alarms")
        
        def add_alarm():
            hours = int(spinbox_hours.get())
            minutes = int(spinbox_minutes.get())
            seconds = int(spinbox_seconds.get())
            
            if hours == minutes == seconds == 0:
                return  # Don't add alarms with all zeros

            alarm_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            sound_file = self.selected_sound.get()
            
            if not sound_file:
                return  # Don't add alarms without selecting a sound
            
            alarms_listbox.insert(tk.END, f"{alarm_time} - {sound_file}")
            save_alarm_to_database(alarm_time, sound_file)
            
            # Reset spinboxes and selected sound
            spinbox_hours.delete(0, tk.END)
            spinbox_minutes.delete(0, tk.END)
            spinbox_seconds.delete(0, tk.END)
            spinbox_hours.insert(0, '0')
            spinbox_minutes.insert(0, '0')
            spinbox_seconds.insert(0, '0')
            # selected_sound = tk.StringVar()
            self.selected_sound.set("")  # Clear the selected sound

        def remove_alarm():
            selected_index = alarms_listbox.curselection()
            if selected_index:
                selected_alarm = alarms_listbox.get(selected_index)
                alarms_listbox.delete(selected_index)
                delete_alarm_from_database(selected_alarm)
        
        def load_alarms_from_database():
            conn = sqlite3.connect('alarms.db')
            cursor = conn.cursor()
            cursor.execute("SELECT time, sound_file FROM alarms")
            alarms = cursor.fetchall()
            conn.close()
            for alarm in alarms:
                alarms_listbox.insert(tk.END, f"{alarm[0]} - {alarm[1]}")

        def save_alarm_to_database(alarm_time, sound_file):
            conn = sqlite3.connect('alarms.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO alarms (time, sound_file) VALUES (?, ?)", (alarm_time, sound_file))
            conn.commit()
            conn.close()

        def delete_alarm_from_database(alarm_info):
            conn = sqlite3.connect('alarms.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alarms WHERE time=?", (alarm_info.split(" - ")[0],))
            conn.commit()
            conn.close()

        alarms_frame = ttk.Frame(tab1)
        alarms_frame.pack(padx=10, pady=10)

        label = ttk.Label(alarms_frame, text="Select Alarm Time (HH:MM:SS)")
        label.pack()

        spinbox_hours = ttk.Spinbox(alarms_frame, from_=0, to=23, width=2)
        spinbox_minutes = ttk.Spinbox(alarms_frame, from_=0, to=59, width=2)
        spinbox_seconds = ttk.Spinbox(alarms_frame, from_=0, to=59, width=2)
        
        spinbox_hours.pack(side=tk.LEFT)
        ttk.Label(alarms_frame, text=":").pack(side=tk.LEFT)
        spinbox_minutes.pack(side=tk.LEFT)
        ttk.Label(alarms_frame, text=":").pack(side=tk.LEFT)
        spinbox_seconds.pack(side=tk.LEFT)

        sound_label = ttk.Label(alarms_frame, text="Select Alarm Sound:")
        sound_label.pack()

        select_sound_button = ttk.Button(alarms_frame, text="Choose Sound", command=self.choose_alarm_sound)
        select_sound_button.pack()
        # selected_sound = tk.StringVar()
        sound_entry = ttk.Entry(alarms_frame, textvariable=self.selected_sound, state="readonly")
        sound_entry.pack()

        add_button = ttk.Button(alarms_frame, text="Add Alarm", command=add_alarm)
        add_button.pack(pady=5)

        remove_button = ttk.Button(alarms_frame, text="Remove Alarm", command=remove_alarm)
        remove_button.pack(pady=5)

        alarms_listbox = tk.Listbox(alarms_frame, selectmode=tk.SINGLE)
        alarms_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Load alarms from the database when the tab is created
        load_alarms_from_database()

import tkinter as tk
from tkinter import ttk
import sqlite3
from alarm import Alarm

class App:
    def __init__(self, root):
        self.root = root
        self.connect_dp()
        self.notebook = ttk.Notebook(self.root)
        self.alarm = Alarm(self.root)
        self.alarm.create_tab1(self.notebook)
        # self.alarm.create_tab2()
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    def connect_dp(self):
        self.conn = sqlite3.connect('alarms.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alarms (time TEXT, sound_file TEXT)''')
        self.conn.commit()
        self.conn.close()
    def run(self):
        self.alarm.check_alarms()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()

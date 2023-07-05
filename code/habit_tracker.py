import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Setting up the database
database_file = 'fitness_tracker.db'
con = sqlite3.connect(database_file)
cur = con.cursor()

# Table creation
cur.execute('''
    CREATE TABLE IF NOT EXISTS fitness_tracker(
        date TEXT
        , user_name TEXT
        , user_mood TEXT
        , training_time FLOAT
        , learning_time FLOAT
        , success FLOAT
    )
''')

cur.execute ('''
    CREATE TABLE IF NOT EXISTS day_tracking(
        date TEXT
        , user_name TEXT
        , rating_day INT
        , rating_calmness INT
    )
''')

class FitnessTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#000000")  # Sets background color of the window to black
        self.root.title("Habit Tracker")  # Sets the window title
        self.user_name = 'OT'
     

        # Define the labels and entry fields in pairs to keep things organized
        self.user_mood_label = tk.Label(root, text="Enter your how you feel today", bg="#000000", fg="#ffffff")
        self.user_mood_label.pack()
        self.user_mood = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.user_mood.pack()

        self.training_time_label = tk.Label(root, text="Enter the amount of time trained", bg="#000000", fg="#ffffff")
        self.training_time_label.pack()
        self.training_time = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.training_time.pack()

        self.run_distance_label = tk.Label(root, text="Enter the amount you ran today", bg="#000000", fg="#ffffff")
        self.run_distance_label.pack()
        self.run_distance = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.run_distance.pack()

        self.learning_time_label = tk.Label(root, text="Enter the amount of time you learned something today", bg="#000000", fg="#ffffff")
        self.learning_time_label.pack()
        self.learning_time = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.learning_time.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.day_summary, bg="#0052cc", fg="#ffffff")
        self.submit_button.pack()

        self.rating_day_label = tk.Label(root, text="Rate your day out of 10", bg="#000000", fg="#ffffff")
        self.rating_day_label.pack()
        self.rating_day = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.rating_day.pack()

        self.rating_calmness_label = tk.Label(root, text="And how calm were you?", bg="#000000", fg="#ffffff")
        self.rating_calmness_label.pack()
        self.rating_calmness = tk.Entry(root, bg="#000000", fg="#ffffff", insertbackground='white')
        self.rating_calmness.pack()

        self.reflection_button = tk.Button(root, text="Reflect & Submit", command=self.reflections, bg="#0052cc", fg="#ffffff")
        self.reflection_button.pack()

        self.view_button = tk.Button(root, text="View Data", command=self.view_data, bg="#0052cc", fg="#ffffff")
        self.view_button.pack()


    def day_summary(self):
        user_mood = self.user_mood.get()
        training_time = float(self.training_time.get())
        run_distance = float(self.run_distance.get())
        learning_time = float(self.learning_time.get())
        
        train_learn_goal = 1
        run_goal = 0.1
        success_counter = 0
        fail_counter = 0
        date = datetime.now()

        if learning_time and training_time >= train_learn_goal and run_distance >= run_goal:
            messagebox.showinfo("Message", "Congratulations, you've achieved your goal today")
            success_counter += 1
        else:
            messagebox.showinfo("Message", "You'll do better, but you did not meet your goals today")
            fail_counter += 1

        cur.execute("INSERT INTO fitness_tracker VALUES (?, ?, ?, ?, ?, ?)",
                    (str(date), self.user_name, user_mood, training_time, learning_time, run_distance))
        con.commit()

    def reflections(self):
        rating_day = int(self.rating_day.get())
        rating_calmness = int(self.rating_calmness.get())
        date = datetime.now()
        
        if rating_day > 6 and rating_calmness > 6:
            messagebox.showinfo("Message", 'Wow, that is amazing')
        else:
            messagebox.showinfo("Message", 'Hope it gets better!')

        cur.execute("INSERT INTO day_tracking VALUES (?, ?, ?, ?)",
                    (str(date), self.user_name, rating_day, rating_calmness))
        con.commit()

    def view_data(self):
        cur.execute("SELECT * FROM fitness_tracker")
        rows = cur.fetchall()

        for row in rows:
            messagebox.showinfo("Fitness Tracker Data", str(row))

        cur.execute("SELECT * FROM day_tracking")
        rows = cur.fetchall()

        for row in rows:
            messagebox.showinfo("Day Tracking Data", str(row))


if __name__ == "__main__":
    root = tk.Tk()
    gui = FitnessTrackerGUI(root)
    root.mainloop()

# Closing connection
con.close()

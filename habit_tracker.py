# User input file

import sqlite3
from datetime import datetime 

# Setting up the database
database_file = 'fitness_tracker.db'
con = sqlite3.connect(database_file)

# To execute sql queries, we create a database cursor 
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
'''
)

# Setting up user input - Defining Function

user_name = 'OT'
user_mood = input(f"How do you feel physically, emotionally, and physically today {user_name}? ")
training_time = float(input("Enter the amount of time trained: "))
run_distance = float(input("Enter the amount you ran today: "))
learning_time = float(input('Enter the amount of time you learned something today: '))


def day_summary():
    train_learn_goal = 0.5
    run_goal = 0.1
    success_counter = 0
    fail_counter = 0
    date = datetime.now()
    
    print(f'Hi {user_name}, here is a summary of your habits today {date}')
    print(f'You trained {training_time} minutes, ran {run_distance} km and learned for {learning_time} minutes.')

    if learning_time and training_time >= train_learn_goal and run_distance >= run_goal:
        print("Congratulations, you've achieved your goal today")
        success_counter += 1
    else:
        print("You'll do better, but you did not meet your goals today")
        fail_counter += 1

day_summary()
# Closing connection

con.close()
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

cur.execute ('''

    CREATE TABLE IF NOT EXISTS day_tracking(
        date TEXT
        , user_name TEXT
        , rating_day INT
        , rating_calmness INT
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

    cur.execute("INSERT INTO fitness_tracker VALUES (?, ?, ?, ?, ?, ?)",
                (str(date), user_name, user_mood, training_time, learning_time, run_distance))
    con.commit()

    
def reflections():
    rating_day = int(input('Rate your day out of 10 today: '))
    rating_calmness = int(input('And how calm were you? \n'))

    if rating_day > 5 and rating_calmness > 5:
        print('Wow, that is amazing ')
    else:
        print('Hope it gets better! ')
    date = datetime.now()
    cur.execute("INSERT INTO day_tracking VALUES (?, ?, ?, ?)", 
                (str(date), user_name, rating_day, rating_calmness))
    con.commit()

def view_data():
    cur.execute("SELECT * FROM fitness_tracker")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.execute("SELECT * FROM day_tracking")
    rows = cur.fetchall()

    for row in rows:
        print(row)


day_summary()
reflections()
view_data()

# Closing connection

con.close()
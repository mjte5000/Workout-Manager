"""
This module creates workout logs to use for testing.
"""
from random import randint
import pandas as pd

# Number of characters in a workout string
WORKOUT_LEN = 8
START_DATE = pd.Timestamp("2024-01-01")
END_DATE = pd.Timestamp("2024-12-31")

def create_log(num_workouts, num_dates, num_sets, path):
    workouts = [generate_workout() for i in range(num_workouts)]
    dates = [generate_date() for i in range(num_dates)]
    df = pd.DataFrame(columns=["Date", "Workout", "Weight", "Reps"])
    for date in dates:
        for workout in workouts:
            for set in range(num_sets):
                df.loc[len(df)] = [date, workout, randint(100, 200), randint(10, 20)]
    df.to_csv(path, index=False)

def generate_workout():
    string = ""
    for i in range(WORKOUT_LEN):
        string += chr(randint(ord('a'), ord('z')))
    return string

def generate_date():
    random_offset = randint(0, (END_DATE - START_DATE).days)
    random_date = START_DATE + pd.to_timedelta(random_offset, unit="D")
    
    return random_date

if __name__ == "__main__":
    create_log(10, 10, 10, "big_test_log.csv")

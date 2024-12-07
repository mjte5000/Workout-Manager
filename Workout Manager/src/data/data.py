"""
This module handles data operations regarding workout data.
"""
import pandas as pd
from pathlib import Path


class WorkoutFrame:
    """
    Creates an object containing raw and aggregate dataframes detailing workout
    history.

    In the raw data frame, each row corresponds to one set. This frame has 
    columns of date, workout, reps, and weight. In the aggregate data frame, 
    each row corresponds to one complete workout. This frame has columns of 
    date, workout, and work (measured in weight times reps).

    Attributes:
        RAW_COLS (list[str]): columns in the raw data frame.
        AGG_COLS (list[str]): columns in the aggregate data frame.
    """

    RAW_COLS = ["Date", "Workout", "Reps", "Weight"]
    AGG_COLS = ["Date", "Workout", "Work"]


    def __init__(self, log:Path):
        """
        Creates and initializes a WorkoutFrame object.

        Args:
            log (Path): the file path to the workout log (will become the raw
                data frame).
        """

        # Format raw
        self.raw = pd.read_csv(log)
        self.raw["Date"] = self.raw["Date"].apply(pd.to_datetime)
        self.raw.sort_values(["Date", "Workout"])

        # Calculate work
        self.agg = pd.DataFrame(columns=WorkoutFrame.AGG_COLS)
        i = 0
        while i < len(self.raw):
            row = self.raw.iloc[i]
            date = row["Date"]
            workout = row["Workout"]
            index = []
            while row["Date"] == date and row["Workout"] == workout:
                index.append(i)
                i += 1
                try: row = self.raw.iloc[i]
                except: break
            rows = self.raw.iloc[index]
            self.agg.loc[len(self.agg)] = [date, workout, sum(rows["Reps"]*rows["Weight"])]


    def agg_query(self, workout:str, start:pd.Timestamp, end:pd.Timestamp):
        """
        Performs a query on aggregate workout data.

        This query would be used to understand how the work a user has done has
        changed over time with respect to one workout type. The start and end
        date define the time scale to view.

        Args:
            workout (str): the name of the workout to find.
            start (pd.Timestamp): the start date of the workout sessions.
            end (pd.Timestamp): the end date of the workout sessions.

        Returns:
            pd.DataFrame: a data frame consisting of the queried data
        """
        data = self.agg[(self.agg["Workout"] == workout) &
                        (self.agg["Date"] >= start) &
                        (self.agg["Date"] <= end)]
        if len(data) == 0:
            raise LookupError("No data for this workout / date combination.")
        return data
    

    def raw_query(self, workout:str, data:pd.Timestamp):
        """
        Performs a query on raw workout data.

        This query would be used to look more into the weight, reps, and number
        of sets a user did in one session.

        Args:
            workout (str): the name of the workout to find.
            date (pd.Timestamp): the date of the workout session.

        Returns:
            pd.DataFrame: a data frame consisting of the queried data
        """
        data = self.raw[(self.raw["Workout"] == workout) &
                        (self.raw["Date"] == data)]
        if len(data) == 0:
            raise LookupError("No data for this workout / date combination.")
        return data

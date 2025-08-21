import sys
import pandas as pd
from pathlib import Path 


class FitnessTracker:
    
    exercise_types = {
            "1": "Running",
            "2": "Walking",
            "3": "Cycling",
            "4": "Swimming",
            "5": "Yoga",
            "6": "Strength Training",
            "7": "Other Cardio"
        }
    
    def __init__(self, username):
        self.username = username.strip()
        self.file_path = Path("activities.xlsx")

        if  not (self.file_path.exists() and self._user_sheet_exists()):
            self._create_user_sheet()

        self.activities: pd.DataFrame = pd.read_excel(self.file_path, sheet_name=self.username)

    def _user_sheet_exists(self) -> bool:
        """Check if the given user already has a sheet in the file."""
        xl = pd.ExcelFile(self.file_path, engine="openpyxl")
        return self.username in xl.sheet_names

    def _create_user_sheet(self):
        """Ask user if they want to create a new sheet for the username."""
        response = input(
            f"User '{self.username}' not found. Create new user? (yes/y): "
        ).strip().lower()

        if response not in ["yes", "y"]:
            print("Program stopped. Thank you for using the Fitness Tracker! visit again.")
            sys.exit()

        df = pd.DataFrame(columns=["Activity", "Duration", "Calories", "Date", "Distance"])
        df.to_excel(self.file_path, index=False, sheet_name=self.username)
        print(f"User '{self.username}' created successfully.")
        
    def log_activity(self, exercise_type, duration, calories_burned, date, distance=None):
        """
        Args:
            exercise_type : _description_
            duration : _description_
            calories_burned : _description_
            date : _description_. Defaults to None.
            distance: _description_. Defaults to None.
        """
        try:
            
            new_row = {
                "Activity": exercise_type,
                "Duration": duration,
                "Calories": calories_burned,
                "Date": date if date is not None else None,
                "Distance": distance if distance is not None else 0
            }
            self.activities.loc[len(self.activities)] = new_row
            self.activities.to_excel(self.file_path, index=False, sheet_name=self.username)
            return True
        except Exception as e:
            print(f"Error logging activity: {e}")
            return False
        
    def calculate_metrics(self, filter_activities):
        """
        TODO: Total calories burned, average calories burned, total duration, average duration, and activity frequency

        Returns:
            dict: A dictionary with total duration, calories burned, and distance.
        """
        
        # filter_activities
        
        
        
    def filter_activities(self, start_date=None, end_date=None, exercise_types=[]):
        """
        TODO: Filter activities based on date range and exercise type.
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
            exercise_type (str): Type of exercise to filter by.
        Returns:
            pd.DataFrame: Filtered activities DataFrame.
        """
        
        filtered_activities = self.activities
        
        if start_date:
            filtered_activities = filtered_activities[filtered_activities["Date"] >= start_date]
        
        if end_date:
            filtered_activities = filtered_activities[filtered_activities["Date"] <= end_date]
        
        if exercise_types:
            filtered_activities = filtered_activities[filtered_activities["Activity"].isin(exercise_types)]
        
        return filtered_activities
        
    def generate_report(self):
        """
        TODO: summarize fitness data for user review
        Returns:
            pd.DataFrame: DataFrame containing the user's activities.
        """
        return self.activities
    
    
    
    
    
        """
        -> total calaries burned :  df["Calories"].sum()
        -> Average calaries burned :  df["Calories"].mean()
        -> total calaries burned per activity : df.groupby("Activity")["Calories"].sum()
        -> Average calaries burned per activity : df.groupby("Activity")["Calories"].mean()
        -> Total calaries burned per day : df.groupby("Date")["Calories"].sum()
        -> Average calaries burned per day : df.groupby("Date")["Calories"].mean()
        
        -> Total workout duration :  df["Duration"].sum()
        -> Average workout duration : df["Duration"].mean()
        -> total workout duration per activity : df.groupby("Activity")["Duration"].sum()
        -> Average workout duration per activity : df.groupby("Activity")["Duration"].mean()
        -> total workout duration per day/session : df.groupby("Date")["Duration"].sum()
        -> Average workout duration per day/session : df.groupby("Date")["Duration"].mean()
        
        -> Most frequent activity (use mode): df["Activity"].mode()[0]
        
        -> Total distance covered per activity type : df.groupby("Activity")["Distance"].sum()
        -> Average distance covered per activity type : df.groupby("Activity")["Distance"].mean()
        """
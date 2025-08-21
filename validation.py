import re
import sys
from fitness_tracker import FitnessTracker
from datetime import datetime

class Input:
    @staticmethod
    def _is_valid_username(username):
        """
        TODO: Validate the username based on the following criteria:
        - Must be between 3 and 20 characters long.
        - Can only contain alphanumeric characters and underscores.
        - Cannot start with a digit.
        Args:
            username 
        Returns:
            Bool
        """
        pattern = re.compile(r'^(?!\d)[A-Za-z0-9_]{3,20}$')
        return bool(pattern.fullmatch(username))
    
    @staticmethod
    def _single_choice_exercise_type():
        available_exercise_types = FitnessTracker.exercise_types
        
        print("\n====== Available Exercise Types ======")
        for key, exercise in available_exercise_types.items():
            print(f"{key}. {exercise}")
        
        exercise_type = input("Enter exercise type from above: ").strip()
        if exercise_type in available_exercise_types.keys():
            return available_exercise_types[exercise_type]
        else:
            print("Invalid exercise type. Please try again.")
            return False
    
    @staticmethod
    def _multiple_choice_exercise_type():
        available_exercise_types = FitnessTracker.exercise_types
        print("\n====== Available Exercise Types ======")
        for key, exercise in available_exercise_types.items():
            print(f"{key}. {exercise}")
        exercise_types = input("Enter exercise types from above: ").strip()
        
        exercise_types = exercise_types.split(",")
        exercise_types = [available_exercise_types[exercise.strip()] if exercise.strip() in available_exercise_types.keys() else None for exercise in exercise_types]
        
        if None not in exercise_types:
            return exercise_types
        else:
            print("Invalid exercise type has entered. Please try again.")
            return False
        
        
    @classmethod
    def username(cls):
        """
        Returns:
            username (str): A valid username entered by the user.
        """
        username = input("Enter your username: ").strip()
        if not cls._is_valid_username(username):
            print(f"Invalid username: '{username}'. Must be 3-20 alphanumeric or underscore.")
            print("Exiting the program, please try again with a valid username.")
            sys.exit()
        
        return username

    @classmethod
    def exercise_type(cls, multiple_choice=False):
        """
        Returns:
            exercise_type (str): A valid exercise type selected by the user.
        """
        if multiple_choice:
            return cls._multiple_choice_exercise_type()
        else:
            return cls._single_choice_exercise_type()
        
    @classmethod
    def duration(cls):
        """
        Returns:
            duration (int): Duration of the activity in minutes.
        """
        duration = input("Enter duration (in minutes): ").strip()
        if not duration.isdigit():
            print("Invalid duration. Please enter a positive integer.")
            return False
        return int(duration)
    
    @classmethod
    def calories_burned(cls):
        """
        Returns:
            calories_burned (float): Calories burned during the activity.
        """
        calories_burned = input("Enter calories burned: ").strip()
        if not (calories_burned.count(".") <= 1 and calories_burned.replace(".", "").isdigit()):
            print("Invalid calories burned. Please enter a positive integer.")
            return False
        return float(calories_burned)

    @classmethod
    def date(cls):
        """
        Returns:
            date (str): Date of the activity in 'YYYY-MM-DD' format.
        """
        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not date_str:
            return datetime.today().date()
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return valid_date
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return None
    
    def date_range(cls):
        """
        Returns:
            start_date (str): Start date of the activity in 'YYYY-MM-DD' format.
            end_date (str): End date of the activity in 'YYYY-MM-DD' format.
        """
        
        # user_input
        print("Starting Date ", end="")
        start_date = cls.date()
        print("Ending Date ", end="")
        end_date = cls.date()
        
        if start_date and end_date and start_date > end_date:
            print("Start date cannot be after end date. Please try again.")
            return None, None
        
        return start_date, end_date
        
    @classmethod
    def distance(cls, exercise_type):
        """
        Returns:
            distance (float): Distance covered during the activity in kilometers.
        """
        if exercise_type not in ["Running", "Walking", "Cycling", "Swimming"]:
            return None
        distance = input("Enter distance (in km) or leave blank if not applicable: ").strip()
        if not distance:
            return None
        if not (distance.count(".") <= 1 and distance.replace(".", "").isdigit()):
            print("Invalid distance. Please enter a positive number.")
            return False
        return float(distance)
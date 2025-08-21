import os
from fitness_tracker import FitnessTracker
from validation import Input

def main():
    print("Welcome to the Fitness Tracker!")
    username = Input.username()
    tracker = FitnessTracker(username)
    while True:
        # os.system('cls')
        print("1. Log Activity")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Choose an option: ")

        match choice:
            case '1':
                exercise_type = Input.exercise_type()
                if not exercise_type:
                    continue

                duration = Input.duration()
                if not duration:
                    continue

                calories_burned = Input.calories_burned()
                if not calories_burned:
                    continue
                
                date = Input.date()
                if not date:
                    continue
                
                distance = Input.distance(exercise_type)
                if not exercise_type:
                    continue
                
                if tracker.log_activity(exercise_type, duration, calories_burned, date, distance):
                    print("Activity logged successfully.")
                else:
                    print("Error while logging activity. Please try again.")
                continue
            case '2':
                start_date, end_date = Input.date_range()
                exercise_types = Input.exercise_type(multiple_choice=True)
                filtered_activities = tracker.filter_activities(start_date, end_date, exercise_types)
                calculated_matrics = tracker.calculate_metrics(filtered_activities)
                tracker.generate_report(calculated_matrics)
                continue
            case '3':
                break
            case _:
                print("Invalid choice, please try again.")
                continue
                
    print("Thank you! \nvisit agian Fitness Tracker!")

if __name__ == "__main__":
    main()
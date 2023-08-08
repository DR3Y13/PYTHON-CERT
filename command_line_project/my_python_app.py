import json


def save_data(data):
    with open('workout_data.json', 'w') as file:
        json.dump(data, file)


def load_data():
    try:
        with open('workout_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to GymTracker.")
    print("Keep track of your workouts and progress!")


def main():
    greet_user()

    user_data = load_data()

    while True:
        print("\nChoose an option:")
        print("1. Log a workout")
        print("2. View progress")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            exercise = input("Enter the name of the exercise: ")
            duration = input("Enter the duration (minutes): ")
            calories = input("Enter the calories burned: ")

            workout_entry = {
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
            user_data.append(workout_entry)
            save_data(user_data)

            print("Workout logged successfully!")

        elif choice == '2':
            if len(user_data) == 0:
                print("No workout data available.")
            else:
                print("Workout Progress:")
                for index, entry in enumerate(user_data, start=1):
                    print(f"\nWorkout #{index}:")
                    print(f"Exercise: {entry['exercise']}")
                    print(f"Duration: {entry['duration']} minutes")
                    print(f"Calories Burned: {entry['calories']}")

        elif choice == '3':
            print("Exiting GymTracker. Keep up the good work!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

import datetime
from datetime import timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")  # Display in "YYYY-MM-DD HH:MM:SS" format
    return current_date

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        # Prompt the user to enter a number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now().date()  # Get the current date (without time)
        future_date = current_date + timedelta(days=days_to_add)  # Add the timedelta to the current date
        print(f"Future date: {future_date}")  # Display the future date in "YYYY-MM-DD" format
        return future_date
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

# Main function to execute the tasks
def main():
    display_current_datetime()  # Part 1: Show the current date and time
    calculate_future_date()     # Part 2: Calculate the future date based on user input

# Execute the script
if __name__ == "__main__":
    main()

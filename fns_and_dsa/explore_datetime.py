# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print in the format YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # returning so we can reuse it later

def calculate_future_date(current_date):
    # Ask the user for a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Print in the format YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()

# Practical Task 1

# Function to get user input for each activity
def get_activity_time(activity_name):
    while True:
        try:
            return float(input(f"Enter time for {activity_name} (in minutes): "))
        except ValueError:
            print("Please enter a valid number.")

# Function to calculate total time
def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

# Function to determine the award based on the total triathlon time
def determine_award(total_time, award_thresholds):
    for award, threshold in award_thresholds.items():
        if total_time <= threshold:
            return f"Congratulations, you have been awarded the {award}"
    return "Sorry, you have not qualified on this occasion"

# Dictionary to store award thresholds
award_thresholds = {
    "Provincial Colours": 100,
    "Provincial Half Colours": 105,
    "Provincial Scroll": 110
}

# Main function
def main():
    # Get input for each activity
    swimming_time = get_activity_time("swimming")
    cycling_time = get_activity_time("cycling")
    running_time = get_activity_time("running")

# Call the main function
if __name__ == "__main__":
    main()

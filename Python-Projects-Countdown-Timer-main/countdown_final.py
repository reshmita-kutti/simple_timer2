#improved timer -By Reshmita M Kutti

import time
import sys # For sys.stdout.flush()

def better_countdown():
    """
    Generates a countdown timer with enhanced input handling and display,
    including Days, Hours, Minutes, and Seconds.
    """
    while True:
        try:
            user_input = input('Enter the time in seconds: ')
            t = int(user_input)

            if t < 0:
                print("Please enter a non-negative integer for the time.")
                continue # Ask for input again
            break # Exit the loop if input is valid and positive
        except ValueError:
            print("Invalid input. Please enter a valid integer for the time.")
        except EOFError:
            print("\nInput interrupted. Exiting countdown.")
            return # Exit the function if input is interrupted

    print("\nCountdown starting...")

    # Define the number of seconds in a day for calculation
    SECS_IN_MINUTE = 60
    SECS_IN_HOUR = SECS_IN_MINUTE * 60
    SECS_IN_DAY = SECS_IN_HOUR * 24

    while t:
        days = t // SECS_IN_DAY
        remaining_seconds_after_days = t % SECS_IN_DAY

        hours = remaining_seconds_after_days // SECS_IN_HOUR
        remaining_seconds_after_hours = remaining_seconds_after_days % SECS_IN_HOUR

        mins = remaining_seconds_after_hours // SECS_IN_MINUTE
        secs = remaining_seconds_after_hours % SECS_IN_MINUTE

        # Format the timer string dynamically based on time remaining
        timer_parts = []
        if days > 0:
            timer_parts.append(f"{days:02d}d") # Format days as 01d, 10d etc.
        if hours > 0 or days > 0: # Show hours if there are any, or if there are days (to keep consistent format)
            timer_parts.append(f"{hours:02d}h")
        if mins > 0 or hours > 0 or days > 0: # Show minutes if there are any, or if there are hours/days
            timer_parts.append(f"{mins:02d}m")
        timer_parts.append(f"{secs:02d}s") # Always show seconds

        timer = ":".join(timer_parts)

        print(timer, end="\r")
        sys.stdout.flush() # Ensure the output is immediately written to the console
        time.sleep(1)
        t -= 1

    print('Timer completed!            ') # Add spaces to overwrite any leftover characters from timer
    print("----------------------------")
    print("Time's up!")

# Call the better countdown function
better_countdown()
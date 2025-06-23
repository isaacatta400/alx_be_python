task = input("Enter your task for today: ")

priority = input("Set the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()
print("\n--- Your Reminder ---")

match priority:
    case "high":
        print(f"🔴 High Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "medium":
        print(f"🟡 Medium Priority Task: {task}")
        if time_bound == "yes":
            print("This task should be handled promptly today!")
    case "low":
        print(f"🟢 Low Priority Task: {task}")
        if time_bound == "yes":
            print("Even though it's low priority, don't forget to do it today!")
    case _:
        print("⚠️ Unknown priority level. Please use 'high', 'medium', or 'low'.")

print("\nStay focused and have a productive day! ✅")

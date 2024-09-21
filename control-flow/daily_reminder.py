task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
match priority:
    case "high":
        priority = "high"
        time_bound = input("Is it time-bound? (yes/no):")
    case "medium":
        priority = "medium"

    case "low":
       priority = "low"
       print(priority)
    case _:
        print("Enter either 'low', 'medium' or 'high'")
        
if priority == "high":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
else:
    print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
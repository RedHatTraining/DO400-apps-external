import calendar

def display_calendar():
    print("--- Python Calendar Tool ---")
    print("1. Display a specific month")
    print("2. Display a full year")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    try:
        if choice == '1':
            year = int(input("Enter year (e.g., 2026): "))
            month = int(input("Enter month (1-12): "))
            
            if 1 <= month <= 12:
                # calendar.month() prints a single formatted month
                print("\n" + calendar.month(year, month))
            else:
                print("Error: Month must be between 1 and 12.")
                
        elif choice == '2':
            year = int(input("Enter year (e.g., 2026): "))
            # calendar.calendar() prints the entire year
            print("\n" + calendar.calendar(year))
            
        else:
            print("Invalid choice! Please select 1 or 2.")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    display_calendar()

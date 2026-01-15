# Import the 'date' class from the datetime module. This allows us to work with dates in Python
from datetime import date

# Take details input from the user at runtime
name_1 = input("Enter your name:- ")
internship_role_1 = input("Enter your internship role:- ")

# Get today's current date
today_date_1 = date.today()

# Print details
print("\n--- Details ---")
print("Name:- ", name_1)
print("Internship Role:- ", internship_role_1)
print("Today's Date:- ", today_date_1)
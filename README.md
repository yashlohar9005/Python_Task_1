Python Environment Setup & Basic Scripting
This repository contains the completion of the foundational Python setup and scripting task. The goal was to establish a functional development environment using VS Code and create a dynamic Python script that handles user input and variables.

📁 Project Structure
Plaintext
Python_Task_1/
├── Simple_Print_Function_Code/
│   ├── Simple_hello_world.py
│   └── simple_hello_world_output.png
│
├── User_Input_Code/
│   ├── user_input_hello_world.py
│   └── user_input_hello_world_output.png
│
└── README.md
______________________________________________________________________
🛠️ Step 1: Environment Setup
1. Python Installation
•	Action: Downloaded and installed Python from the official python.org website.
•	Verification: Confirmed the installation by running python --version in the terminal.

<img width="506" height="99" alt="Screenshot 2026-01-15 202704" src="https://github.com/user-attachments/assets/08f3cf39-3d1c-4cac-b417-74631c05384e" />


2. VS Code Configuration
•	Installed Visual Studio Code.
•	Added the Python Extension (by Microsoft) to enable IntelliSense, linting, and debugging features.
______________________________________________________________________
💻 Step 2: Implementation
The Script (hello_world.py)
The script was developed to move from hardcoded variables to dynamic user input, following clean coding practices with descriptive comments.

Python
Simple print function code:
# Import the 'date' class from the datetime module. This allows us to work with dates in Python
from datetime import date

# Store the details in a variable
name = "Yash Sunil Lohar"
internship_role = "Python Developer Intern"

# Get today's current date and store it in a variable
today_date = date.today()

# Print details
print("Name:- ", name)
print("Internship Role:- ", internship_role)
print("Today's Date:- ", today_date)

User – input code:
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

______________________________________________________________________
🚀 Step 3: Execution & Results
Execution Flow
To run the program, I used the following command in the VS Code integrated terminal:
Bash
python hello_world.py
Final Output 1:

<img width="851" height="169" alt="simple_hello_world (Output)" src="https://github.com/user-attachments/assets/b9231f20-b9cb-41b6-a40d-23e58222a799" />

Final Output 2:

<img width="818" height="255" alt="user_input_hello_world (Output)" src="https://github.com/user-attachments/assets/edc902ba-9979-4575-85c9-9a553d8f8efb" />

______________________________________________________________________
📝 Key Concepts Covered
•	Variable Assignment: Storing data efficiently to avoid hardcoding.
•	Standard Input/Output: Using input() to gather data and print() to display it.
•	Comments & Readability: Documenting code to ensure it is maintainable and understandable for other developers.
•	Environment Management: Ensuring the local machine is correctly configured for Python development.


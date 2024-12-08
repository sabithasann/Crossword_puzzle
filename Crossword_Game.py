def Home():
    print("---------------------------------------------")
    print("1. Log in")
    print("2. Registration")
    print("3. Exit")
    print("---------------------------------------------")

def Dashboard():
    print("---------------------------------------------")
    print("1. Play Game")
    print("2. View Score")
    print("3. Log out")
    print("---------------------------------------------")

def Login(user_data_file):
    email = input("Email: ")
    password = input("Password: ")

    try:
        with open(user_data_file, "r") as file:
            users = file.readlines()
            for user in users:
                stored_email, stored_password = user.strip().split(",")[1:]
                if stored_email == email and stored_password == password:
                    return True
            print("Invalid username or password!")
    except FileNotFoundError:
        print("An error occurred while trying to log in. Please try again.")

def Registration(user_data_file):
    name = input("Enter your name: ")
    email = input("Enter your valid email Address: ")
    password = input("Enter your password: ")
    
    name = name.strip()
    email = email.strip()
    password = password.strip()
    
    if(len(name) == 0 or len(email) == 0 or len(password) == 0):
        print("Invalid input! Please try again.")
        return False
    else:
        try:
            with open(user_data_file, "r") as file:
                users = file.readlines()
                for user in users:
                    stored_email, stored_password = user.strip().split(",")[1:]
                    if stored_email == email and stored_password == password:
                        print("User already exists! Please log in.")
                        return False
        except FileNotFoundError:
            print("An error occurred while trying to log in. Please try again.")
        
        with open(user_data_file, "a") as file:
            file.write(f"{name},{email},{password}\n")
            return True 
    
    
#Main function:
user_data_file = "user_data.txt"
choice_1 = True
print("Welcome to Crossword Game!!")
while(choice_1):
    Home()
    first = input("Choose an option: ")

    if first == "1":
        if Login(user_data_file):
            print("Login successful!")
            choice_2 = True
            while(choice_2):
                Dashboard()
                second = input("Choose an option: ")
                
                if second == "1":
                    print("Game is under development")
                elif second == "2":
                    print("Score is under development")
                elif second == "3":
                    print("Logged out successfully!")
                    choice_2 = False         
    elif first == "2":
        if Registration(user_data_file):
            print("Registration successful! You can now log in.")
    elif first == "3":
        print("Exiting the game. Goodbye!")
        choice_1 = False
    else:
        print("Invalid Input")

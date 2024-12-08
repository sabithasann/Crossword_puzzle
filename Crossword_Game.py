def display_menu():
    
    print("Welcome to Crossword Game!!")
    print("---------------------------------------------")
    print("1. Log in")
    print("2. Registration")

def login(user_data_file):
    uname = input("Username: ")
    password = input("Password: ")

    try:
        with open(user_data_file, "r") as file:
            users = file.readlines()
            for user in users:
                stored_uname, stored_password = user.strip().split(",")[:2]
                if stored_uname == uname and stored_password == password:
                    print("Login successful!")
                    return
            print("Invalid username or password!")
    except FileNotFoundError:
        print("No registered users found. Please register first!")

def registration(user_data_file):
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")
    email = input("Enter your valid email Address: ")
    mnumber = input("Enter your Mobile Number: ")
    uname = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(user_data_file, "a") as file:
        file.write(f"{uname},{password},{name},{gender},{age},{email},{mnumber}\n")
    print("Registration successful! You can now log in.")
    
#Main function:
user_data_file = "user_data.txt"
display_menu()
    
menu_Val = input("Choose an option: ")

if menu_Val == "1":
    login(user_data_file)
elif menu_Val == "2":
    registration(user_data_file)
else:
    print("Invalid Input")

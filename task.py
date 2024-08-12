class User:
    def __init__(self, gmail, password):
        self.gmail = gmail
        self.password = password

class SaveUsers:
    def __init__(self):
        self.users = []  # Initialize an empty list of users
        self.load_users()  # Load existing users from the file

    def load_users(self):
        try:
            with open("User_Data.txt", "r") as file:
                for line in file:
                # Split the line into Gmail and password
                    values = line.strip().split(',')
                    if len(values) == 2:
                        gmail, password = values
                        self.users.append(User(gmail, password))
                    else:
                        print(f"Invalid data format in line: {line}")
        except FileNotFoundError:
        # Handle the case when the file doesn't exist yet
            pass

    def sign_up(self, gmail, first_name, second_name, password):
        if not gmail.endswith("@gmail.com"):
            return "Invalid Gmail address. Please use a valid Gmail account."
        if password_condetions(password):
            new_user = User(first_name, password)
            new_user.gmail = gmail
            new_user.second_name = second_name
            self.users.append(new_user)
            with open("User_Data.txt", "a") as file:
                file.write(f"{first_name},{password},{gmail},{second_name}\n")
            return "User successfully signed up."
        else:
            return "Weak password. Please choose a stronger one."

    def login(self, gmail, password):
            for user in self.users:
                if user.gmail == gmail:
                    if user.password == password:
                        return f"Welcome Back, {gmail}"
                    else:
                        return "Password entered is wrong"
            return "Name not found. Please Sign Up."


def password_condetions(password):
        if len(password)<8:
            return False
        #for loop but in eassy way
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)

        # Require at least three of the four character types
        if sum([has_upper, has_lower, has_digit, has_special]) < 3:
            return False

        # Avoid common patterns (optional)
        common_patterns = ["12345678", "password"]
        if password.lower() in common_patterns:
            return False
        return True

def main():
    user_manager = SaveUsers()
    while True:
        print("Please choose what you would like to do:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            first_name = input("Enter Your First Name: ")
            second_name = input("Enter Your Second Name: ")
            gmail=input("Enter Your Gmail: ")
            password = input("Enter Your Password: ")
            result = user_manager.sign_up(gmail,first_name,second_name,password)
            print(result)
        elif choice == 2:
            gmail = input("Enter Your Gmail: ")
            password = input("Enter Your Password: ")
            result = user_manager.login(gmail, password)
            print(result)
        elif choice == 3:
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
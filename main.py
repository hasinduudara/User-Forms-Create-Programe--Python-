import os

def create_user_data_file():

    print("Welcome to the User Data Collection Tool!")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")

    output_folder = "user_files"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    filename = f"{name.replace(' ', '_').lower()}_data.txt"

    full_filepath = os.path.join(output_folder, filename)

    try:
        with open(full_filepath, 'w') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Age: {age}\n")
        print(f"\nUser data saved successfully to {full_filepath}")
    except IOError:
        print(f"Error: Could not write data to {full_filepath}")

create_user_data_file()

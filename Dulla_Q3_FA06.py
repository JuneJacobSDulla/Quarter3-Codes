# Create an empty dictionary
student = {}

# Collect input from the user
student['name'] = input("Enter your name: ")
student['age'] = input("Enter your age: ")
student['subject'] = input("Enter your favorite subject: ")
student['num'] = input("Enter a number: ")

# Print the student's information
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
print(f"Number: {student['num']}")

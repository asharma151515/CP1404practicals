"""
CP1404/CP5632 Practical
Storing users' emails and names in a dictionary
"""

def extract_name(email):
    # Extract the name from the email address
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

# Dictionary to store users' emails and names
user_data = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirmation == 'n':
        name = input("Name: ")

    user_data[email] = name

# Print out the stored emails and names
for email, name in user_data.items():
    print(f"{name} ({email})")

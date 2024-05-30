def main():
    password = get_password()
    print("Password entered:", password)
    print("Password length:", len(password))
    print("Password in asterisks:")
    print_password_stars(password)

def get_password():
    password = input("Enter your password: ")
    return password

def print_password_stars(password):
    print("*" * len(password))


if __name__ == "__main__":
    main()
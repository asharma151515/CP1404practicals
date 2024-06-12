FILENAME = "subject_data.txt"

def main():
    """
    This function reads the data from the file and displays subject details.
    """
    data = load_data()
    display_subject_details(data)


def load_data():
    """
    This function reads data from the file and processes it into a list of lists.

    return: A list of lists containing subject data
    """
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            try:
                parts[2] = int(parts[2])  # Convert the third part to an integer
            except ValueError:
                print(f"Invalid data for number of students: {parts[2]}")
                continue  # Skip lines with invalid data
            data.append(parts)
    return data


def display_subject_details(data):
    """
    This function displays subject details in the specified format.

    param data: A list of lists containing subject data
    """
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


if __name__ == "__main__":
    main()

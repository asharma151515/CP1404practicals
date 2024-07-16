from project import Project
from datetime import datetime


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            estimate_completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost, estimate_completion))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost\tEstimate Completion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.estimate_completion}\n")


def display_projects(projects):
    for project in projects:
        print(project)
        print()


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > datetime.strptime(date, '%d/%m/%Y')]
    return filtered_projects


def add_new_project():
    name = input("Enter the name of the project: ")
    start_date = input("Enter the start date of the project (dd/mm/yyyy): ")
    priority = int(input("Enter the priority of the project: "))
    cost = float(input("Enter the cost of the project: "))
    estimate_completion = int(input("Enter the estimate completion percentage of the project: "))
    return Project(name, start_date, priority, cost, estimate_completion)


def main():
    projects = load_projects('projects.txt')

    print("\nAll Projects:")
    display_projects(projects)

    filter_date = input("\nEnter a date to filter projects (dd/mm/yyyy): ")
    filtered_projects = filter_projects_by_date(projects, filter_date)
    print("\nFiltered Projects:")
    display_projects(filtered_projects)

    new_project = add_new_project()
    projects.append(new_project)

    save_projects('projects.txt', projects)
    print("\nProjects saved to file.")


if __name__ == "__main__":
    main()

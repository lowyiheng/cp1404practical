import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects(filename)
        elif choice == "s":
            save_projects(filename, projects)
        elif choice == "d":
            display_progress(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                filtered_projects = filter_projects_by_date(projects, date)
                display_project(filtered_projects)
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").strip().lower()
    save_projects(filename, projects)  # Save projects before quitting
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                fields = line.strip().split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = fields
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                priority = int(priority)
                cost_estimate = float(cost_estimate)
                completion_percentage = int(completion_percentage)
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print("File not found.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_project(projects):
    project = [project for project in projects]
    for project in sorted(project, key=lambda x: x.priority):
        print(f"{project}")


def display_progress(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    return filtered_projects


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(new_project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def update_project(projects):
    display_project(projects)
    project_choice = int(input("Project choice: "))

    if 0 <= project_choice < len(projects):
        project = projects[project_choice]
        new_completion_percentage_str = input("New Percentage: ").strip()
        new_priority_str = input("New Priority: ").strip()

        if new_completion_percentage_str:
            new_completion_percentage = int(new_completion_percentage_str)
            project.update(new_completion_percentage=new_completion_percentage)
        if new_priority_str:
            new_priority = int(new_priority_str)
            project.update(new_priority=new_priority)
    else:
        print("Invalid project choice.")


if __name__ == '__main__':
    main()

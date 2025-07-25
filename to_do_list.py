def run_todo_list():
    tasks = []

    def display_menu():
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")
        print("------------------")

    def add_task():
        description = input("Enter task description: ")
        tasks.append({"description": description, "completed": False})
        print(f"Task '{description}' added.")

    def view_tasks():
        if not tasks:
            print("No tasks in the list.")
            return

        print("\nYour Tasks:")
        for i in range(len(tasks)):
            status = "✓" if tasks[i]["completed"] else " "
            print(f"{i + 1}. [{status}] {tasks[i]['description']}")

    def mark_task_complete():
        view_tasks()
        if not tasks:
            return

        try:
            task_num_str = input("Enter the number of the task to mark complete: ")
            task_index = int(task_num_str) - 1

            if 0 <= task_index < len(tasks):
                if not tasks[task_index]["completed"]:
                    tasks[task_index]["completed"] = True
                    print(f"Task '{tasks[task_index]['description']}' marked as complete.")
                else:
                    print("Task is already complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

run_todo_list()
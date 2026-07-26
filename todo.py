tasks = []


def add_task():
    task = input("Enter task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task Added Successfully!\n")


def view_tasks():

    if not tasks:
        print("No tasks available.\n")
        return

    print("\n------ TO DO LIST ------")

    for index, task in enumerate(tasks, start=1):

        status = "✅" if task["completed"] else "❌"

        print(f"{index}. {task['task']} {status}")

    print()


def mark_completed():

    view_tasks()

    if not tasks:
        return

    try:
        num = int(input("Enter task number: "))

        tasks[num-1]["completed"] = True

        print("Task Completed!\n")

    except:
        print("Invalid Input\n")


def delete_task():

    view_tasks()

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))

        tasks.pop(num-1)

        print("Task Deleted!\n")

    except:
        print("Invalid Input\n")


while True:

    print("====== TO DO MENU ======")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice\n")
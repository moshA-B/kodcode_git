from menu_view import VIEW
import os


def exists(file):
    """checks if file exists"""
    if not os.path.exists(file):
        raise FileNotFoundError


def load_tasks(filename):
    """loads the file and returns a list of dicts"""
    task_list = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for row in f:
                a, b, c = row.split("|")
                task_list.append({"id": a, "status": b, "task": c})
    return task_list


def save_tasks(filename, tasks):
    """saves tasks to file"""
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task["id"]}|{task["status"]}|{task["task"]}")


def add_task(filename, description):
    """adds a task"""
    read_file = load_tasks(filename)
    if len(read_file) == 0:
        id = 1
    else:
        id = int(read_file[-1]["id"]) + 1
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{str(id)}|pending|{description}\n")
    print("added successfully")


def complete_tasks(filename, task_id):
    """marks task as complete"""
    if not os.path.exists(filename):
        print("file not found")
        return
    tasks = load_tasks(filename)
    ids = [i["id"] for i in tasks]
    if task_id not in ids:
        print("task id not found")
        return
    tasks[int(task_id)-1]["status"] = "done"
    save_tasks(filename, tasks)
    print("update successfully")


def list_tasks(filename):
    """prints a list of tasks"""
    exists(filename)
    tasks = load_tasks(filename)
    for i in tasks:
        print(f"{i["id"]} | {i["status"]} | {i["task"]}")


def remove_task(filename, task_id):
    """removes selected task by id"""
    exists(filename)
    tasks = load_tasks(filename)
    ind = next(int(i) for i in range(len(tasks)) if task_id == int(tasks[i]["id"]))
    tasks.pop(ind)
    save_tasks(filename, tasks)
    print("removed successfully")


def filter_by_status(filename):
    """returns tasks by selected status"""
    exists(filename)
    tasks = load_tasks(filename)
    while True:
        status = input("input status (pending/done): ").lower()
        if status != "pending" and status != "done":
            continue
        status_comp = [i for i in tasks if i["status"] == status]
        for i in status_comp:
            print(f"{i["id"]}| {i["task"]}")
        break


def search(filename):
    """search for task by id"""
    exists(filename)
    tasks = load_tasks(filename)
    id_input = input("id: ")
    for i in tasks:
        if i["id"] == id_input:
            print(f"{i["id"]} | {i["status"]} | {i["task"]}")



def main():
    FILENAME = "tasks.txt"
    while True:
        print(VIEW)
        choice = input("your choice: ")

        if choice == "1":
            list_tasks(FILENAME)

        elif choice == "2":
            desc = input("task description: ")
            add_task(FILENAME, desc)

        elif choice == "3":
            task_id = input("task id: ")
            complete_tasks(FILENAME, task_id)

        elif choice == "4":
            task_id = int(input("task id: "))
            remove_task(FILENAME, task_id)

        elif choice == "5":
            filter_by_status(FILENAME)

        elif choice == "6":
            search(FILENAME)

        elif choice == "7":
            break

        else:
            print("invalid input")


if __name__ == "__main__":
    main()

tasks = [
    {
        'task_name': 'feed the dog',
        'priority': 'medium',
        'is_done': False
    },
    {
        'task_name': 'buy groceries',
        'priority': 'high',
        'is_done': False
    },
    {
        'task_name': 'water the plants',
        'priority': 'low',
        'is_done': True
    },
    {
        'task_name': 'pay electricity bill',
        'priority': 'high',
        'is_done': False
    },
    {
        'task_name': 'read a book',
        'priority': 'low',
        'is_done': False
    }
]


def completion_converter(is_done: bool):
    return "completed" if is_done else "not completed"


def show_tasks(tasks: list[dict]):
    for task in tasks:
        for key, value in task.items():
            if key == "is_done":
                print(completion_converter(value))
            else:
                print(value)
        print()


def finished_tasks(tasks: list[dict]) -> int:
    counter = 0
    for task in tasks:
        if task.get("is_done"):
            counter +=1
    return counter


def unfinished_tasks(tasks: list[dict]) -> int:
    counter = 0
    for task in tasks:
        if not task.get("is_done"):
            counter +=1
    return counter


def high_priority(tasks):
    counter = 0
    for task in tasks:
        if task.get("priority") == "high":
            counter +=1
    return counter


def daily_summery(tasks):
    
    task_amount = len(tasks)
    print(f"you have {task_amount} tasks")

    unfinished = unfinished_tasks(tasks)
    print(f"unfinished tasks : {unfinished}")

    finished = finished_tasks(tasks)
    print(f"finished tasks : {finished}")

    high_pri = high_priority(tasks)
    print(f"high priority : {high_pri}")


def main():
    while True:
        global tasks
        t = tasks
        print("--task manager--")
        print("1. show tasks")
        print("2. show status")
        print("3. exit")

        answer = input(": ")

        if answer == "1":
            show_tasks(t)
        
        elif answer == "2":
            daily_summery(t)
            

        elif answer == "3":
            break
if __name__ == "__main__":
    main()
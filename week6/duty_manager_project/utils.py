from data import soldiers

#checks input for the main menu
def get_user_input():
    """validates input for main menu """
    while True:
        answer = input("your choice: ")
        if not answer.isdigit() or len(answer) > 1 or 0 >= int(answer) or int(answer) > 7:
            print("please enter a valid number")
        else:
            break
    return answer 

#validates name 
def valid_name(prompt = "name: "):
    """checks if name is letters"""
    while True:
        name = input(prompt)
        if name.strip() and all(x.isalpha() or x.isspace() for x in name):
            return name
        else:
            print("please enter a valid name")
    


def valid_id():
    """checks if id is correct format"""
    while True:
        id = input("input id: ")
        if id.isdigit() and int(id) > 0 and len(id) == 7:
            return int(id)
        else:
            print("please enter valid id")


def find_soldier_by_id(soldier_id):
    """checks if soldier in list and returns soldier"""
    for i in soldiers:
        if i["id"] == soldier_id:
            return i
    return

def soldier_has_duty(soldier, duty_input):
    """checks if duty exists in soldier"""
    for duty in soldier["duties"]:
        if duty_input == duty["duty"]:
            return True
    return

def valid_day(day):
    """checks if day is valid"""
    valid_day_list = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day.lower() in valid_day_list


def valid_status(status):
    """checks if status is valid"""
    valid_status_list = ["pending", "completed", "missed"]
    return status.lower() in valid_status_list
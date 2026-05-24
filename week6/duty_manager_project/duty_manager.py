from utils import *
from data import soldiers


def add_duty_to_soldier(id_input, duty_input, day_input):
    """adds a new duty to a specific soldier"""
    soldier = find_soldier_by_id(id_input)

    if not soldier:
        raise KeyError("Keyerror - soldier does not exists")
    
    if soldier_has_duty(soldier, duty_input):
        raise ValueError("ValueError - soldier already has duty")
    
    if not valid_day(day_input):
        raise ValueError("ValueError - invalid day")
    
    soldier["duties"].append(
        {"duty": duty_input, "status": "pending", "day": day_input}
    )
    return


def update_duty_status(id_input, duty_name, new_status):
    """updates the status of an existing duty"""
    soldier = find_soldier_by_id(id_input)
    
    if not soldier:
        raise KeyError("Keyerror - soldier does not exists")
    
    if not soldier["duties"]:
        raise IndexError("no duties yet")
    
    if not soldier_has_duty(soldier, duty_name):
        raise KeyError("Keyerror - duty does not exists")
    
    if not valid_status(new_status):
        raise ValueError("ValueError - invalid status")
    
    for i in soldier["duties"]:
        if i["duty"] == duty_name:
            i["status"] = new_status
    return


def view_soldier_duties(id_input):
    """prints all duties assigned to a soldier"""
    soldier = find_soldier_by_id(id_input)
    if not soldier:
        raise KeyError("Keyerror - soldier does not exists")
    if len(soldier["duties"]) == 0:
        print("no duties to show")
    for i in soldier["duties"]:
        print(f"duty: {i['duty']}, day: {i['day']}, status: {i['status']}")
    return
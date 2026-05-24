from data import soldiers 
from utils import *


def add_solder(id_input, name_input):
    """adds solder to list"""
    if find_soldier_by_id(id_input):
        raise ValueError("ValueError - soldier already exists")
    else:
        soldiers.append({"id": id_input, "name": name_input, "duties": []})
        return


# removes selected solder from list
def remove_solder(id_input):
    """removes a solder from the list"""
    soldier = find_soldier_by_id(id_input)
    if not soldier:
        raise ValueError("ValueError - soldier not found")
    soldiers.remove(soldier)
    print(f"removed {id_input}")
    return
    

def show_solder_list():
    """prints summary of all soldiers"""
    for i in soldiers:
        print(f"id: {i['id']}, name: {i['name']}, duties: {len(i['duties'])}")
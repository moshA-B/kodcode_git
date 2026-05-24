from utils import *
from soldier_manager import *
from duty_manager import *
from data import *


def handle_add_soldier():
    """handles user input to add a soldier"""
    while True:
        id_input = valid_id()
        name_input = valid_name()
        try:
            add_solder(id_input, name_input)
            return
        except ValueError as e:
            print(e)


def handle_remove_soldier():
    """handles user input to remove a soldier"""
    while True:
        id_input = valid_id()
        try:
            remove_solder(id_input)
            return
        except ValueError as e:
            print(e)

def handle_show_soldier():
    """displays the list of all soldiers"""
    show_solder_list()


def handle_add_duty():
    """handles user input to add a duty"""
    while True:
        id_input = valid_id()
        duty_input = valid_name(prompt="duty: ")
        day_input = input("day: ")
        try:
            add_duty_to_soldier(id_input, duty_input, day_input)
            return
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


def handle_update_status():
    """handles user input to update duty status"""
    while True:
        id_input = valid_id()
        duty_name = input("duty: ")
        new_status = input("status: ")
        try:
            update_duty_status(id_input, duty_name, new_status)
            return
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)
            break
        

def handle_view_soldier_duties():
    """handles user input to view duties"""
    while True:
        id_input = valid_id()
        try:
            view_soldier_duties(id_input)
            return
        except KeyError as e:
            print(e)


def show_menu():
    """prints the main menu options"""
    print("==soldier task manager==")
    print("1. add soldier")
    print("2. remove soldier")
    print("3. show soldier list")
    print("4. add duty to soldier")
    print("5. update duty status")
    print("6. view soldier duties")
    print("7. exit")



def main():
    """main program loop execution"""
    while True:
        show_menu()
        answer = get_user_input()
        if 7 > int(answer) > 1:
            if len(soldiers) == 0:
                print("list is empty")
                continue
    

        if answer == "1":
            handle_add_soldier()

        elif answer == "2":
            handle_remove_soldier()

        elif answer == "3":
            handle_show_soldier()

        elif answer == "4":
            handle_add_duty()

        elif answer == "5":
            handle_update_status()

        elif answer == "6":
            handle_view_soldier_duties()

        elif answer == "7":
            break


if __name__ == "__main__":
    main()
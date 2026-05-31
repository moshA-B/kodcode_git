from shape_manager import ShapeManager
from hexagon import Hexagon
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle
import logging
import json


def show_menu():
    """Print the primary CLI application menu options to the console."""
    print("1. create shape")
    print("2. show all shapes")
    print("3. update shape")
    print("4. delete shape")
    print("5. exit ")


def show_shape_menu():
    """Print the menu of available geometric shapes for creation selection."""
    print("1. square")
    print("2. rectangle")
    print("3. triangle")
    print("4. circle")
    print("5. hexagon")


def valid_input_for_shape(prompt=""):
    """Prompt user for a numeric value and return it as a float if it is greater than zero."""
    while True:
        num = input(prompt)
        try:
            if not float(num) <= 0:
                return float(num)
            print("please enter a valid number")
        except (ValueError, TypeError):
            print("please enter a valid number")


def valid_input_for_menu(prompt=""):
    """Prompt user for an integer selection and return it as a string if valid."""
    while True:
        choice = input(prompt)
        try:
            a = int(choice)
            return choice
        except (ValueError, TypeError):
            print("please enter a valid number")


def handle_input_for_shapes(current_shape):
    """Collect specific geometric dimensional attributes based on the type of shape provided."""
    if current_shape == None:
        raise ValueError("invalid id")
    if isinstance(current_shape, Square) or current_shape == Square:
        side = valid_input_for_shape("enter new side: ")
        data = {"side": side}
    elif isinstance(current_shape, Rectangle) or current_shape == Rectangle:
        width = valid_input_for_shape("enter new width: ")
        height = valid_input_for_shape("enter new height: ")
        data = {"width": width, "height": height}
    elif isinstance(current_shape, Triangle) or current_shape == Triangle:
        side1 = valid_input_for_shape("input side1")
        side2 = valid_input_for_shape("input side2")
        side3 = valid_input_for_shape("input side3")
        data = {"side1": side1, "side2": side2, "side3": side3}
    elif isinstance(current_shape, Circle) or current_shape == Circle:
        radius = valid_input_for_shape("enter new radius: ")
        data = {"radius": radius}
    elif isinstance(current_shape, Hexagon) or current_shape == Hexagon:
        side = valid_input_for_shape("enter new side: ")
        data = {"side": side}

    return data


def handle_create_shape(ins, available):
    """Guide the user through selecting and creating a new shape instance via the manager."""
    show_shape_menu()
    shape_input = valid_input_for_menu("your choice(1 - 5): ")
    try:
        available_keys = list(available.keys())
        chosen_key = available_keys[int(shape_input) - 1]

        current_shape = available[chosen_key]
        data = handle_input_for_shapes(current_shape)
        ins.create_shape(current_shape, **data)
    except KeyError:
        print("please enter a valid number")


def handle_get_shapes(ins):
    """Retrieve all tracked shapes from the manager and print them as formatted JSON strings."""
    shape_list = ins.get_all_shapes()
    for item in shape_list:
        print(json.dumps(item, indent=4))


def handle_update_shape(ins):
    """Locate an existing shape by ID and safely update its defining attributes."""
    id = int(valid_input_for_menu("enter id: "))
    current_shape = None
    for obj in ins.shapes:
        if obj.shape_id == id:
            current_shape = obj
    try:
        new_data = handle_input_for_shapes(current_shape)
        ins.update_shape(id, new_data)
        print("updated")
        return
    except ValueError as e:
        print(e)


def handle_remove_shape(ins):
    """Prompt for a shape ID and remove the corresponding shape via the manager."""
    id = int(valid_input_for_menu("enter id: "))
    ins.delete_shape(id)
    print("removed")


def main():
    """Initialize application dependencies and execute the main operational menu loop."""
    available_shapes = {
        "square": Square,
        "rectangle": Rectangle,
        "triangle": Triangle,
        "circle": Circle,
        "hexagon": Hexagon,
    }
    shape_manager = ShapeManager(available_shapes)
    while True:

        show_menu()

        choice = valid_input_for_menu("your choice: ")

        if choice == "1":
            handle_create_shape(shape_manager, available_shapes)

        elif choice == "2":
            handle_get_shapes(shape_manager)

        elif choice == "3":
            handle_update_shape(shape_manager)

        elif choice == "4":
            handle_remove_shape(shape_manager)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
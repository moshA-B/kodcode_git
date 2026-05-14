# question 1
def user_validation(user_list):
    result = []
    for item in user_list:
        if item[1] >= 18 and item[2] == "active":
            result.append(item[0])
    return result

user_list = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(user_validation(user_list))

# question 2

def validate_email(email):
    if not email:
        print("Invalid user")
        return None
    
def quantity_validate(quantity, stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None
    
def price(quantity):
    if quantity >= 10:
       price = 0.9
    if quantity >= 50:
       price = 0.85
    return quantity * price

def handle_purchase(user_email, product_name, quantity):
    
    stock = 2000
    order_user = validate_email(user_email)
    order_product = product_name
    order_quantity = quantity_validate(quantity, stock)
    order_total = price(order_quantity)
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status

# question 3

def manage_students(names, grades, new_name, new_grade):
    # validation
    
    
    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

def student_report(student):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_to_file():
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    return names, grades

def name_validation(name):
    if not name or len(name) < 2:
        print("Error: invalid name")
        return 
    
def grade_validation(grade):
    if grade < 0 or grade > 100:
        print("Error: grade must be 0-100")
        return 


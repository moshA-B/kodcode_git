# question 1.

age = int(input("PLease enter your age: "))
if 0 < age > 120:
    print("Invalid")
elif 0 < age < 12:
    print("Child")
elif 13 <= age < 17:
    print("teen")
else:
    print("Adult")

# question 2.


char = input("Enter a character: ").lower()

if char not in "abcdefghijklmnopqrstuvwxyz":
    print("Consonant")

elif char in "aeiou":
    print("Vowel")

else:
    print("invalid")

# question 3.

age = int(input("PLease enter your age: "))
has_vip = input("VIP card (yes/no): ")

if age < 16:
    print("access denied")
elif (age == 18 and has_vip == "yes") or (19 <= age < 21):
    print("access granted")
else:
    print("else")

# question 4.

stored_password = "1234"

user_input = input("Enter your password: ")


if user_input == stored_password:
    print("Access Granted")
elif len(user_input) < 8:
    print("Too short")
else:
    print("Wrong password")


# question 5.


x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))


if x < 10 or x > 50 or y < 20 or y > 80:
    print("Outside the rectangle")

elif x == 10 or x == 50 or y == 20 or y == 80:
    print("On the edge")

else:
    print("Inside the rectangle")

# question 6.

user_input = input("Please enter your name: ")

name = user_input or "Anonymous"

print(f"Hello, {name}!")

# question 8.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


positive_count = (num1 > 0) + (num2 > 0) + (num3 > 0)

print(f"Number of positive values: {positive_count}")

# question 10.

score = float(input("Enter your score (0-100): "))

grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))

print(grade)

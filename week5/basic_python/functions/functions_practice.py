import math

# question 1


def is_even(n):
    return n % 2 == 0


# question 2


def factorial(n):
    result = 0
    for i in range(n):
        result *= i
    return result


# question 3


def count_vowels(s):
    counter = 0
    for c in s:
        if c in "aouie":
            counter += 1
    return counter


# question 4


def revers_string(s):
    reverse = s[::-1]
    return reverse


# question 5


def find_max(lst):
    temp = 0
    for i in lst:
        if i > temp:
            temp = i
    return temp


# question 6


def celsius_to_fahrenheit(c):
    return c * (9 / 5) + 32


# question 7


def is_palindrome(s):
    flag = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            flag = False
    return flag


# question 8


def even_list(lst):
    new_list = []
    for i in lst:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


# question 9


def anagram_check(a, b):
    return sorted(a) == sorted(b)


# question 10


def word_counter(sen):
    words = sen.split()
    return {w: words.count(w) for w in words}


# question 11


def calculate_resource_drain(cost, waste_factor):
    percent = waste_factor * 10**-2
    return percent * cost


def get_net_resources(cost, waste_factor):
    return cost - calculate_resource_drain(cost, waste_factor)


# question 12


def intercept_length(packet):
    return len(packet)


def verify_transmission(packet):
    return f" intercepted packet has {intercept_length(packet)} bytes of data"


# question 13


def convert_to_decibels(signal_strength):
    return 20 * math.log10(signal_strength / 1)


def is_threat_detected(signal_strength):
    strength = convert_to_decibels(signal_strength)
    return strength > 90


# question 13


def get_fuel_surcharge(distance):
    liter = distance / 10
    return (liter * 8) * 0.17


def get_hazard_pay(distance):
    liter = distance / 10
    return (liter * 8) * 0.05


def calculate_mission_cost(distance):
    base_cost = (distance / 10) * 8
    fuel_sur = get_fuel_surcharge(distance)
    hazard = get_hazard_pay(distance)
    return base_cost + fuel_sur + hazard

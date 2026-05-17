#question 1

def safe_int(s):
    try:
        return int(s)
    except (ValueError ,TypeError):
        return
    
#question 2

def safe_divide(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        return "undefined"
    except TypeError:
        return
    

#question 3

def read_first_line(path):
    try:
        with open(path, 'r') as p:
            read = p.readline()
        return read
    except (FileNotFoundError, ValueError, TypeError):
        return None

# question 4

def get_value(d, key):
    try: 
        return d[key]
    except (KeyError, ValueError , TypeError):
        return 
    
#question 5

def prase_ints(vals):
    new = []
    for i in vals:
        try:
            new.append(int(i))
        except (TypeError, ValueError):
            continue
    return new

#question 6

def set_age(age):
    try:
        if 0 > age or age > 150:
            raise ValueError("ValueError")
        else:
            return age
    except TypeError:
        return 
    
#question 7

class InsufficientFundsError(Exception):
    pass
    def withdraw(balance, amount):
        if amount > balance:
            raise InsufficientFundsError
        return balance - amount
    
#question 8

def retry(func, n):
    for _ in range(n):
        try:
            return func
        except Exception as e:
            final = e
            
    return final

#question 9 

def count_errors(funcs):
    count = 0
    for f in funcs:
        try:
            f
        except Exception:
            count += 1

    return count

#question 10
def load(path):
    try:
        with open(path, 'r') as file:
            first_line = file.readline()
            return int(first_line)
    except Exception as original_error:
        raise RuntimeError("failed to load") from original_error

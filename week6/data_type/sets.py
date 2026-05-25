#1

def remove_duplicates(lst):
    new = set(lst)
    return list(new)

#2
def unique_count(lst):
    new = set(lst)
    count = 0
    for i in new:
        count += 1
    return count

#3
def common_elements(lst1,lst2):
    common = set(lst1) & set(lst2)
    return sorted(list(common))

#4

def unique_elements(lst1, lst2):
    one = set(lst1)
    two = set(lst2)
    u1 = one - two
    u2 = two - one
    return sorted(list(u1 | u2))


#5
def is_subset(lst1, lst2):
    one = set(lst1)
    two =set(lst2)
    sub = one & two
    return True if not sub else False

#6
def unique_str(string):
    return len(string) == len(set(string)) 


#7
def duplicates(lst):
    new = set()
    for i in lst:
        if i in new:
            return i
        else:
            new.add(i)

#8
def distinct_words(string):
    new = set()
    for word in string.split().lower():
        new.add(word)
    return len(new)

#9
def pair_sum(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

#10
def symmetric_difference(lst1, lst2):
    diff1 = set(lst1) - set(lst2)
    diff2 = set(lst2) - set(lst1)
    
    return sorted(list(diff1) + list(diff2))

        



print(symmetric_difference([2,1,3,4,7,6,10,1], [5,3,4,6]))
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
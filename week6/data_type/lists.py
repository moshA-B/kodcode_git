#1
def sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

#2
def max(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    
    return max

#3
def count_val(lst, val):
    count = 0
    for i in lst:
        if i == val:
            count += 1

    return count

#4
def reverse_m(lst):
    new_list = [lst[-i -1] for i in range(len(lst))]
    return new_list

#5
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list

#6
def second_to_largest(lst):
    result = 0
    for i in lst:
        if i > result:
            if i < max(lst):
                result = i
        
    return result if result else None



#7
def merge_and_sort(lst1, lst2):
    new_list = lst1+lst2
    new_list.sort()
    return new_list

#8
def rotate(lst, k):
    k = k % len(lst)
    new = lst[-k:]
    new2 = lst[:-k]
    new += new2
    return new
    


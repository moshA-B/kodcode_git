
#1
def sum(tpl):
    count = 0
    for i in tpl:
        count += i
    return count

#2
def max(tpl):
    count = 0
    for i in tpl:
        if i > count:
            count = i
    return count

#3
def count(tpl, oc):
    count = 0
    for i in tpl:
        if i == oc:
            count += 1
    return count


#4
def reverse(tpl):
    new = ()
    for i in range(len(tpl)):
        new += (tpl[-i -1],)
    return new


#5
def swap_pairs(tpl):
    new = ()
    for i in range(0,len(tpl)-1,2):
        a,b = (tpl[i],tpl[i+1])
        new += (b,a)
    return new


#6
def min_max(tpl):
    min = tpl[0]
    max = tpl[0]
    for i in tpl:
        if i > max:
            max = i
        elif i < min:
            min = i
    return min,max
print(min_max((1,2,3,4,5,6)))


#7
def euclidean_distance(t1, t2):
    num1 = (t1[0] - t2[0])**2
    num2 =  (t1[1] - t2[1])**2
    distance = (num1 + num2)**0.5
    return distance

#8
def merge_and_sort(tpl1 , tpl2):
    return tuple(sorted(tpl1 + tpl2))


#9
def total_count(tpl):
    dict = {}
    for i in tpl:
        dict[i] = dict.get(i,0)+1
    return tuple(dict.items())

#10
def rotate(tpl, k):
    k = k % len(tpl)
    new = (tpl[-k :])
    new2 = (tpl[: -k ])
    new += new2
    return new

print(rotate((1,2,3,4,5,6),2))


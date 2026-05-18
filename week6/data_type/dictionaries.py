
#1
def sum(dct):
    count = 0
    for k in dct:
        count += dct[k]
    return count

#2
def max_m(dct):
    max = (0,0)
    for k in dct.items():
        if k[1] > max[1]:
            max = k

    return max[0]


#3
def count_chars(str):
    chr_dict = {}
    for chr in str:
        chr_dict[chr] = chr_dict.get(chr,0) + 1
    return chr_dict

#4
def invert(dct):
    return {v : k for k,v in dct.items}

#5
def merge(dct1, dct2): 
    return dct1 | dct2

#6
def filter_by_val(dct , thresh):
    return {k : dct[k] for k in dct if dct[k] > thresh}

#7
def first_letter(lst):
    dct = {}
    for word in lst:
        dct.setdefault(word[0],[]).append(word)
    return dct

#8
def words_in_str(str):
    dct = {}
    for word in str.split():
        dct[word] = dct.get(word, 0) + 1
    return dct

#9
def common_keys(dct1, dct2):
    return sorted([k for k in dct1 if k in dct2])
    

#10
def most_common_val(dct):
    new_dct = {}
    for v in dct.values():
        new_dct[v] = new_dct.get(v, 0)+1
    return max(new_dct , key=new_dct.get)



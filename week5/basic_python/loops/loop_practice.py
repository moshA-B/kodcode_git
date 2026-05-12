# #question1
# for i in range(10):
#     if i % 2 == 0:
#         if i == 0:
#             print(i)
#         continue
#     elif i == 7:
#         break
#     print(i)

# #question2
# while True:
#     password = input("password: ")
#     if password == "1234":
#         print("welcom!")
#         break
#     else:
#         print("try again")

# #question3

# product_list=[]

# while True:
#     product=input("product: ")
#     if product == "done":
#         break
#     else:
#         product_list.append(product)

# print(product_list)

# #question3 2.0

# for row in range(1,3):
#     for col in range(1,3):
#         if col == 2:
#             break
#         print(row,col)

# #question4

# word =input("word: ").lower()
# count=0
# for l in word:
#     if l in "ieoua":
#         count+=1
# print(count)

# #question5
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i} x {j} = {i*j}")

#question6
# word =input("word: ")
# rev =""
# for i in range(len(word)):
#     rev+= word[-i -1]
# print(rev)

#question7
# num = int(input("number: "))

# temp = num
# count =0
# while temp > 0:
#     digit = temp % 10    
#     if digit % 2 == 0:     
#         count += 1
        
#     temp = temp // 10  
# print("Even digit count:", count)
    
#question8

# word = input("word: ")
# new_str=""
# for chr in word:
#     new_str+=chr*2
# print(new_str)

#questin9
# high=0
# while True:
#     num = int(input("enter a posotiv number: "))
#     if num == 0:
#         print(high)
#         break
#     if num > high:
#         high = num

#question10
# word = input("word: ")
# good= True
# for chr in word:
#     if not chr.isalnum():
#         good = False
#         break
# print(good)

#question11

num = int(input("number: "))

reverse = 0
while num > 0:
    temp = num % 10
    reverse = (reverse * 10) +temp
    num = num // 10

print(reverse)


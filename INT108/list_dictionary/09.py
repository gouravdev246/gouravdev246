#Find index of element in list. If not found, print -1.
# list1 = []
# size_of_list = int(input("Enter Size OF list:"))
# word = (input("Enter integers: "))
# for i in range(size_of_list):
#     integers = word.split()
#     list1.append(int(integers[i]))
# element = int(input("Enter the element you want to find:"))
# index = 0
# for num in list1:
#     if num == element:
#         print(index)
#         break
#     index +=1
# else:
#     print(-1)

# Find index of element in list. If not found, print -1.
size_of_list = int(input("Enter Size OF list: "))
word = input("Enter integers: ")
list1 = [int(x) for x in word.split()]
element = int(input("Enter the element you want to find: "))
try:
    print(list1.index(element))
except ValueError:
    print(-1)
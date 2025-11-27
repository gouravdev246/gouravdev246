#Form a dictionary using two lists.
list1 = []
size_of_list = int(input("Enter Size OF list:"))
for i in range(size_of_list):
    word = input("Enter key: ")
    list1.append(word)
list2 =[]
for i in range(size_of_list):
    word = input("Enter value: ")
    list2.append(word)
dict1 = dict(zip(list1 , list2))
print(dict1)
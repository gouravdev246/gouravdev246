size_of_list = int(input("Enter Size OF list: "))
word = input("Enter integers: ")
list1 = [int(x) for x in word.split()]
element = int(input("Enter the element you want to find: "))
try:
    print(list1.index(element))
except ValueError:
    print(-1)
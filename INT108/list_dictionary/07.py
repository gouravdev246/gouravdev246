#Remove duplicate elements from a list.
integers = []
size_of_list = int(input("Enter Size OF list:"))
for i in range(size_of_list):
    num = int(input("Enter Integers: "))
    integers.append(num)
integers_copy = set(integers)
print(list(integers_copy))
# Find the maximum and minimum element from a list.
integers = []
size_of_list = int(input("Enter Size OF list:"))
for i in range(size_of_list):
    num = int(input("Enter Integers: "))
    integers.append(num)
print(f"Max Value: {max(integers)}")
print(f"Min Value: {min(integers)}")
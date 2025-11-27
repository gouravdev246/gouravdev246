#Sort a dictionary by values in ascending order.
n1 = int(input("Size:"))
dict1 = {}
for i in range(n1) :
    key_value1 = input("Enter Key value Pair(eg. apple 10):")
    key , value = key_value1.split()
    dict1[key] = int(value)
print(sorted(dict1.items() , reverse=True))
#Merge two dictionaries. If a key exists in both, add their values.
n1 = int(input("Size of 1st Dictionary :"))

dict1 = {}

for i in range(n1) :
    key_value1 = input("Enter Key value Pair(eg. apple 10):")
    key , value = key_value1.split()
    dict1[key] = int(value)
n2 = int(input("Enter the size of the second dictionary: "))
dict2 = {}
for i in range(n2):
    key_value2 = input("Enter Key value Pair(eg. apple 10):")
    key , value = key_value2.split()
    dict2[key] = int(value)
merged_dict = dict1.copy()
for key , value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value
print(merged_dict)

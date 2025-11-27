#Create a dictionary of student names and marks. Print the topper.
n = int(input("Size of 1st Dictionary :"))

dict1 = {}

for i in range(n) :
    key_value1 = input("Enter Key value Pair(eg. apple 10):")
    key , value = key_value1.split()
    dict1[key] = int(value)
topper_name = max(dict1, key=dict1.get)
topper_score = dict1[topper_name]
print(f"The topper is {topper_name} with {topper_score} marks.") 


        
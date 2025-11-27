#Find the second largest element in a list.
n = int(input('Size of list:'))
num = []
for i in range(n):
    integers = int(input("Enter Integers:"))
    num.append(integers)
s_l = []
for i in range(len(num)):
    if num[i] >= min(num):
        s_l.append(num[i])
print(s_l[-2])

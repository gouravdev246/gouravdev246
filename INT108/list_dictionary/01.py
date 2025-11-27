# Write a program that reads a list of integers and prints the list in reverse order.
l = [1 , 2 ,3 ,4,5,6,7,8,9]
r_l =[]
for i in range(1 ,len(l)+1):
    r_l.append(l[-i])
print(r_l)
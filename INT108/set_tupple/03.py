#Find the difference between two sets (setl - set2).
set1 = set(map(int , input().split() ))
set2 = set(map(int , input().split()))

# union_set = set1 - set2
diff_set = set1.difference(set2)

print(diff_set)
n = 6
for i in range(1 , n+1):
    for j in range(n - i):
        print(" " , end=" ")
    for k in range(1 , 2*i):
        print(k, end=" ")
    print()
'''

          1 
        1 2 3
      1 2 3 4 5
    1 2 3 4 5 6 7
  1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10 11

'''
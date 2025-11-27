'''
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 


'''

n = 5
alph = 65
for i in range(1 , n+1):
    for j in range(n - i):
        print(" " , end="")
    for k in range(i):
        # chr(65) is 'A'. So, 65+0='A', 65+1='B', etc.
        letter = chr(65 + k)
        print(letter, end=" ")

    print()
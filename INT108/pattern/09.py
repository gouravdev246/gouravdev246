'''


*********
 *******
  *****
   ***
    *

'''

# n = 7
# for i in range(n , 0 , -1):
#     for j in range(i - 1):
#         print(" " ,end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
# Set the number of rows for the initial pyramid height
n = 5

# Loop downwards from n to 1
for i in range(n, 0, -1):
    # 1. Print the leading spaces
    for j in range(n - i):
        print(" ", end="")
        
    # 2. Print the stars
    for k in range(2 * i - 1):
        print("*", end="")
        
    # 3. Move to the next line
    print()
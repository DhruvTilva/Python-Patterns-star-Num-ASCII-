# *******pattern1 star********
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()


# n= int(input("enter number:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end='')
#     print()
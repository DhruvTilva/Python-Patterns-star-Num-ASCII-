from re import A


n= int(input("enter number:"))

# print(k)
for i in range(n):
    k= ord("A") + i #ASCII value for
    for j in range(i+1):
        print(chr(k),end='')
        k=k+1
    print()
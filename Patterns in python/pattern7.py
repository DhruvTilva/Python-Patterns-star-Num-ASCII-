# ********8pattern7 star********
for i in range(1,5):
    for j in range(1,8):
        if j<=5-i or j>=3+i:  #logic
            print("*",end='')
        else:
            print(" ",end='')
    print()
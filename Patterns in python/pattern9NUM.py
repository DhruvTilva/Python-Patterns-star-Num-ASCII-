for i in range(1,6):
    k=6-i #logic 1
    for j in range(1,6):
        if j<=6-i: #logic 2
            
            print(k,end='')
            k-=1 #logic3
        else:
            print(" ",end='')
    print()
n=int(input(""))
c="*"
for i in range(1,n+1):
    for k in range(n-i+1,1,-1):
        print(" ",end="")
    
    for j in range(i):
        print("*",end=" ")
        
    for k in range(n-i+1,1,-1):
        print(" ",end="")
        
    # for k in range(i):
    #     print(" ",end="")
    
    # for j in range(n-i+1,1,-1):
    #     print("*",end=" ")
        
    # for k in range(i):
    #     print(" ",end="")

    for k in range(n-i+1,1,-1):
        print(" ",end="")
    
    for j in range(i):
        print("*",end=" ")
    print("")
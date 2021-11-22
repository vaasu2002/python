n=9
m = int((n+1)/2)
for i in range(n):
    if(i==0 or i==(n-1)):
        for j in range(n):
            print("*",end="")
    elif(i == (n-1)/2):
        print("*",end="")
        for k in range(1,m-1):
            print(" ",end="")
        print("*",end="")
        for m in range(m-2):
            print(" ",end="")
        print("*",end="")
    else:
        for j in range(n):
            if(j==0 or j==(n-1)):
                print("*",end="")
            elif(i==j or j == (n-1-i)):
                print("*",end="")
            else:
                print(" ",end="")
            
    print("\r")

"""    
*********
**     **
* *   * *
*  * *  *
*   *   *
*  * *  *
* *   * *
**     **
********* 
"""

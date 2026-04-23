def posconveter(n):
    while(n-1<=0):
        print(n,end=" " )
        n-=1
def negconveter(n):
    while(n+1>=0):
        print(n,end=" ")
        n+=1
n=int(input("enter the number:"))
if(n>0):
    posconveter(n)
else:
    negconveter(n)
          
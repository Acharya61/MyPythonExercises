def Sqrt(x):
    if (x == 0 or x == 1):
        return x
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i
    return i - 1
   
b=[] 
def prime(x):
    f = 0
    for i in range(2,x-1):
        if(x%i==0):
            f = 0
            break
        f = 1
    if(f==1):
        b.append(x)

n=int(input())
a=[]
for i in range (2,Sqrt(n)):
    if(n%i==0):
       a.append(i)
for j in range(0,len(a)):
  prime(a[j])
r=len(b)
print(b[r-1])
            
        
        
            
    
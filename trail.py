def c_gcd(x,y):
    while(y):
        x,y = y , x%y
    return x
lst=list(map(int,input().split()))
n1=lst[0]
n2=lst[1]
gcd = c_gcd(n1,n2)
for i in range(2,len(lst)):
    gcd=c_gcd(gcd,lst[i])
print(gcd)


def c_gcd(a,b):
    if b==0:
        return a
    else:
        return c_gcd(b,a%b)
n1=int(input("num1"))
n2=int(input("num2"))
ans=c_gcd(n1,n2)
print("gcd of the two numbers is ",ans)
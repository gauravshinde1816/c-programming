str=input()
str=str.replace(" ","")
str=str.lower()
flag=[False]*26
lst=list(str)
for x in lst:
    index=ord(x)-ord('a')
    flag[index]=True

for x in flag:
    if x==False:
        print("not pangram")
        break
    
else:
    print("pangram")
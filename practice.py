s=input()
lst=list(s)
flag = [False]*5
for x in lst:
    if x.isalnum()==True:
        flag[0] = flag[0] or True  
    if x.isalpha()==True:
        flag[1] = flag[1] or True
 
    if x.isalpha()==True:
        flag[2] = flag[2] or True

    if x.islower()==True:
        flag[3]  = flag[3] or True 
    if x.isupper()==True:
        flag[4] = flag[4] or True


print(flag)
    
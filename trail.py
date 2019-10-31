n=int(input())
lst=[]

for j in range(n):
    lst1=input().split()
    if lst1[0]=="insert":
        lst.insert(int(lst1[1]),int(lst1[2]))
        # print(lst)
    elif lst1[0]=="append":
        lst.append(int(lst1[1]))
        # print(lst)
    elif lst1[0]=="remove":
        lst.remove(int(lst1[1]))
        # print(lst)
    elif lst1[0]=="sort":
        lst.sort()
        # print(lst)
    elif lst1[0]=="pop":
        lst.pop()
        # print(lst)
    elif lst1[0]=="reverse":
        lst.reverse()
        break
        
    else:
        print(lst)


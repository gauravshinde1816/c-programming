
def minion_game(s):
    S=0
    K=0
    for i in range(0,len(s)):
        add=len(s)-i
        if s[i] in ['A','I','O','U','E']:
            K+=add
        else:
            S+=add
    if S>K:
        print("Stuart",S)
    elif K>S:
        print("kevin",K)
    else:
        print("draw")
# if __name__ == "__main__":
    # string=input()
    # minion(string)

if __name__ == '__main__':
    s = input()
    minion_game(s)
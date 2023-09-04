n = input()
char = "abcdefghijklmnopqrstuvwxyz"

for ch in char:
    if ch in n:
        print(n.index(ch), end = " ")
    else:
        print(-1, end = " ")
    
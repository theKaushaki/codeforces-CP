i = int(input())
o = 0
for j in range(0, i):
    a, b, c = input().split(" ")
    if((int(a)+int(b)+int(c)) > 1):
        o=o+1
        pass
    pass
print(o)
i = int(input())
inline=[]
for k in range(0, i):
    inline.append(input())
    pass
for a in inline:
    if(len(a) > 10):
        print(f"{a[0]}{len(a)-2}{a[-1]}")
        pass
    else:
        print(a)
        pass
    pass
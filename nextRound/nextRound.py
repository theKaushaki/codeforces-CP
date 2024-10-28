n, k = input().split()
k = int(k)
#n is the number of contestants,and k is qualifying score
scoreLine = input()
scoreLine = scoreLine.split()
qn = 0
for i in scoreLine:
    if(int(i) < int(scoreLine[k])):
        break
    elif(int(i) > 0):
        qn = qn + 1
        pass
    pass
print(qn)
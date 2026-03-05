n,m = input().split()
n = int(n)
m = int(m)
ary1 = list(map(int, input().split()))
ary2 = list(map(int, input().split()))
ans=[]

ary1.sort()
ary2.sort()

p1 = 0
p2 = 0

while p1 < n and p2 < m:
    if ary1[p1] < ary2[p2]:
        ans.append(ary1[p1])
        p1 += 1
    else:
        ans.append(ary2[p2])
        p2 += 1
while p1 < n:
    ans.append(ary1[p1])
    p1 += 1

while p2 < m:
    ans.append(ary2[p2])
    p2 += 1
print(*ans)
    


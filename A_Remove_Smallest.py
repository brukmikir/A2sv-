t = int(input())

for _ in range(t):
    n = int(input())
    ary = list(map(int, input().split()))
    
    ary.sort()
    possible = True
    
    for i in range(n - 1):
        if ary[i + 1] - ary[i] > 1:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
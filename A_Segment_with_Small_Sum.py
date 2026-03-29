n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
sumn = 0
ans = 0

for r in range(n):
    sumn += arr[r]

    while sumn > s:
        sumn -= arr[l]
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
from collections import defaultdict


def solve():
    n = int(input())
    h = [int(i) for i in input().split()]
    ans = 1

    if n == 1:
        return ans

    for k in range(n):
        for i in range(1, n):
            cur, cnt = -1, 0
            for j in range(k, n, i):
                if cur != h[j]:
                    ans = max(ans, cnt)
                    cnt = 1
                    cur = h[j]
                else:
                    cnt += 1
                    ans = max(ans, cnt)

    return ans


print(solve())

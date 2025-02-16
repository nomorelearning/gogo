import sys
sys.stdin = open('test.txt')

T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    t, p = data
    n, m =len(t), len(p)
    i = j = 0
    cnt = 0
    while i < n:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == m:
            cnt += 1
            j = 0

    result = n - (m-1) * cnt
    print(f'#{tc}', result)
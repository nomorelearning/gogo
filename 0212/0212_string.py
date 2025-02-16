import sys
sys.stdin = open('test.txt', encoding = 'utf-8')

for _ in range(10):
    tc = int(input())
    p = input()
    t = input()
    n, m = len(t), len(p)
    i = j = cnt = 0
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
    print(f'#{tc}',cnt)
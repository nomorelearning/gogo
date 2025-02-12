import sys
sys.stdin = open('test.txt')

T = int(input())
for tc in range(1,T+1):
    p = input()
    t = input()
    n = len(t)
    m = len(p)
    i = j = 0
    while i < n and j < m:
        if t[i] != p[j]:            # 여기 인덱스 i는 그대로 넣어야지!!!!
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
    if j == m:
        result = 1
    else:
        result = 0

    print(f'#{tc}', result)
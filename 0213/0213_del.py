
import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    data = list(input())
    lst = []
    top = 0
    lst.append(data[0])
    i = 1
    while i < len(data):
        if lst:
            if lst[top] == data[i]:
                lst.pop()
                top -= 1
                i += 1
                continue

        lst.append(data[i])
        top += 1
        i += 1
    print(f'#{t} {len(lst)}')
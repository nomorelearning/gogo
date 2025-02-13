import sys
sys.stdin = open('test.txt')

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    if top == -1:
        return
    else:
        top -= 1
        return stack[top+1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    stack = [0] * n
    top = -1
    for i in range(n):
        if lst[i] == 0:
            pop()
        else:
            push(lst[i])

    data = stack[:top+1]
    result = 0
    for i in data:
        result += i

    print(f'#{t}',result)
import sys
sys.stdin = open('test.txt')


def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    top -= 1
    return stack[top + 1]

for t in range(1,11):
    n, nums = input().split()
    n = int(n)
    stack = [0] * (n+1)
    top = -1
    for num in nums:
        if top == -1:
            push(num)
        else:
            if stack[top] == num:
                pop()
            else:
                push(num)
    print(f'#{t}', ''.join(stack[:top+1]))
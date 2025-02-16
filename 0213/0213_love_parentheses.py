import sys
sys.stdin = open('test.txt')


opt = ('(','[','{','<','>','}',']',')')

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    if top == -1:
        return -1
    else:
        top -= 1
        return stack[top+1]

for t in range(1,11):
    n = int(input())
    lst = list(input())
    top = -1
    stack = [0] * n
    ans = 0
    for i in range(n):
        val = lst[i]
        if val in opt[:4]:
            push(val)
        else:
            k = pop()
            if k == -1:     # 없는데 닫는 기호 입력 시 중단
                break
            if stack[top] != opt[-opt.index(val)]:
                print(val,opt[-opt.index(val)-1])
                break
    if top == -1:
        ans = 1
    print(ans)

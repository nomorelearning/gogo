T = int(input())

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
        return stack[top + 1]


for t in range(1, T + 1):
    data = list(input())
    top = -1
    stack = [0] * len(data)
    opt = ('(', '{', ')', '}')
    ans = 0
    for i in range(len(data)):
        if data[i] not in opt:
            continue
        elif data[i] in opt[0:2]:
            push(data[i])
        else:
            val = pop()
            if val == -1:
                break
            if data[i] == opt[2]:
                if val != opt[0]:
                    break
            if data[i] == opt[3]:
                if val != opt[1]:
                    break
    else:
        if top == -1:
            ans = 1

    print(f'#{t}', ans)
import sys
sys.stdin = open('test.txt', 'r')
#
# d = 'algorithm'
# txt = list(d)
# N = len(txt)
#
# for i in range(N//2):
#     txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
#
# print(txt)


def fight(str, n):
    for i in range(n//2):
        if str[i] != str[n-1-i]:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    text = list(input())
    n = len(text)
    result = fight(text, n)
    print(f'#{tc}', result)


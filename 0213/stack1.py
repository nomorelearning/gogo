import sys
sys.stdin = open('test.txt')

def pair_check():
    stck = []
    if n%2 != 0:
        return 0
    for i in range(n):
        if lst[i] in pair.keys():
            stck.append(lst[i])
        else:
            one = stck.pop()
            if pair[one] != lst[i]:
                return 0
    if not stck:
        return 1

pair = {'(':')', '[':']', '{':'}', '<':'>'}
for tc in range(1,11):
    n = int(input())
    lst = input()
    print(f'#{tc} {pair_check()}')




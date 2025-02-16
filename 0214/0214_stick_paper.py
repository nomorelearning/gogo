import sys
sys.stdin = open('test.txt')

T = int(input())

def check(length):
    if length == 10:
        return 1
    if length == 0:
        return 1
    else:
        return 2 * check(length - 20) + check(length - 10)

for t in range(1,T+1):
    length = int(input())
    result = check(length)
    print(f'#{t}',result)
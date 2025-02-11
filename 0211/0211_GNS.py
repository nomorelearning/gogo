import sys
sys.stdin = open('test.txt', 'r')

which = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())

def mk_lst(n, tuple, texts):
    lst = [0] * 10
    for i in range(n):
        for j in range(10):
            if texts[i] == tuple[j]:
                lst[j] += 1
                break
    return lst

for _ in range(T):
    tc, n = input().split()
    texts = list(input().split())
    n = int(n)
    result = []
    lst = mk_lst(n, which, texts)
    for i in range(10):
        for _ in range(lst[i]):
            result.append(which[i])
    print(tc)
    print(*result)
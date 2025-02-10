import sys
sys.stdin = open('test.txt', 'r')

def binary_search(a, n, key):
    start = 0
    end = n - 1
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if a[middle] == key:
            return count
        elif a[middle] < key:
            start = middle
        else:
            end = middle
    return 1000


T = int(input())
for tc in range(1,T+1):
    page, pa, pb = map(int,input().split())
    pages = list(range(1, page + 1))

    a_result = binary_search(pages, page, pa)
    b_result = binary_search(pages, page, pb)

    if a_result < b_result:
        result = 'A'
    elif b_result < a_result:
        result = 'B'
    else:
        result = 0

    print(f'#{tc}', result)
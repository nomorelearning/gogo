import sys
sys.stdin = open('test.txt', 'r')

def my_sort(lst, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    result = my_sort(lst, N)
    print(f'#{tc}', *lst)
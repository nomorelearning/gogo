def find_min(a, start):
    min_idx = start
    for k in range(start + 1, len(a)):
        if a[min_idx] > a[k]:
            min_idx = k
    a[start], a[min_idx] = a[min_idx], a[start]

def find_max(a,start):
    max_idx = start
    for k in range(start + 1, len(a)):
        if a[max_idx] < a[k]:
            max_idx = k
    a[start], a[max_idx] = a[max_idx], a[start]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(10):
        if i % 2 == 0:
            find_max(lst, i)
        else:
            find_min(lst, i)

    print(f'#{tc}', *lst[:10])


N = int(input())
lst = list(map(int,input().split()))

mid_idx = N // 2 + 1
for i in range(mid_idx+1):
    min_idx = i
    for j in range(i+1, N):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

print(lst[mid_idx])
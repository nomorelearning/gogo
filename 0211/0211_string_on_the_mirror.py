T = int(input())

lst_1 = ['b', 'd', 'p', 'q']
lst_2 = ['d', 'b', 'q', 'p']

for tc in range(1, T+1):
    lst = list(input())
    n = len(lst)
    for i in range(n):
        for j in range(4):
            if lst[i] == lst_1[j]:
                lst[i] = lst_2[j]
                break
    for i in range(n//2):
        lst[i], lst[n-1-i] = lst[n-1-i], lst[i]
    print(f'#{tc}', ''.join(lst))
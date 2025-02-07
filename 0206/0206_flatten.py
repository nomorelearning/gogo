
def find_minmax(lst):
    min_val = lst[0]
    max_val = lst[0]
    for i in range(100):
        if min_val > lst[i]:
            min_val = lst[i]
        if max_val < lst[i]:
            max_val = lst[i]
    return min_val, max_val

def minmax_lst(min_val, max_val, lst):
    min_lst = []
    max_lst = []
    for i in range(len(lst)):
        if lst[i] == min_val:
            min_lst.append(i)
        if lst[i] == max_val:
            max_lst.append(i) 
    return min_lst, max_lst
            

for tc in range(1, 11):
    limit = int(input())
    lst = list(map(int,input().split()))
    max_val = min_val = lst[0]
    while True:
        if limit <= 0:
            break
        min_val, max_val = find_minmax(lst)
        if max_val - min_val <= 1:
            break
        min_lst, max_lst = minmax_lst(min_val, max_val, lst)
        while len(min_lst) > 0 and len(max_lst) > 0:
            if limit == 0:
                break
            lst[max_lst.pop()] -= 1
            lst[min_lst.pop()] += 1
            limit -= 1
    min_value, max_value = find_minmax(lst)
    result = max_value - min_value
    
    print(f'#{tc} {result}')
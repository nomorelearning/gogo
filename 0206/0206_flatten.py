for tc in range(1, 101):
    limit = int(input())
    lst = list(map(int,input()))


    while min_lst != [] and max_lst != []:
        if limit == 0:
            break
        lst[max_lst.pop()] -= 1
        lst[min_lst.pop()] += 1
        limit -= 1

def find_minmax(lst):
    min_val = lst[0]
    max_val = lst[0]
    for i in range(101):
        if min_val > lst[i]:
            min_val = lst[i]
        if max_val < lst[i]:
            max_val = lst[i]
    return min_val, max_val

def minmax_lst(min_val, max_val):
    min_lst = []
    max_lst = []
    for i in range(101):
        if lst[i] == min_val:
            min_lst.append(i)
        if lst[i] == max_val:
            max_lst.append(i)
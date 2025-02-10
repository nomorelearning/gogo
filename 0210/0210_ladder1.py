import sys
sys.stdin = open('test.txt', 'r')

def find_2(lst, index):
    for i in index:
        if lst[i] == 2:
            return i

def check_1(lst, start):
    idx_2 = start
    while idx_2 > 0:
        if lst[idx_2] == 1:
            return idx_2
        else:
            idx_2 -= 1
    return idx_2

def check_0(lst,start,dir):
    idx_3 = start
    while 100 >= idx_3 > 0:
        if lst[idx_3] == 0:
            return idx_3 - dir
        else:
            idx_3 += dir
    return idx_3

def get_result(arr, r, c):
    leg = [list(x) for x in zip(*arr)]
    while r >= 0:
        left_line = check_1(leg[c-1], r)
        right_line = check_1(leg[c+1], r)
        if left_line > right_line:
            c = check_0(arr[left_line], c, -1)
            r = left_line
        else:
            c = check_0(arr[right_line], c, 1)
            r = right_line

def mklst(lst):
    lst = []
    for i in range(100):
        if lst[i] == 1:
            lst.append(i)
    return lst

for tc in range(1,11):
    no = int(input())
    ladder_map = [list(map(int, input().split())) for _ in range(100)]
    lst = mklst(ladder_map[0])
    r = 99
    c = find_2(ladder_map[99], lst)

    print(f'#{tc}', result)



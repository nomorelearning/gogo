import sys
sys.stdin = open('test.txt', 'r')

def palindrome(lst, n):
    for i in range(n//2):
        if lst[i] != lst[n-1-i]:
            return 0
    return 1

for t in range(1,11):
    n = int(input())
    row_lst = [list(input()) for _ in range(8)]
    col_lst = [list(x) for x in zip(*row_lst)]
    count = 0

    for j in range(8):
        for i in range(9-n):
            result = palindrome(row_lst[j][i:i+n],n)
            count += result
            result = palindrome(col_lst[j][i:i + n], n)
            count += result
    print(f'#{t}', count)
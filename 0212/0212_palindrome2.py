import sys
sys.stdin = open('test.txt')

def find_palindrome(arr, x):         # arr은 테스트 리스트, x는 찾는 회문 길이
    for s in range(100 - x + 1):          # 기대하는 길이의 회문이 리스트에 포함되어 있는지 확인하는 함수
        e = s + x - 1
        for i in range(x//2):
            if arr[i + s] != arr[e - i]:
                break
        else:
            return True
    else:
        return False

for _ in range(10):
    tc = int(input())
    row_arr = [list(input()) for _ in range(100)]
    col_arr = [list(x) for x in zip(*row_arr)]

    for x in range(100, 0, -1):
        for i in range(100):
            if find_palindrome(row_arr[i], x) or find_palindrome(col_arr[i], x):
                print(f'#{tc}', x)
                break
        else:
            continue
        break

def howmany_charge(k, n, m, lst):
    if (m + 1) * k < n:
        return 0
    
    stage = [0] * (n+1)
    for i in lst:
        stage[i] += 1
    
    count = 0
    x = 0
    while x < n:
        if x + k >= n:
            break
        
        for j in range(x+k, x-1, -1):
            if j == x:
                count = 0
                return 0
            
            if stage[j] == 1:
                count += 1
                x = j
                break
    return count

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int,input().split())
    lst = list(map(int, input().split()))
    result = howmany_charge(k, n, m, lst)
    print(f'#{tc} {result}')
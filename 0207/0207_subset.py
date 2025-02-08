T = int(input())            # 테스트 케이스 개수받고, 1부터 12까지 있는 리스트 arr 생성
arr = range(1,13)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0              # 조건에 만족하는 부분집합 담을 변수 result 생성
    
    for i in range(1<<12):  # 모든 부분집합을 고려
        subset_sum = 0      # 생성할 부분집합의 합과 개수를 담을 변수 생성
        subset_count = 0
        
        for j in range(12): # 부분집합의 원소들을 순회하며 1인 원소들의 개수와 합 계산
            if i & (1<<j):  
                subset_sum += arr[j]
                subset_count += 1
        
        # 조건에 맞는 부분집합이 나타날 경우 result를 증가
        if subset_sum == K and subset_count == N:
            result += 1
            
    print(f'#{tc} {result}')
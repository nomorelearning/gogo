import sys
sys.stdin = open('test.txt', 'r')

num_dict = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
}
T = int(input())



for _ in range(T):
    tc, n = input().split()
    texts = list(input().split())
    n = int(n)
    
    count = [0] * 10
    for i in range(n):
        count[num_dict[texts[i]]] += 1
        
    print(count)
    result = []
    for eng_num in num_dict:
        for _ in range(count[num_dict[eng_num]]):
            result.append(eng_num)
    
    print(tc)
    print(*result)
def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dir_r = [0,1,0,-1]
    dir_c = [1,0,-1,0]
    r = c = 0
    direction = 0
    turn_time = 0
    num = 1

    arr[r][c] = num
    num += 1

    while True:
        if turn_time == 4:
            break
        nr = r + dir_r[direction]
        nc = c + dir_c[direction]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            arr[nr][nc] = num
            r, c = nr, nc
            turn_time = 0
            num += 1
        else:
            turn_right()
            turn_time += 1

    print(f'#{tc}')
    for lst in arr:
        print(*lst)
def solution(maps, start, dest) :
    stack = [start]
    hori = len(maps[0])
    verti = len(maps)

    # 스택에 데이터가 있다면 계속 진행
    while len(stack) > 0 :

        # 스택의 가장 마지막 데이터 추출
        now = stack.pop()
        print(now)
        
        # 정답 여부 검사
        if now == dest :
            return True

        x = now[1]
        y = now[0]

        # 왼쪽으로 이동할 수 있다면
        if x - 1 > -1 :
            # 갈 수 있는 길이라면 스택에 추가하고 방문여부를 2로 표시
            if maps[y][x-1] == 0 :
                stack.append([y,x-1])
                maps[y][x-1] = 2

        # 오른쪽으로 이동할 수 있다면
        if x + 1 < hori :
            # 갈 수 있는 길이라면 스택에 추가하고 방문여부를 2로 표시
            if maps[y][x+1] == 0 :
                stack.append([y,x+1])
                maps[y][x+1] = 2

        # 위로 이동할 수 있다면
        if y - 1 > -1 :
            # 갈 수 있는 길이라면 스택에 추가하고 방문여부를 2로 표시
            if maps[y-1][x] == 0 :
                stack.append([y-1,x])
                maps[y-1][x] = 2

        # 아래로 이동할 수 있다면
        if y + 1 < verti :
            # 갈 수 있는 길이라면 스택에 추가하고 방문여부를 2로 표시
            if maps[y+1][x] == 0 :
                stack.append([y+1,x])
                maps[y+1][x] = 2

    # 스택에 데이터가 없으면 False
    return False


maps = [[0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0]]
start = [0, 0]
dest = [5, 5]

print(solution(maps, start, dest))
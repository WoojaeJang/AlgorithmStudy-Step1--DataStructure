def solution(data, start, dest) :
    # 방문 여부 표시할 리스트 생성
    visited = [False]*max(map(max, data))

    # 시작점 방문
    visited[start-1] = True
    queue = [start]

    answer = 0
    
    # 큐에 데이터가 있다면 계속 진행
    while len(queue) > 0 :

        # 같은 거리에 있는 큐 데이터 갯수
        count = len(queue)

        # 같은 거리에 있는 큐 개수만큼 검사
        for time in range(count) :
            now = queue.pop(0)

            # 정답이 존재하면 값 반환
            if now == dest :
                return answer

            # 연결된 포인트 완전 탐색
            for i in data :
                
                # 방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
                if i[0] == now and visited[i[1]-1] == False :
                    queue.append(i[1])
                    visited[i[1]-1] = True

                # 방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
                elif i[1] == now and visited[i[0]-1] == False :
                    queue.append(i[0])
                    visited[i[0]-1] = True

        # 거리 1 증가
        answer += 1

    return answer


data = [[1, 2], [1, 5], [1, 6], [2, 3], [2, 11], [3, 6], [3, 7], [3, 8], 
        [4, 8], [4, 12], [5, 6], [5, 9], [5, 11], [6, 12],
        [7, 8], [7, 10], [8, 11], [9, 10]]
start = 1
dest = 12
print(solution(data, start, dest))
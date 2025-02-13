# 3주차 - 📏 깊이우선탐색과 너비우선탐색

## [✍ 강의 정리]

### PART 01 깊이우선탐색(DFS)

#### 깊이우선탐색(DFS)란?
- Depth First Search의 약자로 넓이 우선 탐색을 의미
- 하나의 경우의 수에 대하여 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정

<br/>

#### 깊이우선탐색(DFS)의 구조

|||
|---|---|
|![w03_01_01](../images/w03/w03_01_01.png)|![w03_01_02](../images/w03/w03_01_02.png)|
|||
|![w03_01_03](../images/w03/w03_01_03.png)|![w03_01_04](../images/w03/w03_01_04.png)|
|||
|![w03_01_05](../images/w03/w03_01_05.png)|![w03_01_06](../images/w03/w03_01_06.png)|
|||
|![w03_01_07](../images/w03/w03_01_07.png)|![w03_01_08](../images/w03/w03_01_08.png)|
|||
|![w03_01_09](../images/w03/w03_01_09.png)|![w03_01_10](../images/w03/w03_01_10.png)|
|||
|![w03_01_11](../images/w03/w03_01_11.png)|![w03_01_12](../images/w03/w03_01_12.png)|
|||
|![w03_01_13](../images/w03/w03_01_13.png)|![w03_01_14](../images/w03/w03_01_14.png)|

<br/>

#### 깊이우선탐색(DFS)과 스택

||||
|---|---|---|
|![w03_02_01](../images/w03/w03_02_01.png)|![w03_02_02](../images/w03/w03_02_02.png)|![w03_02_03](../images/w03/w03_02_03.png)|
||||
|![w03_02_04](../images/w03/w03_02_04.png)|![w03_02_05](../images/w03/w03_02_05.png)|![w03_02_06](../images/w03/w03_02_06.png)|
||||
|![w03_02_07](../images/w03/w03_02_07.png)|![w03_02_08](../images/w03/w03_02_08.png)|![w03_02_09](../images/w03/w03_02_09.png)|
||||
|![w03_02_10](../images/w03/w03_02_10.png)|![w03_02_11](../images/w03/w03_02_11.png)|![w03_02_12](../images/w03/w03_02_12.png)|
||||
|![w03_02_13](../images/w03/w03_02_13.png)|![w03_02_14](../images/w03/w03_02_14.png)|![w03_02_15](../images/w03/w03_02_15.png)|
||||
|![w03_02_16](../images/w03/w03_02_16.png)|![w03_02_17](../images/w03/w03_02_17.png)|![w03_02_18](../images/w03/w03_02_18.png)|
||||
|![w03_02_19](../images/w03/w03_02_19.png)|![w03_02_20](../images/w03/w03_02_20.png)|![w03_02_21](../images/w03/w03_02_21.png)|
||||
|![w03_02_22](../images/w03/w03_02_22.png)|![w03_02_23](../images/w03/w03_02_23.png)|![w03_02_24](../images/w03/w03_02_24.png)|
||||
|![w03_02_25](../images/w03/w03_02_25.png)|![w03_02_26](../images/w03/w03_02_26.png)|![w03_02_27](../images/w03/w03_02_27.png)|

<br/>

#### 깊이우선탐색(DFS) 구현 - 미로찾기

||||
|---|---|---|
|![w03_03_01](../images/w03/w03_03_01.png)|![w03_03_02](../images/w03/w03_03_02.png)|![w03_03_03](../images/w03/w03_03_03.png)|
||||
|![w03_03_04](../images/w03/w03_03_04.png)|![w03_03_05](../images/w03/w03_03_05.png)|![w03_03_06](../images/w03/w03_03_06.png)|
||||
|![w03_03_07](../images/w03/w03_03_07.png)|![w03_03_08](../images/w03/w03_03_08.png)|![w03_03_09](../images/w03/w03_03_09.png)|
||||
|![w03_03_10](../images/w03/w03_03_10.png)|![w03_03_11](../images/w03/w03_03_11.png)|![w03_03_12](../images/w03/w03_03_12.png)|
||||
|![w03_03_13](../images/w03/w03_03_13.png)|![w03_03_14](../images/w03/w03_03_14.png)|![w03_03_15](../images/w03/w03_03_15.png)|
||||
|![w03_03_16](../images/w03/w03_03_16.png)|![w03_03_17](../images/w03/w03_03_17.png)|![w03_03_18](../images/w03/w03_03_18.png)|
||||
|![w03_03_19](../images/w03/w03_03_19.png)|![w03_03_20](../images/w03/w03_03_20.png)|![w03_03_21](../images/w03/w03_03_21.png)|
||||
|![w03_03_22](../images/w03/w03_03_22.png)|![w03_03_23](../images/w03/w03_03_23.png)|![w03_03_24](../images/w03/w03_03_24.png)|
||||
|![w03_03_25](../images/w03/w03_03_25.png)|![w03_03_26](../images/w03/w03_03_26.png)|![w03_03_27](../images/w03/w03_03_27.png)|
||||
|![w03_03_28](../images/w03/w03_03_28.png)|![w03_03_29](../images/w03/w03_03_29.png)|![w03_03_30](../images/w03/w03_03_30.png)|
||||
|![w03_03_31](../images/w03/w03_03_31.png)|![w03_03_32](../images/w03/w03_03_32.png)|![w03_03_33](../images/w03/w03_03_33.png)|
||||
|![w03_03_34](../images/w03/w03_03_34.png)|![w03_03_35](../images/w03/w03_03_35.png)|![w03_03_36](../images/w03/w03_03_36.png)|
||||
|![w03_03_37](../images/w03/w03_03_37.png)|![w03_03_38](../images/w03/w03_03_38.png)|![w03_03_39](../images/w03/w03_03_39.png)|
||||
|![w03_03_40](../images/w03/w03_03_40.png)|![w03_03_41](../images/w03/w03_03_41.png)|![w03_03_42](../images/w03/w03_03_42.png)|
||||
|![w03_03_43](../images/w03/w03_03_43.png)|![w03_03_44](../images/w03/w03_03_44.png)|![w03_03_45](../images/w03/w03_03_45.png)|
||||
|![w03_03_46](../images/w03/w03_03_46.png)|![w03_03_47](../images/w03/w03_03_47.png)|![w03_03_48](../images/w03/w03_03_48.png)|
||||
|![w03_03_49](../images/w03/w03_03_49.png)|![w03_03_50](../images/w03/w03_03_50.png)|![w03_03_51](../images/w03/w03_03_51.png)|
||||
|![w03_03_52](../images/w03/w03_03_52.png)|![w03_03_53](../images/w03/w03_03_53.png)|![w03_03_54](../images/w03/w03_03_54.png)|
||||
|![w03_03_55](../images/w03/w03_03_55.png)|![w03_03_56](../images/w03/w03_03_56.png)|![w03_03_57](../images/w03/w03_03_57.png)|
||||
|![w03_03_58](../images/w03/w03_03_58.png)|![w03_03_59](../images/w03/w03_03_59.png)|![w03_03_60](../images/w03/w03_03_60.png)|
||||
|![w03_03_61](../images/w03/w03_03_61.png)|![w03_03_62](../images/w03/w03_03_62.png)|![w03_03_63](../images/w03/w03_03_63.png)|
||||
|![w03_03_64](../images/w03/w03_03_64.png)|![w03_03_65](../images/w03/w03_03_65.png)|![w03_03_66](../images/w03/w03_03_66.png)|
||||
|![w03_03_67](../images/w03/w03_03_67.png)|||

<br/>

#### 깊이우선탐색(DFS) 예시코드 - 미로찾기

```python
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

```

<br/>

### PART 02 너비우선탐색(BFS)

#### 너비우선탐색(BFS)란?
- Breadth First Search의 약자로 넓이 우선 탐색을 의미
- 하나의 경우의 수에 대한 다음 단계의 모든 경우의 수를 조사하면서 해를 찾는 과정

<br/>

#### 너비우선탐색(BFS)의 구조

|||
|---|---|
|![w03_04_01](../images/w03/w03_04_01.png)|![w03_04_02](../images/w03/w03_04_02.png)|
|||
|![w03_04_03](../images/w03/w03_04_03.png)|![w03_04_04](../images/w03/w03_04_04.png)|
|||
|![w03_04_05](../images/w03/w03_04_05.png)|![w03_04_06](../images/w03/w03_04_06.png)|
|||
|![w03_04_07](../images/w03/w03_04_07.png)|![w03_04_08](../images/w03/w03_04_08.png)|
|||
|![w03_04_09](../images/w03/w03_04_09.png)|![w03_04_10](../images/w03/w03_04_10.png)|
|||
|![w03_04_11](../images/w03/w03_04_11.png)|![w03_04_12](../images/w03/w03_04_12.png)|

<br/>

#### 너비우선탐색(BFS)과 큐

||||
|---|---|---|
|![w03_05_01](../images/w03/w03_05_01.png)|![w03_05_02](../images/w03/w03_05_02.png)|![w03_05_03](../images/w03/w03_05_03.png)|
||||
|![w03_05_04](../images/w03/w03_05_04.png)|![w03_05_05](../images/w03/w03_05_05.png)|![w03_05_06](../images/w03/w03_05_06.png)|
||||
|![w03_05_07](../images/w03/w03_05_07.png)|![w03_05_08](../images/w03/w03_05_08.png)|![w03_05_09](../images/w03/w03_05_09.png)|
||||
|![w03_05_10](../images/w03/w03_05_10.png)|![w03_05_11](../images/w03/w03_05_11.png)|![w03_05_12](../images/w03/w03_05_12.png)|
||||
|![w03_05_13](../images/w03/w03_05_13.png)|![w03_05_14](../images/w03/w03_05_14.png)|![w03_05_15](../images/w03/w03_05_15.png)|
||||
|![w03_05_16](../images/w03/w03_05_16.png)|![w03_05_17](../images/w03/w03_05_17.png)|![w03_05_18](../images/w03/w03_05_18.png)|
||||
|![w03_05_19](../images/w03/w03_05_19.png)|![w03_05_20](../images/w03/w03_05_20.png)|![w03_05_21](../images/w03/w03_05_21.png)|

<br/>

#### 너비우선탐색(BFS) 구현 - 최단경로찾기

||||
|---|---|---|
|![w03_06_01](../images/w03/w03_06_01.png)|![w03_06_02](../images/w03/w03_06_02.png)|![w03_06_03](../images/w03/w03_06_03.png)|
||||
|![w03_06_04](../images/w03/w03_06_04.png)|![w03_06_05](../images/w03/w03_06_05.png)|![w03_06_06](../images/w03/w03_06_06.png)|
||||
|![w03_06_07](../images/w03/w03_06_07.png)|![w03_06_08](../images/w03/w03_06_08.png)|![w03_06_09](../images/w03/w03_06_09.png)|
||||
|![w03_06_10](../images/w03/w03_06_10.png)|![w03_06_11](../images/w03/w03_06_11.png)|![w03_06_12](../images/w03/w03_06_12.png)|
||||
|![w03_06_13](../images/w03/w03_06_13.png)|![w03_06_14](../images/w03/w03_06_14.png)|![w03_06_15](../images/w03/w03_06_15.png)|
||||
|![w03_06_16](../images/w03/w03_06_16.png)|![w03_06_17](../images/w03/w03_06_17.png)|![w03_06_18](../images/w03/w03_06_18.png)|
||||
|![w03_06_19](../images/w03/w03_06_19.png)|![w03_06_20](../images/w03/w03_06_20.png)|![w03_06_21](../images/w03/w03_06_21.png)|
||||
|![w03_06_22](../images/w03/w03_06_22.png)|![w03_06_23](../images/w03/w03_06_23.png)|![w03_06_24](../images/w03/w03_06_24.png)|
||||
|![w03_06_25](../images/w03/w03_06_25.png)|![w03_06_26](../images/w03/w03_06_26.png)|![w03_06_27](../images/w03/w03_06_27.png)|

<br/>

#### 너비우선탐색(BFS) 예시코드 - 최단경로찾기

```python
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

```

<br/><br/>

## [🥇 문제풀이]

### W03_1_DFS와 BFS
- [문제 원본 보기](https://www.acmicpc.net/problem/1260)
- [풀이 보기](./../code/practice/prc_w03_1_DFS와BFS.py)

<br/>

### W03_2_바이러스
- [문제 원본 보기](https://www.acmicpc.net/problem/2606)
- [풀이 보기](./../code/practice/prc_w03_2_바이러스.py)

<br/>

### W03_3_타겟 넘버
- [문제 원본 보기](https://www.acmicpc.net/problem/10816)
- [풀이 보기](./../code/practice/prc_w03_3_타겟넘버.py)
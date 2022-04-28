def my_solution(N, M, V, data) :

    def get_DFS(N, M, V, data) : 

        stack = []
        visited = [False]*N
        stack.append(V)

        answer_DFS = []
        while len(stack) > 0:

            if visited == [True]*N :
                break
            
            now = stack.pop()

            if visited[now-1] == False :
                visited[now-1] = True
                answer_DFS.append(str(now))

                temp = []
                for line in data :
                    if (line[0] == now) & (visited[line[1]-1] == False) :
                        temp.append(line[1])
                    elif (line[1] == now) & (visited[line[0]-1] == False) :
                        temp.append(line[0])
                stack += sorted(temp, reverse=True)

        return answer_DFS

    def get_BFS(N, M, V, data) :
        
        queue = []
        visited = [False]*N
        queue.append(V)
        visited[V-1] = True

        answer_BFS = []
        while len(queue) > 0:
            
            now = queue.pop(0)
            answer_BFS.append(str(now))
            
            temp = []
            for line in data :
                if (line[0] == now) & (visited[line[1]-1] == False) :
                    temp.append(line[1])
                    visited[line[1]-1] = True
                elif (line[1] == now) & (visited[line[0]-1] == False) :
                    temp.append(line[0])
                    visited[line[0]-1] = True

            queue += sorted(temp)

        return answer_BFS



    print(" ".join(get_DFS(N, M, V, data)))
    print(" ".join(get_BFS(N, M, V, data)))




# if __name__ == "__main__" :

N, M, V = list(map(int, input().split()))
data = []
for i in range(M) :
    data.append(list(map(int, input().split())))

my_solution(N, M, V, data)


def my_solution(N, data) :
    
    stack = []
    visited = [False]*N
    
    stack.append(1)
    
    answer = -1
    while len(stack) > 0 :
        
        now = stack.pop()
        if visited[now-1] == False :
            
            visited[now-1] = True
            answer += 1
            
            for s in data :
                if (s[0] == now) & (visited[s[1]-1] == False) :
                    stack.append(s[1])
                    
                elif (s[1] == now) & (visited[s[0]-1] == False) :
                    stack.append(s[0])
                                
    print(answer)


if __name__ == "__main__" :

    N = int(input())
    S = int(input())
    data = []
    for i in range(S) :
        data.append(list(map(int, input().split())))
        
    my_solution(N, data)
# 나의 풀이
def my_solution(progresses, speeds):
    befo_day = [(100-progresses[i])//speeds[i] + 1 if (100-progresses[i])%speeds[i] != 0 else (100-progresses[i])//speeds[i] for i in range(len(progresses))]
    
    answer = []
    idx = -1
    max_day = -1
    if len(befo_day) != 0 :   
        for day in befo_day :
            if day > max_day :
                idx += 1
                max_day = day            
                answer.append(1)
            else :
                answer[idx] += 1
            
    return answer
'''
실수만 줄이면 될듯하다...
'''


# 미친 모범 답안
def good_solution_1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''
이건 도데체 어떻게 떠오르냐.... 대단...
'''


if __name__ == "__main__" :
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    
    print(my_solution(progresses, speeds))
    print(good_solution_1(progresses, speeds))
    
    
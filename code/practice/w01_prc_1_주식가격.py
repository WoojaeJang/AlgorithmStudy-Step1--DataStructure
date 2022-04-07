# 처음 나의 풀이
def solution(prices):
    
    answer = []
    
    while prices :
        p1 = prices.pop(0)
        count = 0
        for p2 in prices :
            count += 1
            if p1 > p2 :
                break
        answer.append(count)
    return answer
'''
효율성 도저히 해결되지 않아 찾아보았다.
다 똑같고 deque를 사용하는 활용하는 풀이가 있길래
기존에 price를 deque(price)로만 바꾸었다.
'''



# deque 활용
from collections import deque

def solution(prices):
    
    queue = deque(prices)
    answer = []
    
    while queue :
        p1 = queue.popleft()
        count = 0
        for p2 in queue :
            count += 1
            if p1 > p2 :
                break
        answer.append(count)
    return answer

'''
진짜 너무 짜증나는게 왜 이건되고
내가 한건 안되는지... 진짜 열받는다...
아직도 모르곗다...
'''



# pop 안쓰고 풀기
def solution(prices):
    answer = [0]*len(prices)
    
    for i in range(len(prices)-1) :
        p1 = prices[i]
        for j in range(i+1, len(prices)) :
            answer[i]+=1
            p2 = prices[j]
            if p1 > p2 :
                break             
    
    return answer

'''
스택 큐라고 해서 굳이 pop 쓰려고 안해도 될듯싶다.
'''

def solution(trump) :
    for i in range(len(trump)) :
        if trump[i] == 8 :
            return i
    return -1


trump = [9, 'A', 8, 5, 7, 3, 'K', 'J']
print(solution(trump))
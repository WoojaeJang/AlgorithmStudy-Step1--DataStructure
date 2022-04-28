def solution(trump, loc) :
    if trump[loc] == 8 :
        return loc
    else :
        return solution(trump, loc+1)


trump = [9, 'A', 8, 5, 7, 3, 'K', 'J']
print(solution(trump, 0))
from itertools import permutations

def my_solution(numbers):
    
    numbers_permu_list = []
    for nn in range(len(numbers)) :
        numbers_permu_list += (list(permutations(numbers, nn+1)))
    
    numbers_list = sorted(list(set([int(''.join(permu_set)) for permu_set in numbers_permu_list if int(''.join(permu_set)) > 1])))
    
    answer = 0
    for number in numbers_list :
        x = 0
        for d in range(2, (int(number**(1/2)))+1) :
            if number%d == 0 :
                x += 1
        if x == 0 :
            answer += 1
    
    return answer
'''
너무 어렵다...
'''

from itertools import permutations
def good_solution_1(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''
map 사용과 에라토스테네스체 지린다...
'''

def good_solution_2(numbers):
    
    primeSet = set()
    
    def isPrime(number):
        if number in (0, 1):
            return False
        for i in range(2, number):
            if number % i == 0:
                return False

        return True
    
    def makeCombinations(str1, str2):
        if str1 != "":
            if isPrime(int(str1)):
                primeSet.add(int(str1))

        for i in range(len(str2)):
            makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])
    
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer
'''
재귀함수 미쳤음...
'''


if __name__ == "__main__" :
    
    numbers = "17"
    
    print(my_solution(numbers))
    print(good_solution_1(numbers))
    print(good_solution_2(numbers))

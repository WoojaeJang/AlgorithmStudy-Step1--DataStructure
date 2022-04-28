def my_solution(numbers, target):
    
    data = [[numbers[0]], [-numbers[0]]]
    for n in numbers[1:] :
        copy1 = [d+[n] for d in data]
        copy2 = [d+[-n] for d in data]
        data = copy1 + copy2
    
    answer = len([x for x in list(map(sum, data)) if x == target])
    return answer


def good_solution_1(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return good_solution_1(numbers[1:], target-numbers[0]) + good_solution_1(numbers[1:], target+numbers[0])


from itertools import product
def good_solution_2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

 

if __name__ == "__main__" :
    numbers = [1, 1, 1, 1, 1]
    target = 3
    
    print(my_solution(numbers, target))
    print(good_solution_1(numbers, target))
    print(good_solution_2(numbers, target))
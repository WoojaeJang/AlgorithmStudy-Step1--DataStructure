def my_solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]*((len(answers)-1)//5 + 1)
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]*((len(answers)-1)//8 + 1)
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*((len(answers)-1)//10 + 1)
    
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(answers)) :
        if answers[i] == s1[i] :
            num1 += 1
        if answers[i] == s2[i] :
            num2 += 1
        if answers[i] == s3[i] :
            num3 += 1
    
    answer_num_list = [num1, num2, num3]
    
    for i, n in enumerate(answer_num_list) :
        if n == max(answer_num_list) :
            answer.append(i+1)
            
    return answer

def good_solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

if __name__ == "__main__" :
    
    answers = [1,3,2,4,2]
    
    print(my_solution(answers))
    print(good_solution(answers))
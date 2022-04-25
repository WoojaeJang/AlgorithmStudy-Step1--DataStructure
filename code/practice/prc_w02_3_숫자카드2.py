def my_solution(N_Cards, M_Cards) :

    N_Cards_dict = {}
    for N_Card in N_Cards :
        if N_Card in N_Cards_dict.keys() :
            N_Cards_dict[N_Card] += 1
        else :
            N_Cards_dict[N_Card] = 1

    N_Cards_dict_key = list(N_Cards_dict.keys())

    for M_Card in M_Cards :
        count = 0
        left_idx = 0
        right_idx = len(N_Cards_dict_key)-1
        while left_idx <= right_idx :
            mid_idx = (left_idx + right_idx)//2
            if M_Card == N_Cards_dict_key[mid_idx] :
                count = N_Cards_dict[N_Cards_dict_key[mid_idx]]
                break
            elif M_Card > N_Cards_dict_key[mid_idx]  :
                left_idx = mid_idx + 1
            else :
                right_idx = mid_idx - 1
        print(count, end=" ")



def my_solution2(N_Cards, M_Cards) :

    N_Cards_dict = {}
    for N_Card in N_Cards :
        if N_Card in N_Cards_dict.keys() :
            N_Cards_dict[N_Card] += 1
        else :
            N_Cards_dict[N_Card] = 1

    N_Cards_dict_key = list(N_Cards_dict.keys())

    for M_Card in M_Cards :
        count = 0
        try :
            count = N_Cards_dict[M_Card]
        except :
            pass
        print(count, end=" ")


if __name__ == "__main__" :

    N = int(input())
    N_Cards = sorted(list(map(int, input().split(" "))))
    M = int(input())
    M_Cards = list(map(int, input().split(" ")))

    my_solution(N_Cards, M_Cards)
    print()

    my_solution2(N_Cards, M_Cards)
    print()
def solution(trump) :
    # 함수 시작 시 left, right 선언
    left = 0
    right = len(trump) - 1

    # left가 right보다 작거나 같으면 계속 실행
    while(left <= right) :
        
        # mid값 계산
        mid = (left+right)//2

        # 정답을 찾으면 정답 반환
        if trump[mid] == 8 :
            return mid

        # 정답보다 작을 경우 left를 mid + 1 로
        elif trump[mid] < 8 :
            left = mid + 1

        # 정답보다 클 경우 right를 mid-1 로
        elif trump[mid] > 8 :
            right = mid - 1

    return mid


trump = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution(trump))
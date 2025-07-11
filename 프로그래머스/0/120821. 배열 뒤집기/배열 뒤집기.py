def solution(num_list):
    # 리스트 길이 저장
    n = len(num_list)

    # 리스트의 절반만 순회하여 양 끝 요소를 교환
    for i in range(n // 2):  
        p = n - i - 1  # 반대쪽 요소의 인덱스
        num_list[i], num_list[p] = num_list[p], num_list[i]  # 값 교환

    return num_list  # 뒤집힌 리스트 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5]))        # [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 2]))        # [2, 1, 1, 1, 1]
def solution(array):
    # 배열에서 가장 큰 값을 찾음
    max_value = max(array)
    
    # 가장 큰 값의 인덱스를 찾음
    max_index = array.index(max_value)
    
    # 결과를 리스트 형태로 반환
    return [max_value, max_index]

# 테스트 예제 실행
print(solution([1, 8, 3]))  # [8, 1]
print(solution([9, 10, 11, 8]))  # [11, 2]
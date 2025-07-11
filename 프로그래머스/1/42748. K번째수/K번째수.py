def solution(array, commands):
    # 결과를 저장할 리스트 초기화
    answer = []

    # commands 리스트를 순회하면서 각 연산 수행
    for c in commands:
        # i번째부터 j번째까지 배열을 슬라이싱하고 정렬
        slice = sorted(array[c[0]-1:c[1]])  
        # 정렬된 리스트에서 k번째 요소를 선택하여 결과 리스트에 추가
        answer.append(slice[c[2]-1])  

    # 최종 결과 반환
    return answer

if __name__ == "__main__":
    # ✅ 예제 테스트 실행
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  
    # 결과: [5, 6, 3] (각각의 연산 수행 결과)
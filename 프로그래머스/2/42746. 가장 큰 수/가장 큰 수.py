def solution(numbers):
    # 숫자들을 문자열로 변환
    num_strs = list(map(str, numbers))

    # 커스텀 정렬 (문자열 비교를 활용)
    sorted_numbers = sorted(num_strs, key=lambda x: x * 10, reverse=True)

    # 정렬된 리스트를 이어붙여 최종 결과 생성
    result = "".join(sorted_numbers)

    # 결과가 "000" 같은 경우 "0" 반환
    return result if result[0] != "0" else "0"

# ✅ 예제 테스트 실행
print(solution([6, 10, 2]))  # 결과: "6210"
print(solution([3, 30, 34, 5, 9]))  # 결과: "9534330"
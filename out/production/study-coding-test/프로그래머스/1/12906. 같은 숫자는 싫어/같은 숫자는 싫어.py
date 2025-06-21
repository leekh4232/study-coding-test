def solution(arr):
    answer = []
    previous = None             # 이전 숫자를 저장할 변수 초기화

    for num in arr:
        if num != previous:     # 현재 숫자가 이전 숫자와 다르면 추가
            answer.append(num)
            previous = num      # 이전 숫자를 현재 숫자로 업데이트

    return list(answer)


# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # 결과: [1, 3, 0, 1]
    print(solution([4, 4, 4, 3, 3]))        # 결과: [4, 3]
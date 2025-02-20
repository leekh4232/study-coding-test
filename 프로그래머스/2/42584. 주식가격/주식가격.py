def solution(prices):
    n = len(prices)  # 주식 가격 배열의 길이
    answer = [0] * n  # 결과 배열 초기화

    for i in range(n):  # 각 시점별 가격 확인
        for j in range(i + 1, n):  # 이후 가격과 비교
            answer[i] += 1
            if prices[i] > prices[j]:  # 가격이 떨어지면 중단
                break

    return answer

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))  # 결과: [4, 3, 1, 1, 0]
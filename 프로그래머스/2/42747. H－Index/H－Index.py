def solution(citations):
    # 인용 횟수를 내림차순 정렬
    citations.sort(reverse=True)

    # H-Index를 저장할 변수
    answer = 0

    # 정렬된 리스트를 순회하며 H-Index 계산
    for i in range(len(citations)):
        if citations[i] >= i + 1:  # 현재 논문의 인용 횟수가 (i+1)번 이상이면 조건 만족
            answer = i + 1  # H-Index 업데이트
        else:
            break  # 조건을 만족하지 않으면 종료

    # 최종 H-Index 반환
    return answer

if __name__ == '__main__':
    # ✅ 예제 테스트 실행
    print(solution([3, 0, 6, 1, 5]))  # 결과: 3 (H-Index)
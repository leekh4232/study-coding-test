def solution(people, limit):
    # 구명보트의 수를 저장할 변수 초기화
    answer = 0

    # 사람들의 몸무게를 오름차순으로 정렬
    people.sort()

    # 가장 가벼운 사람을 가리키는 포인터
    S = 0
    # 가장 무거운 사람을 가리키는 포인터
    E = len(people) - 1

    # 두 포인터가 만나거나 교차할 때까지 반복
    while S <= E:
        # 구명보트 하나 사용
        answer += 1

        # 가장 가벼운 사람과 가장 무거운 사람의 합이 제한 이내라면
        if people[S] + people[E] <= limit:
            S += 1  # 가벼운 사람도 보트에 태움
            E -= 1  # 무거운 사람도 보트에 태움
        else:
            E -= 1  # 무거운 사람만 단독으로 보트에 태움

    # 필요한 구명보트의 수 반환
    return answer

# 테스트 케이스 실행
print(solution([70, 50, 80, 50], 100))  # 결과: 3
print(solution([70, 80, 50], 100))      # 결과: 3

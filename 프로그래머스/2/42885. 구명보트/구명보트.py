def solution(people, limit):
    # 구명보트의 수를 저장할 변수 초기화
    answer = 0

    # 사람들의 몸무게를 오름차순으로 정렬
    people.sort()
    # 가장 가벼운 사람의 인덱스
    i = 0
    # 가장 무거운 사람의 인덱스
    j = len(people) - 1

    # 두 인덱스가 만나거나 교차할 때까지 반복
    while i <= j:
        # 구명보트 하나 추가
        answer += 1
        # 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 제한 이하인 경우
        if people[i] + people[j] <= limit:
            # 가장 가벼운 사람을 태우고 인덱스 증가
            i += 1
            # 가장 무거운 사람을 태우고 인덱스 감소
            j -= 1
        else:
            # 가장 무거운 사람만 태우고 인덱스 감소
            j -= 1

    # 필요한 구명보트의 수 반환
    return answer

if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))  #3
    print(solution([70, 80, 50], 100))      #3
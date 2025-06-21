def solution(answers):
    # 수포자 1번의 찍는 패턴
    pattern1 = [1, 2, 3, 4, 5]
    # 수포자 2번의 찍는 패턴
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 수포자 3번의 찍는 패턴
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자의 점수를 저장할 리스트 (1번, 2번, 3번 순서)
    score = [0, 0, 0]

    # 결과를 저장할 리스트
    result = []

    # 정답 리스트를 하나씩 순회하며
    for idx, answer in enumerate(answers):
        # 수포자 1번의 현재 인덱스에 해당하는 패턴 값과 정답이 같은 경우 점수 +1
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        # 수포자 2번
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        # 수포자 3번
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    # 가장 높은 점수를 구함
    maxScore = max(score)

    # 최고 점수를 받은 수포자를 찾아 result 리스트에 저장
    for idx, s in enumerate(score):
        if s == maxScore:
            # 수포자 번호는 인덱스 + 1
            result.append(idx + 1)

    # 결과 리스트 반환
    return result

# 테스트 케이스 실행
print(solution([1, 2, 3, 4, 5]))  # 출력 -> [1]
print(solution([1, 3, 2, 4, 2]))  # 출력 -> [1, 2, 3]
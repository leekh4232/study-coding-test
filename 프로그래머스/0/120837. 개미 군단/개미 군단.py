def solution(hp):
    # 장군개미 (5의 공격력) 사용 개수 계산
    general = hp // 5
    remainder = hp % 5  # 남은 체력

    # 병정개미 (3의 공격력) 사용 개수 계산
    soldier = remainder // 3
    worker = remainder % 3  # 남은 체력 (일개미가 담당)

    return general + soldier + worker  # 총 개미 수 반환

# ✅ 예제 테스트 실행
print(solution(23))  # 결과: 5
print(solution(24))  # 결과: 6
print(solution(999)) # 결과: 201
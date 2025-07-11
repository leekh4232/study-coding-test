from itertools import permutations

# 숫자야구 문제 해결 함수
def solution(queries: list[list[int, int, int]]) -> int:
    """
    queries: [[guess, strike_expected, ball_expected], ...]
    - guess: 민혁이가 질문한 숫자 (예: 123)
    - strike_expected, ball_expected: 영수가 답한 스트라이크와 볼 수
    """
    # 가능한 모든 세 자리 숫자 생성 (1~9까지의 숫자 중 3개를 순열로)
    candidates = [''.join(p) for p in permutations('123456789', 3)]

    # 조건을 만족하는 숫자의 개수를 세기 위한 변수
    count = 0

    # 각 후보 숫자에 대해 모든 질문 조건을 검사
    for cand in candidates:
        ok = True           # 현재 후보가 가능한 숫자인지 판별하는 플래그

        for q, s_exp, b_exp in queries:  # 각 질문에 대해 검사
            guess = str(q)               # 질문 숫자를 문자열로 변환

            # 스트라이크 개수 계산: 같은 자리에서 같은 숫자인 경우
            strike = sum(c1 == c2 for c1, c2 in zip(cand, guess))

            # 볼 개수 계산: 숫자는 포함되어 있지만 자리 위치는 다른 경우
            ball = sum(c in cand for c in guess) - strike

            # 영수가 말한 예상 strike, ball 수와 다르면 후보 제외
            if strike != s_exp or ball != b_exp:
                ok = False
                break

        # 모든 조건을 만족하는 경우 count 증가
        if ok: count += 1

    # 가능한 후보 개수 반환
    return count

# 테스트 실행
print(solution([ [123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1] ]))

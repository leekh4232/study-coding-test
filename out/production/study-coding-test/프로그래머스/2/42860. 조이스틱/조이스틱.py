def solution(name):
    # 알파벳을 변경하는 데 필요한 총 조작 횟수를 저장할 변수
    spell_move = 0

    # 기본 커서 이동 횟수: 문자열의 맨 끝까지 이동하는 경우
    cursor_move = len(name) - 1

    # 이름의 각 문자에 대해 순회
    for i, spell in enumerate(name):
        # 현재 문자를 만들기 위해 필요한 상하 이동 횟수(▲ 또는 ▼ 중 작은 값 선택)
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)

        # 다음 인덱스부터 연속된 'A' 구간 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 커서 이동 최적화
        # 아래 세 가지 방법 중 최소 이동을 선택
        # 1. 초기 커서 이동 (오른쪽으로 쭉 이동)
        # 2. 현재 위치까지 이동 → 왼쪽으로 돌아가기 → 마지막까지 이동
        # 3. 끝까지 이동 → 연속된 A 이후를 다시 왼쪽으로 돌아오기
        cursor_move = min([cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경 횟수와 최적 커서 이동 횟수를 합산하여 결과 반환
    return spell_move + cursor_move

# 테스트 케이스 실행
print(solution("JEROEN"))   # 결과: 56
print(solution("JAN"))      # 결과: 23
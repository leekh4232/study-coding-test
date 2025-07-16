def solution(data, col, rowBegin, rowEnd):
    # col-1은 파이썬의 0-based 인덱스에 맞추기 위한 조정이다.
    # 람다 함수는 정렬의 기준을 정의한다.
    # 첫 번째 기준으로 col-1번째 컬럼의 값을 사용하고 오름차순 정렬한다.
    # 만약 col-1번째 컬럼의 값이 같다면, 두 번째 기준으로 첫 번째 컬럼(0번째)의 값을 사용하고 내림차순 정렬한다.
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 최종 결과를 저장할 변수를 0으로 초기화한다.
    answer = 0

    # rowBegin과 rowEnd는 1-based 인덱스이므로, 파이썬 리스트의 0-based 인덱스에 맞추기 위해 1을 빼준다.
    # range 함수의 끝 값은 포함되지 않으므로, rowEnd는 그대로 사용하면 rowEnd-1까지 반복한다.
    for i in range(rowBegin - 1, rowEnd):
        # 현재 처리 중인 행의 1-based 번호를 계산한다.
        rowNumber = i + 1

        # 현재 행의 S_i 값을 저장할 변수를 0으로 초기화한다.
        si = 0
        # 현재 행 (data[i])의 각 원소를 반복하여 접근한다.
        for element in data[i]:
            # 각 원소를 현재 행 번호로 나눈 나머지를 si에 더한다.
            si += (element % rowNumber)

        # 만약 현재 행이 범위 내의 첫 번째 행이라면,
        # si 값을 answer에 직접 할당한다.
        if i == rowBegin - 1:
            answer = si
        # 첫 번째 행이 아니라면,
        # 현재 si 값을 기존 answer와 XOR 연산하여 answer를 갱신한다.
        else:
            answer ^= si

    # 모든 계산이 완료된 후 최종 answer 값을 반환한다.
    return answer
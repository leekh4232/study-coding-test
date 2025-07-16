def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])
    # 찾아낸 후보 키들을 저장할 리스트
    candidate_keys = []

    # 모든 가능한 속성 조합(부분집합)을 순회
    # mask는 1부터 (1 << col_count) - 1 까지 증가
    for mask in range(1, 1 << col_count):
        # 최소성(Minimality) 검사
        # 현재 mask가 이미 찾아낸 후보 키의 상위 집합인지 확인
        # (mask & key) == key는 key가 mask의 부분집합임을 의미
        if any((mask & key) == key for key in candidate_keys):
            continue

        # 유일성(Uniqueness) 검사
        # 현재 mask에 해당하는 속성들로 구성된 튜플들을 저장할 set
        unique_tuples = set()
        for r in range(row_count):
            # 결과를 담을 임시 리스트 생성
            selected_values = []

            # 0부터 전체 컬럼 개수(col_count) - 1 까지 반복
            for j in range(col_count):
                # 현재 컬럼(j)이 mask에 포함되어 있는지 확인
                # (mask >> j) & 1 연산의 결과가 1이면 포함된 것
                if (mask >> j) & 1:
                    # 포함되었다면, 현재 행(r)의 j번째 컬럼 값을 리스트에 추가
                    selected_values.append(relation[r][j])

            # 리스트를 튜플로 변환
            tpl = tuple(selected_values)
            
            unique_tuples.add(tpl)

        # set의 크기가 전체 행의 개수와 같다면 모든 튜플이 유일
        if len(unique_tuples) == row_count:
            candidate_keys.append(mask)
            
    # 최종적으로 찾아낸 후보 키의 개수를 반환
    return len(candidate_keys)
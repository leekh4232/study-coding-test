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
            # 선택된 컬럼(j)들의 값으로 튜플을 생성
            tpl = tuple(relation[r][j] for j in range(col_count) if (mask >> j) & 1)
            unique_tuples.add(tpl)

        # set의 크기가 전체 행의 개수와 같다면 모든 튜플이 유일
        if len(unique_tuples) == row_count:
            candidate_keys.append(mask)
            
    # 최종적으로 찾아낸 후보 키의 개수를 반환
    return len(candidate_keys)
def solution(n):
    # 1. 숫자를 문자열로 변환하여 리스트로 저장
    k = list(str(n))

    # 2. 리스트 크기 및 반절 위치 구하기
    size = len(k)
    half = size // 2

    # 3. 리스트를 직접 뒤집는 과정 (swap 방식)
    for i in range(half):
        p = size - i - 1  # 반대쪽 인덱스 계산

        # 두 값을 교환 (swap)
        a = k[i]
        k[i] = k[p]
        k[p] = a

    # 4. 문자열 리스트를 정수 리스트로 변환하여 반환
    return list(map(int, k))

# ✅ 예제 테스트 실행
if __name__ == '__main__':
    n = 12345
    print(solution(n))  # 결과: [5, 4, 3, 2, 1]
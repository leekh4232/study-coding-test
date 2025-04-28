def solution(n, lost, reserve):
    # 도난당한 학생 목록과 여벌이 있는 학생 목록을 번호순으로 정렬
    lost.sort()
    reserve.sort()

    # 도난당했지만 여벌도 있는 학생은 lost와 reserve 모두에서 제거
    for i in reserve[:]:      # reserve 리스트를 복사하여 순회
        if i in lost:         # 여벌을 가진 학생이 도난당한 경우
            reserve.remove(i) # reserve 리스트에서 제거
            lost.remove(i)    # lost 리스트에서도 제거

    # 남은 reserve 리스트를 순회하면서 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:       # 앞번호 학생이 체육복이 없는 경우
            lost.remove(i-1)  # 앞번호 학생에게 체육복을 빌려주고 lost에서 제거
        elif i+1 in lost:     # 앞번호 학생이 없고 뒷번호 학생이 체육복이 없는 경우
            lost.remove(i+1)  # 뒷번호 학생에게 체육복을 빌려주고 lost에서 제거

    # 전체 학생 수에서 여전히 체육복이 없는 학생 수를 빼서 결과 반환
    return n - len(lost)

# 테스트 케이스 실행
print(solution(5, [2, 4], [1, 3, 5]))   # 결과: 5
print(solution(5, [2, 4], [3]))         # 결과: 4
print(solution(3, [3], [1]))            # 결과: 2
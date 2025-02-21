n = int(input())            # 정수 입력 (삼각형의 높이 및 너비 설정)

for i in range(n):          # i(행) -> 0부터 n-1까지 반복
    star = ""               # 매 행마다 출력할 별을 저장할 문자열을 초기화

    for j in range(i+1):    # i번째 행에서 출력할 별의 개수 = i+1개
        star += "*"         # 빈 문자열에 별을 하나씩 추가

    print(star)             # 현재 행의 별 출력

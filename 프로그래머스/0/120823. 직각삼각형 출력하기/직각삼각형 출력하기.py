n = int(input())            # 입력값 : 3
    
for i in range(n):          # i(행) -> 0~n 전까지 
    star = ""               # 매 행마다 출력할 내용을 초기화 함
    
    for j in range(i+1):    # 매 행마다 1개씩 출력할 별의 수를 늘림
        star += "*"         # 빈 문자열에 별을 누적해서 연결함 (문자열 덧셈은 연결)

    print(star)             # 행단위 출력
def solution(id_pw, db):
    # 기본적으로 로그인 실패 상태를 가정하고 "fail"로 설정
    answer = 'fail'

    # 데이터베이스(db)의 회원 정보를 하나씩 확인
    for d in db:
        # 입력된 아이디와 회원 정보의 아이디가 같은지 확인
        if id_pw[0] == d[0]:
            # 아이디가 일치하면 비밀번호도 같은지 확인
            if id_pw[1] == d[1]:
                # 아이디와 비밀번호가 모두 일치하면 "login" 반환
                answer = 'login'
            else:
                # 아이디는 맞지만 비밀번호가 다르면 "wrong pw" 반환
                answer = 'wrong pw'

    # 최종적으로 결정된 결과 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
# 결과: "login" (아이디 "meosseugi"와 비밀번호 "1234"가 db에 존재)

print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
# 결과: "wrong pw" (아이디는 존재하지만 비밀번호가 다름)

print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))
# 결과: "fail" (아이디 자체가 존재하지 않음)
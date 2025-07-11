# 전화번호 목록에 접두어 관계가 있는 번호가 있는지 확인하는 함수
def solution(phone_book):

    # 전화번호를 키로 저장할 해시맵 생성
    hash_map = {}

    # 모든 전화번호를 해시맵에 저장 (값은 의미 없음)
    for nums in phone_book:
        hash_map[nums] = 1

    # 각 전화번호마다
    for nums in phone_book:
        # 접두어를 만들기 위한 문자열 초기화
        arr = ""

        # 전화번호의 각 숫자를 순차적으로 더해가며 접두어를 생성
        for num in nums:
            arr += num

            # 접두어가 해시맵에 존재하고, 자기 자신은 아닐 때
            if arr in hash_map and arr != nums:
                # 접두어 관계가 존재하므로 false 반환
                return False

    # 접두어 관계가 없으므로 true 반환
    return True

# 테스트 케이스 실행
print(solution(["119", "97674223", "1195524421"]))   # False
print(solution(["123","456","789"]))   # True
print(solution(["12","123","1235","567","88"]))   # False

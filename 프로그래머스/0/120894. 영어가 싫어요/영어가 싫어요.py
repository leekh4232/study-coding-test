def solution(numbers):
    # 영어 숫자와 실제 숫자의 매핑 리스트 생성
    words = ["zero", "one", "two", "three", "four", 
             "five", "six", "seven", "eight", "nine"]
    
    # 주어진 문자열(numbers)에서 영어 숫자를 실제 숫자로 변환
    for i, v in enumerate(words):
        numbers = numbers.replace(v, str(i))
    
    # 최종적으로 변환된 문자열을 정수로 변환하여 반환
    return int(numbers)

# ✅ 예제 테스트 실행
print(solution("onetwothreefourfivesixseveneightnine"))  
# 결과: 123456789 (영어 숫자가 숫자로 변환됨)

print(solution("onefourzerosixseven"))  
# 결과: 14067 (영어 숫자가 숫자로 변환됨)
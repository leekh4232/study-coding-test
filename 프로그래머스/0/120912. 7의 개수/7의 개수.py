def solution(array):
    # [풀이1]
    # 리스트의 요소를 하나씩 꺼내서 문자열로 변경하여 7인 경우 카운트
    # answer = 0
    #
    # for i in array:
    #     if str(i) == "7":
    #         answer += 1
    #
    # return answer

    # [풀이2]
    # 리스트의 요소를 하나씩 꺼내서 문자열로 변경하여 하나의 문자열로 결합
    # mystr = ""

    # for i in array:
    #     mystr += str(i)

    # 문자열에서 7의 개수를 카운트하여 리턴
    # return mystr.count("7")

    # [풀이3]
    # 파이썬의 str() 함수를 사용하여 리스트를 문자열로 변환후 카운트
    return str(array).count("7")

print(solution([7, 77, 17]))    # 4
print(solution([10, 29]))       # 0
def solution(arr):
    answer = []
    previous = None  # 이전 숫자를 저장할 변수 초기화

    for num in arr:
        if num != previous:  # 현재 숫자가 이전 숫자와 다르면
            answer.append(num)  # answer 리스트에 추가
            previous = num  # 이전 숫자를 현재 숫자로 업데이트

    return answer
def solution(bin1, bin2):
    # int()로 2진수 bin1과 bin2를 10진수로 바꾼다.
    a = int(bin1, 2)
    b = int(bin2, 2)
    
    # 10진수로 바꾼 bin1과 bin2를 더해준다. --> 결과값이 10진수로 생성됨
    # 그 값을 bin()함수에 넣어 2진수로 만든다.
    answer = bin(a+b)
    
    # bin 함수의 리턴값은 2진수를 뜻하는 "0b"가 앞에 붙어서 나오기 때문에
    # 문자열 슬라이싱을 이용하여 2번째부터 끝까지 출력한다.
    answer = answer[2:]
    return answer
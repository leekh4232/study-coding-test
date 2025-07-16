def solution(n, arr1, arr2):
    # 최종적으로 완성된 지도의 각 행을 저장할 리스트
    answer = []

    # 지도의 각 행에 대해 반복
    for i in range(n):
        # arr1[i]와 arr2[i]를 비트 OR 연산하고 이진수 문자열로 변환
        # bin() 함수는 '0b' 접두사를 붙이므로 [2:]로 제거
        binary = bin(arr1[i] | arr2[i])[2:]

        # 이진수 문자열의 길이가 n보다 작을 경우, 앞에 '0'을 채워 길이를 맞춤
        padded = binary.zfill(n)

        # '1'을 '#'으로, '0'을 ' '으로 변환하여 지도 행을 생성
        map_row = padded.replace('1', '#').replace('0', ' ')

        # 변환된 지도 행을 answer 리스트에 추가
        answer.append(map_row)
        
    # 모든 행에 대한 변환이 완료된 answer 리스트를 반환
    return answer
def solution(array):
    if len(array) == 0:
        return -1

    # 빈도 계산을 위한 딕셔너리 준비
    frequency_dict = {}

    # 배열을 순회하며 빈도를 계산
    for num in array:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    # 최대 빈도 및 최빈값 찾기
    max_freq = 0
    mode = -1
    is_unique = True

    for num, freq in frequency_dict.items():
        if freq > max_freq:
            max_freq = freq
            mode = num
            is_unique = True
        elif freq == max_freq:
            is_unique = False

    if is_unique:
        return mode
    return -1
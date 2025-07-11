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
    freq_list = list(frequency_dict.items())
    max_freq = freq_list[0][1]
    max_key = freq_list[0][0]
    is_unique = True

    for i in range(1, len(freq_list)):
        key, freq = freq_list[i]

        if freq > max_freq:
            max_freq = freq
            max_key = key
            is_unique = True
        elif freq == max_freq:
            is_unique = False

    if is_unique:
        answer = max_key
    else:
        answer = -1

    return answer


print(solution([1, 2, 3, 3, 3, 4])) # 3
print(solution([1, 1, 2, 2]))       # -1
print(solution([1]))                # 1
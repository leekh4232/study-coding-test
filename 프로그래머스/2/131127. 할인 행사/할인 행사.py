def solution(want, number, discount):
    from collections import Counter

    # 필요한 제품 목록과 수량을 딕셔너리로 변환
    want_dict = {want[i]: number[i] for i in range(len(want))}
    want_counter = Counter(want_dict)

    # 슬라이딩 윈도우 크기
    window_size = sum(number)
    count = 0

    for i in range(len(discount) - window_size + 1):
        window = discount[i:i + window_size]
        window_counter = Counter(window)

        if all(window_counter[item] >= want_counter[item] for item in want_counter):
            count += 1

    return count
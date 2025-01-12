def solution(name, yearning, photo):
    # 이름과 그리움 점수를 딕셔너리로 매핑
    map_ = {name[i]: yearning[i] for i in range(len(name))}
    
    # 각 사진별로 그리움 점수 합산 계산
    result = [
        sum(map_[person] for person in group if person in map_)
        for group in photo
    ]
    
    return result
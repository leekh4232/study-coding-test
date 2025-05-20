# 참가자 중 완주하지 못한 사람을 찾아 반환하는 함수
def solution(participant, completion):
    # 이름의 해시값을 키로, 이름 자체를 값으로 저장할 딕셔너리
    hashDict = {}

    # 참가자의 해시값 총합
    sumHash = 0

    # 참가자 리스트를 순회하면서 해시값을 누적하고 딕셔너리에 저장
    for part in participant:
        # part 이름의 해시값을 키로, 이름을 값으로 저장
        hashDict[hash(part)] = part

        # 참가자의 해시값을 누적
        sumHash += hash(part)

    # 완주자 리스트를 순회하면서 해시값을 총합에서 차감
    for comp in completion:
        # 완주자의 해시값을 누적값에서 빼기
        sumHash -= hash(comp)

    # 남은 해시값은 완주하지 못한 사람의 해시값
    # 이를 통해 해당 이름을 딕셔너리에서 찾아 반환
    return hashDict[sumHash]

# 테스트 케이스 실행
print(solution(["leo", "kiki", "eden"],
               ["eden", "kiki"]))
# --> leo

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
# --> vinko

print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))
# --> mislav
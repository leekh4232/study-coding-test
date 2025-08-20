from collections import deque

def solution(begin, target, words):
    # 만약 목표 단어가 words 리스트에 없으면 변환 불가능
    if target not in words:
        return 0
    
    # BFS 탐색을 위한 큐와 방문 기록을 위한 set 생성
    # (현재 단어, 변환 단계)를 큐에 저장
    queue = deque([(begin, 0)])
    visited = {begin}
    
    # 두 단어가 한 글자만 다른지 확인하는 헬퍼 함수
    def is_diff_one(word1, word2):
        diff_count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
        return diff_count == 1
    
    # BFS 시작
    while queue:
        # 큐에서 현재 단어와 단계를 꺼냄
        current_word, steps = queue.popleft()
        
        # 현재 단어가 목표 단어와 같으면
        if current_word == target:
            # 최종 단계 수를 반환
            return steps
        
        # words 리스트에 있는 모든 단어를 순회
        for word in words:
            # 해당 단어가 아직 방문하지 않았고, 현재 단어와 한 글자만 다르면
            if word not in visited and is_diff_one(current_word, word):
                # 방문 처리
                visited.add(word)
                # 다음 단어와 다음 단계를 큐에 추가
                queue.append((word, steps + 1))
                
    # 모든 탐색이 끝났는데도 목표 단어에 도달하지 못했으면
    return 0
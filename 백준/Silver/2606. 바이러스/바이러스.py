n = int(input())  # 컴퓨터의 수
k = int(input())  # 연결의 수

# 인접 리스트 초기화
al = [[] for _ in range(n)]
for _ in range(k):
    l1, l2 = map(int, input().split())
    l1 -= 1  # 0-based 인덱스로 변환
    l2 -= 1
    al[l1].append(l2)
    al[l2].append(l1)

# 방문 여부 리스트 및 전역 변수
visited = [False] * n
answer = 0

# DFS 함수
def dfs(start):
    global answer
    visited[start] = True
    for neighbor in al[start]:
        if not visited[neighbor]:
            answer += 1  # 감염된 컴퓨터 수 증가
            dfs(neighbor)

# 1번 컴퓨터(0번 노드)에서 시작
dfs(0)
print(answer)

    
    
#종이의 크기 n
n = int(input())
# n x n 2차원 배열 
graph = [list(map(int, input().split())) for _ in range(n)] 
# 0, 1로만 이루어진 면의 개수
cnt = [0, 0]
# x: 시작 행, y: 시작 열, N: 정사각형 한 변의 길이
def recursive(x, y, N):
    #이전과 다른 값이 발견되면 4분할
    initial = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if graph[i][j] != initial:
                mid = N // 2
                recursive(x, y, mid) #2사분면
                recursive(x, y + mid, mid) #3사분면
                recursive(x + mid, y, mid) #1사분면
                recursive(x + mid, y + mid, mid) #4사분면
                return #다른 값이 발견되었을 경우, 4분할 후 함수 종료
    #모든 면의 요소가 initial로 동일한 경우, 해당 cnt 증가
    #(반복문에서 면 내부의 모든 요소를 조사했는데 동일하지 않은 요소가 없음)
    cnt[initial] += 1 
    
#수행 및 출력               
recursive(0, 0, n)
for i in cnt:
    print(i)
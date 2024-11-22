import sys
sys.setrecursionlimit(10000)

def dfs(x, y, graph, n, m):
    graph[x][y] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny, graph, n, m)

def solve():
    t = int(input()) 
    for _ in range(t):
        m, n, k = map(int, input().split())  
        graph = [[0] * m for _ in range(n)]  
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1  

        count = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:  
                    dfs(i, j, graph, n, m)
                    count += 1  
        print(count)

solve()
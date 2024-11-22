from queue import Queue
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
def bfs(graph, start, visited):
  visited[start] = True
  queue = Queue()
  queue.put(start)
  while not queue.empty():
    s = queue.get()
    print(s, end=' ')
    for i in graph[s]:
      if not visited[i]:
        visited[i] = True
        queue.put(i)

n, m, v = map(int, input().split())
graph = []
for i in range(n+1):
    graph.append([])
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1) 
for adj in graph:
    adj.sort()
visited = [False] * (n+1)
dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)
  
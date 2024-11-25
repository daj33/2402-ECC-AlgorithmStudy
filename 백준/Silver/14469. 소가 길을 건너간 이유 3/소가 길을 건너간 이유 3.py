n = int(input())
l = []
time = 0
for _ in range(n): 
  (s, e) = map(int, input().split())
  l.append((s, e))
l.sort(key = lambda x: x[0])
for item in l:
  if time < item[0]:
    time = item[0]
  time+=item[1]
print(time)
n, m = map(int, input().split())
l = list(map(int, input().split()))
answer = 0 
for i in range(0, len(l)):
  for j in range(i+1, len(l)):
    for k in range(j+1, len(l)):
      result = l[i] + l[j] + l[k]
      if result<=m and result>answer : 
        answer = result
print(answer)
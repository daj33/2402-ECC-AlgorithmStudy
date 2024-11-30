n = int(input())
scores = []
count = 0
for i in range(n):
  s = int(input())
  scores.append(s)
scores.reverse()
for j in range(n-1):
  while(scores[j]<=scores[j+1]):
    count+=1
    scores[j+1]-=1
print(count)
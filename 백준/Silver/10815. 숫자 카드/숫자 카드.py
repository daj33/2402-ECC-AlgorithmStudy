n = int(input())
hv = map(int, input().split())
m = int(input())
cd = map(int, input().split())

dic = {}
for c in cd:
  dic[c] = 0
for h in hv:
  if h in dic:
    dic[h] = 1
for d in dic:
  print(dic[d], end=' ')

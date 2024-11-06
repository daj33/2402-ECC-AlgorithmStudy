n = int(input())
words = set()
answer = []
for i in range(n):
  words.add(input())
answer = list(words)
answer.sort()
answer.sort(key=len)
for word in answer:
  print(word)
  
import sys
input = sys.stdin.readline
n = int(input()) 
count = 0 
r = {}
for _ in range(n):
    c,s= map(str,input().upper().split())
    c = c[:2]  
    
    if c == s : # 도시와 주의 표기가 같으면 SKIP
        continue 
    if (s, c) not in r:
        r[(s,c)] = 0 #(s,c) 가 r에 없을 경우 추가
    r[(s,c)]+=1 
    if (c,s) in r: # (s,c) 와 순서를 바꾼 (c,s) 를 비교해서 special pair를 찾기
         count += r[(c,s)] # 들어 있으면 count에 더해줌 
print(count)
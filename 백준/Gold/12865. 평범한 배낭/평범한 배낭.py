N, K =  map(int, input().split()) #N: 물품의 수, K: 최대 무게
val = [] #물품의 가치 배열
wt = [] #물품의 무게 배열
for i in range(N):
    w, v =  map(int, input().split())
    val.append(v)
    wt.append(w)
#행렬: 0-N(물품의 수) * 0-K(최대 용량)
table = [[0]*(K+1) for _ in range(N + 1)]

for i in range(1, N+1):
    for k in range(1, K+1):
        #i행 물품의 무게가 k열 배낭 무게를 초과하면 이전 물품 값 유지
        if wt[i-1] > k: 
            table[i][k] = table[i-1][k]
        #아닐 경우
        #i행 물품을 포함한 경우와 포함하지 않은 경우 중 큰 값 선택
        else:
            valwith = val[i-1] + table[i-1][k-wt[i-1]]
            #i행 물품 가치 + i행 물품 판단 이전 무게 딱 맞춘 상태의 가치
            valwithout = table[i-1][k]
            table[i][k] = max(valwith, valwithout)
print(table[N][K])

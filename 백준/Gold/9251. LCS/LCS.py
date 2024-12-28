x = input()
y = input()
#행렬: X 문자열 길이+1 Y 문자열 길이+1
t = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
for r in range(1, len(x) + 1):
    for c in range(1, len(y) + 1):
        #X 문자열의 r번째 문자와 Y 문자열의 c번째 문자 비교
        #동일한 경우
        #X 문자열의 r-1번째 문자와 Y 문자열의 c-1번쨰 문자를 비교한 경우 + 1
        #(상대적 위치 고려?!)
        if x[r - 1] == y[c - 1]:
            t[r][c] = t[r - 1][c - 1] + 1
        #동일하지 않은 경우, X 문자열에서 r번째 문자를 제외할지,
        #Y 문자열에서 c번째 문자를 제외할지... 큰 값 선택
        else:
            t[r][c] = max(t[r - 1][c], t[r][c - 1])

print(t[len(x)][len(y)])

            
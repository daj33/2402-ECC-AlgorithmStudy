def backtracking(k):
    global cnt 
    for i in range(N): #N개의 행 수만큼 실행
        if queen(k,i): #k행 i열에 퀸을 놓을 수 있는 경우
            board[k] = i
            if k == N-1: #다 놓았다면 종료하기
                cnt += 1
                return
            else:
                backtracking(k+1) #k행 i열에 퀸을 놓을 수 없는 경우 다음 행으로 이동
def queen(a,b): #배치 가능 판단
    for i in range(a): 
        if board[i] == b or abs(board[i]-b) == abs(i-a): # 같은 열이거나 같은 대각선
            return False 
    return True 

import sys
N = int(sys.stdin.readline())
board = [0]*N #배치된 퀸의 위치를 저장하는 배열(k행 i열)
cnt = 0 #배치된 퀸의 수 
backtracking(0)
print(cnt)

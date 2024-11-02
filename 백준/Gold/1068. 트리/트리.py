import sys


n = int(sys.stdin.readline())


arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))


remove_node = int(sys.stdin.readline())

def dfs(delete, arr):


    arr[delete] = -2

    for i in range(n):

       
        if (arr[i] == delete):
            dfs(i, arr)


dfs(remove_node, arr)


leaf = 0


for i in range(n):

   
    if (arr[i] != -2):

       
        if (i not in arr):

           
            leaf += 1

print(leaf)
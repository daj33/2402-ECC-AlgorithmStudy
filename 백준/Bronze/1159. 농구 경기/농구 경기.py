n = int(input())  
players = []
for i in range(n):
    player = input() 
    players.append(player)

players.sort()  
k = players[0][0]  
c = 0
r = []

for player in players:
    if k == player[0]:
        c += 1
        if c == 5:  
            r.append(k)
    else:
        k = player[0]
        c = 1
if not r: 
    print("PREDAJA")
else: 
    print("".join(r))  

        

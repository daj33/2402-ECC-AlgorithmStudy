def hanoi_tower(n, start, tmp, goal):
    if(n==1):
        print("원판 1: %s --> %s" %(start, goal))
    else:
        hanoi_tower(n-1, start, goal, tmp)
        print("원판 %d: %s --> %s" %(n, start, goal))
        hanoi_tower(n-1, tmp, start, goal)

hanoi_tower(3, "a", "b", "c")       
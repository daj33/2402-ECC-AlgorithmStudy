n = int(input())
for i in range(n):
    string = input()
    words = string.split()
    print(f"Case #{i+1}: ", end="")
    for j in range(len(words)):
        print(words.pop(), end= " ")
    print()
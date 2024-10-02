n = int(input())
string = input()
words = string.split()
temp_s = int(words[0])
temp_b = int(words[0])
for i in range(n-1):
    if (temp_s>=int(words[i+1])):
        temp_s= int(words[i+1])
    if (temp_b<=int(words[i+1])):
        temp_b= int(words[i+1])
print(temp_s, end=" ")
print(temp_b)
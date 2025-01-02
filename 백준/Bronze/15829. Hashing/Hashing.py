l=int(input())
s=input()
sum=0
r=1
#a의 아스키 코드값: 96
for i in range(l):
    c=s[i]
    sum+=(ord(c)-96)*r
    r*=31
print(sum%1234567891)
    
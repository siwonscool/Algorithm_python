number,money=map(int,input().split())
kind=[]
count=0

for i in range(number):
    kind.append(int(input()))

for i in kind[-1:-len(kind)-1:-1]:
    if money>=i:
        count+=money//i
        money-=(money//i)*i

print(count)
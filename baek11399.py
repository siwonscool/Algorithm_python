number=int(input())
time=[]
add=[]
sum=0

time=list(map(int,input().split()))

time.sort()
for i in time:
    sum += i
    add.append(sum)

sum=0

for i in add:
    sum+=i
print(sum)
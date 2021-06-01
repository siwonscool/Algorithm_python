# 입력조건 : 첫째 줄에 N (1 <= N <= 100000) 과 K (2 <= K <=100000)가 공백을 기준으로 하여 각각 자연수로 주어집니다.
# 출력조건 : 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 관정을 수행해야 하는 횟수의 최솟값을 출력

n,k=map(int,input().split())
result=0

while(True):
    target = (n//k)*k
    result += (n-target) #1빼주기
    n=target
    if(n<k):
        break
    result+=1
    n//=k

result += (n-1)
print(result)

# 입력조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다 (1 <= S의 길이 <= 20)
# 출력조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

data = input()
result = int(data[0])
for i in range(1,len(data)):
    num = int(data[i])
    if result > 1 and num > 1:
        result *= num
    else:
        result += num

print(result)
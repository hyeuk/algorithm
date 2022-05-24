
n,k = map(int,input().split()) # n,k을 공백을 기준으로 구분하여 입력 받기

result = 0

while True:
    target = (n//k) * k    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기 
    result += (n-target)
    n = target

    if n<k:  # n이 k보다 작을때(더 이상 나눌 수 없을때) 반복문 탈출
        break

    result += 1  
    n //=k  # k로 나누기


result += (n-1)  # 마지막 남은 수에 대하여 1씩 빼기

print(result)
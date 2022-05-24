n = int(input())

h = list(map(int,input().split()))
h.sort()

group = 0 # 그룹 수 
cnt = 0 # 현재 그룹에 포함되어있는 모험가의 수

for i in h: # 공포도를 낮은 것 부터 하나씩 확인하며
    cnt +=1 # 현재 그룹에 해당 모험가를 포함시키기
    if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group +=1 # 총 그룹의 수 증가시키기
        cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화


print(group) # 총 그룹의 수 출력
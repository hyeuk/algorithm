
num = list(map(int,input()))  


result = 1

for i in num:
    
    
    if i ==0:
        result+=0
    elif i==1:
        result+=1
    else:
        result*=i

print(result)
    



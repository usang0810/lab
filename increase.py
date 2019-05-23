def add(num):
    for i in range(0, 10):
        num = num+1
        print(num)

    return num
    
num = 0
num = add(num)

print('last =',num)
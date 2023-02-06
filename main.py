def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        a,b,j=0,1,1
        while j<i:
            a,b,j = b,a+b,j+1
        return b

for ind in range(100):
    print(f"{ind} - {fibonacci(ind)}")


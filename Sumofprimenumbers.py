def prime(x):
    for i in range(2,x-1):
        if i%2!=0:
            print(i)
n=int(input('enter the n value='))
prime(n)

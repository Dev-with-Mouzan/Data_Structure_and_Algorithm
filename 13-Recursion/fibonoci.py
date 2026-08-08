def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    

if __name__ == "__main__":
    x=int(input("Enter how many terms you want in Fibonacci series: "))
    for i in range(x):
        print(fibo(i), end=" ")

        
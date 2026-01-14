def fict(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fict(n-1)
    

if __name__=="__main__":
    num=int(input("Enter a number: "))
    result=fict(num)
    print(f"The factorial of {num} is {result}")
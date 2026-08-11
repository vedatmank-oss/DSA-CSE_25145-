def fac (n):
    if n < 0 :
        print("Please aenter a +ve number")
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)

n = int(input("Enter a number : "))
print(f"The Factorial of {n} is {fac(n)}")
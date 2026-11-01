def fib(n):
    if(n < 0):
        print("Please enter a +ve number")
        return None
    if (n == 0 or n == 1):
        return n
    else: 
        return fib(n-1)+fib(n-2)
    
n = int(input("Enter the number : "))
for i in range (n+1):
    print(f"{fib(i)}",end = " ")
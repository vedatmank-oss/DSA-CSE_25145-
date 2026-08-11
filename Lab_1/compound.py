def C_Int(p,n,r,t):
    decimal_rate = r/100
    total_amount = p*(1+decimal_rate/n)**(n*t)
    interest_earned = total_amount - p
    return total_amount, interest_earned

p = int(input("Enter the principal amount (₹) : "))
n = int(input("Times compounded per year : "))
r = float(input("Enter the annual interest rate (%) : "))
t = float(input("Enter the number of years : "))


final_balance, pure_interest = C_Int(p, n, r, t)

print("\n--- Financial Breakdown ---")
print(f"Interest Earned: ₹{pure_interest:.2f}")
print(f"Total Balance:   ₹{final_balance:.2f}")

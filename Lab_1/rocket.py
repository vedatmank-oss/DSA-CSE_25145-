def rocket_countdown(n):
    if n == 0:
        print("LAUNCHED! 🚀")
        return
    
    print(n)
    
    rocket_countdown(n - 1)

start_num = int(input("Enter starting countdown number: "))

print("\n--- Starting Countdown ---")
rocket_countdown(start_num)

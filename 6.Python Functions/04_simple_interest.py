def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100


p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time: "))

print("Simple Interest =", calculate_interest(p, r, t))
# A = P(1+r/n)**t
# \(A\) is the final amount, \(P\) is the principal, \(r\) is the annual interest rate (as a decimal), \(n\) is the number of times interest is compounded per year, and \(t\) is the time in years
# principle = int(input("Enter principle amount: "))
# rate = int(input("Enter Rate: "))
# time = int(input('Enter time in years: '))

principle = 0
rate = 0
time = 0
n = 12

while principle <=0:
    principle = float(input("Enter principle amount: "))
    if principle <=0:
        print("principle cant be negetive or zero")
while rate <=0:
    rate = float(input("Enter rate amount: "))
    if rate <=0:
        print("rate cant be negetive or zero")
while time <=0:
    time = int(input("Enter time amount: "))
    if time <=0:
        print("time cant be negetive or zero")

total = principle * ((1 + rate / n)**time)
print(f"Balance after {time} year/s: ${total:.2f}")
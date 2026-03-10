hr = input("Enter hours:")
rt = input("Enter Rate:")
try:
    fh = float(hr)
    fr = float(rt)
except:
    print("Invalid inputs, please type numbers only")
    quit()

if fh <= 40:
    pay = fh * fr
elif fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    pay = reg + otp
print("Pay:", pay)
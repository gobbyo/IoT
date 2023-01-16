num = input("0-9999: ")

digits = [0,0,0,0]
i = len(num)-1
while i >= 0:
    digits[i] = int(num[i])
    i -= 1

print(digits)
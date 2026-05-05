# Password Checker

password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for n in password:
    if n.isdigit():
        digit = True

result.append(digit)

upper = False
for n in password:
    if n.isupper():
        upper = True    

result.append(upper)
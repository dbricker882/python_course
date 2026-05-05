# Password Checker

password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for n in password:
    if n.isdigit():
        digit = True

result["digits"] = digit

upper = False
for n in password:
    if n.isupper():
        upper = True    

result["upper"] = upper

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
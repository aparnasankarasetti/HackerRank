import re
pattern= re.compile(r"(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$")
for _ in range(int(input())):
    if pattern.search(input()):
        print("Valid")
    else:
        print("Invalid")

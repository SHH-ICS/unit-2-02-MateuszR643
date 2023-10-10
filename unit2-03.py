def birthyear(n, a, b):
    a = int(a) + int(b)
    print(n, "was born in ", 2023 - a)

name = input("Name: ")
age = input("Age: ")
birthdaythisyear = input("Did you have a birthday this year (0 if yes, 1 if not)")

birthyear(name, age, birthdaythisyear)
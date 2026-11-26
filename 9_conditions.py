age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

if (age >= 18 and has_id == "yes") or age >= 21:
    print(True)
else:
    print(False)
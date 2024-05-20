num = int(input("enter a number: "))

if 0 < num < 1000:
    length = len(str(num))
    print(f"Number {num} has {length} digits")
else:
    print("why")

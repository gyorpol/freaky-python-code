temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()
result = (temp * 9/5) + 32 if unit == "C" else (temp - 32) * 5/9
print(f"{temp} {unit} is equal to {result:.2f} {'F' if unit == 'C' else 'C'}")

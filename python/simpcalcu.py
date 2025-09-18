print("=== SIMPLE CALCULATOR ===")

input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))

addition = input1 + input2
subtraction = input1 - input2
multiplication = input1 * input2
division = input1 / input2
modulus = input1 % input2
exponentiation = input1 ** input2
floor_division = input1 // input2

print(f"Results for {input1} and {input2}:")
print(f"Addition: {input1} + {input2} = {addition}")
print(f"Subtraction: {input1} - {input2} = {subtraction}")
print(f"Multiplication: {input1} × {input2} = {multiplication}")
print(f"Division: {input1} ÷ {input2} = {division}")
print(f"Modulus: {input1} % {input2} = {modulus}")
print(f"Exponentiation: {input1} ^ {input2} = {exponentiation}")
print(f"Floor Division: {input1} // {input2} = {floor_division}")


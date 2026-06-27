import math

def calculate_circle_area(radius):

    pi_value = math.pi
    area = pi_value * (radius ** 2)
    return area

def calculate_total_due(money, tax_rate):

    total_due = money + (money * tax_rate)
    return total_due

def convert_fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

print("Function 1: Area of a Circle")
print("Enter the radius:")
radius_input = float(input())
area_result = calculate_circle_area(radius_input)

print(f"Output: {round(area_result, 2)}")

print("\nFunction 2: Taxes")
print("Enter the amount of money:")
money_input = float(input())
print("Enter the tax rate as a decimal")
tax_input = float(input())
tax_result = calculate_total_due(money_input, tax_input)

print(f"Output: {tax_result:.2f}")

print("\nFunction 3: Temperature")
print("Enter the temperature in Fahrenheit:")
fah_input = float(input())
celsius_result = convert_fahrenheit_to_celsius(fah_input)

if celsius_result == 0:
    print("Output: 0")
else:
    print(f"Output: {round(celsius_result, 5)}")
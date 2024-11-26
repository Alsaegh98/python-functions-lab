# example 1

def calculate_area_triangle(base, height):
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5)) 

# example 2

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2)) 

# example 3

def apply_discount(price, discount_percentage):
    return price * (1 - discount_percentage / 100)

print('Exercise 3:', apply_discount(100, 25)) 

# example 4

def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        return None

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# example 5

def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6)) 

# example 6

def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3)) 

# example 7

def calculate_tip(bill_amount, tip_percentage):
    return (bill_amount * tip_percentage) / 100

print('Exercise 7:', calculate_tip(50, 20))

# example 8

def product(*nums):
    result = 1
    for number in nums:
        result *= number
    return result

print('Exercise 8:', product(2, 5, 5))  


# example 9

def basicCalculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract")) 

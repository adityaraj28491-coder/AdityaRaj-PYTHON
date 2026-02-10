# First Program
print("Hello World!")

#RESUME
print("Hello! I will introduce myself.")
print('Name: Aditya raj')
print('Age: 20')
print('Address: Delhi, India' )
print('Place of Birth: Jharkhand, India')

#Circumference
radius = 4.0
print("Radius = ",radius)
print("Area = ", 3.14 * radius * radius)
print("Circumference = ", 2.0 * 3.14 * radius)

#Calculate the area of circle.
radius = 5.0
print("Radius = ",radius)
print("Area of cicle = ",3.14 * radius * radius)

# Calculate Area of Triangle
base = 4.0
height = 5.0
print("Area of Trinagle = ", 0.5 * base * height)

# Calculate Area of rectangle
length = 14
breadth = 5
print("Area of Rectangle = ", length * breadth)

# Design simple interest calculator
p = 1000
t = 2
r =5
si = (p*r*t)/100
print("Simple Interest = ",si)

# Calculate average of three numbers
num1 = 2
num2 = 4
num3 = 6
avg = (num1 + num2 +num3)/3
print("Average of three numbers = ", avg )

# Calculate Celsius into Fahrenheit
celsius = 37
convert = celsius * (9/5) + 32
print("celsius to Fahrenheit = ", convert)

# Calculate your age in days
age = 19
leap_year = (age % 4 == 0) and (age % 100 != 0 or age % 400 == 0)
age_days = (age * 365) + leap_year
print("Age in days = ",age_days)

# Take user input and calculate the Area of circle
radius = int(input("Enter the Radius = "))
area = 3.14 * radius * radius
print("Area of cirle = ", area)

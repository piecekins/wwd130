#What is the temperature in Fahrenheit? 81
#The temperature in Celsius is 27.2 degrees.

fahrenheit = float(input('What is the temperature in Fahrenheit? '))
celsius = (fahrenheit - 32) * ( 5 / 9 )

print(f'The temperature in Celsius is {celsius:.1f} degrees.')


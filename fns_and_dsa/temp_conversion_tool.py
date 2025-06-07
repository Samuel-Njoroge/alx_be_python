FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celcius
def convert_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celcius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    
# Prompt user to enter temperature
def main():
    try:
        temperature = float(input('Enter the temperature to convert: '))

        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

        if choice == 'C':
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        elif choice == 'F':
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        else:
            print("Invalid choice")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value")
    
if __name__ == '__main__':
    main()
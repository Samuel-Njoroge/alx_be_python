FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9) 
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

# Convert Fahrenheit to Celcius
def convert_to_celsius(fahrenheit):
    celcius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius
    
# Convert Celcius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

# Prompt user to enter temperature
def main():
    while True:
        temperature = float(input('Enter the temperature to convert: '))
        choice = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
        if choice == 'C':
            print(f"{temperature}C is {convert_to_fahrenheit(temperature)}F")
            pass
        elif choice == 'F':
            print(f"{temperature}F is {convert_to_celsius(temperature)}C")
        else:
            print("Invalid choice")
        break
    
if __name__ == '__main__':
    main()
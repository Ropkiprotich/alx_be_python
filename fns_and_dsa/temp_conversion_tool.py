FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) 

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
def main():
    convetion_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if convetion_choice == "F":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")

    elif convetion_choice == "C":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid input. Please enter 'F' for Fahrenheit to Celsius or 'C' for Celsius to Fahrenheit.")

if __name__ == "__main__":
    main()
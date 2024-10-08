FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
def main():
    convetion_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if convetion_choice == "F":
        fahrenheit = float(input("Enter the temperature to convert: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")

    elif convetion_choice == "C":
        celsius = float(input("Enter the temperature to convert: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num /denom
        return f"Result:{result}"  
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
def main():
    numerator = input("Enter the numerator")
    denominator = input("Enter the denominator")
    result = safe_divide(numerator, denominator)
    print(f"The result of the division is:{result}")
if __name__ == "__main__":
    main()

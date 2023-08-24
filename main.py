def main():
    # Input temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    
    # Result
    print(f"{celsius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")

    # Return the values 
    return celsius, fahrenheit

if __name__ == '__main__':
    main()

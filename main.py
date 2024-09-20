def celsius_to_fahrenheit(celsius): 
    # Convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32
    

def main():
    # Get user input
    celsius = float(input("Enter temperature in Celsius: "))
   
    # Convert to Fahrenheit using the function  
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # Print the result
    print(f"{celsius} ºC is equal to {fahrenheit} ºF") 


    ########################################
    # Do not delete the return statement
    ########################################
    return celsius, fahrenheit

if __name__== "__main__":
    main()
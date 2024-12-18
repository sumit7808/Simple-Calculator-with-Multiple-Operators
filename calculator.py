# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JCZsBLH2j7Cl-ckeiRaFj--N8OYB4hH4
"""

def calculator():


    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, %, **, //): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '//':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 // num2
        else:
            print("Error: Invalid operator")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input")
if __name__ == "__main__":
    calculator()
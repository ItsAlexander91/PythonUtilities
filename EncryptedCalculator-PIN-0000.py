import time
import math

for i in range(0,26):
    print(i,("% Processed"))
    time.sleep(0.5)

for e in range(26,51):
    print(e,("% Processed"))
    time.sleep(0.2)

for t in range(51,101):
    print(t,("% Processed"))
    time.sleep(0.15)

print("Completed")
a = input("Enter Password... ")
if a == "0000":
    print ("Connecting...")
else:
    exit    
    

for r in range(0,101):
 print(("[====="),r,("% Connected=====)"))
time.sleep(0.5)

while True:
    sign = input("Choose a sign +, -, *, or /: ")
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    
    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "*":
        result = num1 * num2
    elif sign == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        print("Invalid sign. Please choose from +, -, *, or /.")
        continue

    print(f"The result is: {result}")
    print("Closing in 10 Sec")
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(1)
    break

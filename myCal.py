import math
print("welcome to my calculator")
numberDictionary = {}  #to store the numbers
i = 1
operationHistory = ""   #for history purpose

number = float(input(f"Enter {i} no number: "))
numberDictionary[f"num{i}"] = number

# asking here if scientific sciFunction is needed or not
print("Apply scientific sciFunction to this number? (sin/cos/tan/cosec/sec/cot/log or press Enter to skip)")
sciFunc = input("sciFunction: ")

if sciFunc == 'sin':
    number = math.sin(math.radians(number))
    operationHistory = f"sin({numberDictionary[f'num{i}']})" 

elif sciFunc == 'cos':
    number = math.cos(math.radians(number))
    operationHistory = f"cos({numberDictionary[f'num{i}']})"

elif sciFunc == 'tan':
    number = math.tan(math.radians(number))
    operationHistory = f"tan({numberDictionary[f'num{i}']})"

elif sciFunc == 'cosec':
    sin_value = math.sin(math.radians(number))
    if sin_value == 0:
        print("Error: cosec is undefined for this value!")
        exit()
    number = 1 / sin_value
    operationHistory = f"cosec({numberDictionary[f'num{i}']})"

elif sciFunc == 'sec':
    cos_value = math.cos(math.radians(number))
    if cos_value == 0:
        print("Error: sec is undefined for this value!")
        exit()
    number = 1 / cos_value
    operationHistory = f"sec({numberDictionary[f'num{i}']})"

elif sciFunc == 'cot':
    tan_value = math.tan(math.radians(number))
    if tan_value == 0:
        print("Error: cot is undefined for this value!")
        exit()
    number = 1 / tan_value
    operationHistory = f"cot({numberDictionary[f'num{i}']})"

elif sciFunc == 'log':
    if number <= 0:
        print("Error: Cannot take log of zero or negative number!")
        exit()
    number = math.log10(number)
    operationHistory = f"log({numberDictionary[f'num{i}']})"

else:
    operationHistory = str(number)


result = number


while True:
    print("Operators: +, -, *, /, ^ (power)")
    operator = input("Enter operator or press Enter to calculate: ")
    
    if ( operator == '' ):
        break
    
    if (operator in ['+', '-', '*', '/', '^']):
        i = i+1
        number = float(input(f"Enter {i} number: "))
        numberDictionary[f"num{i}"] = number
        
        pending_operator = operator
        
        print("Apply sciFunction to this number? (sin/cos/tan/cosec/sec/cot/log or press Enter to skip)")
        sciFunc = input("sciFunction: ")
        
        if sciFunc == 'sin':
            number = math.sin(math.radians(number))
            operationHistory = operationHistory + operator + f"sin({numberDictionary[f'num{i}']})"

        elif sciFunc == 'cos':
            number = math.cos(math.radians(number))
            operationHistory = operationHistory + operator + f"cos({numberDictionary[f'num{i}']})"

        elif sciFunc == 'tan':
            number = math.tan(math.radians(number))
            operationHistory = operationHistory + operator + f"tan({numberDictionary[f'num{i}']})"

        elif sciFunc == 'cosec':
            sin_value = math.sin(math.radians(number))
            if sin_value == 0:
                print("Error: cosec is undefined for this value!")
                i = i - 1
                continue
            number = 1 / sin_value
            operationHistory = operationHistory + operator + f"cosec({numberDictionary[f'num{i}']})"

        elif sciFunc == 'sec':
            cos_value = math.cos(math.radians(number))
            if cos_value == 0:
                print("Error: sec is undefined for this value!")
                i = i - 1
                continue
            number = 1 / cos_value
            operationHistory = operationHistory + operator + f"sec({numberDictionary[f'num{i}']})"

        elif sciFunc == 'cot':
            tan_value = math.tan(math.radians(number))
            if tan_value == 0:
                print("Error: cot is undefined for this value!")
                i = i - 1
                continue
            number = 1 / tan_value
            operationHistory = operationHistory + operator + f"cot({numberDictionary[f'num{i}']})"

        elif sciFunc == 'log':
            if number <= 0:
                print("Error: Cannot take log of zero or negative number!")
                i = i - 1
                continue
            number = math.log10(number)
            operationHistory = operationHistory + operator + f"log({numberDictionary[f'num{i}']})"
        else:
            operationHistory = operationHistory + operator + str(number)
        
        #applying all the pending operators
        if ( pending_operator == '+' ):
            result = result + number
        elif ( pending_operator == '-' ):
            result = result - number
        elif ( pending_operator == '*' ):
            result = result * number
        elif ( pending_operator == '/' ):
            if ( number != 0 ):
                result = result / number
            else:
                print("Cannot divide by zero!")
                i = i - 1
                continue
        elif ( pending_operator == '^' ):
            result = result ** number
    else:
        print("Invalid operator!")

print(f"\n{operationHistory} = {result}")

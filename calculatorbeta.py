

def calculator():
    a= input('ENTER A NUMBER : ')
    b= input('ENTER A NUMBER : ')
    CHOICE= input('ENTER AN OPERATION (+ - * /) : ')
    a = int(a)
    b = int(b)
    HISTORY=[]
    if CHOICE == '+':
        result= a + b

    
    elif CHOICE == '-':
        result= a - b

    elif CHOICE == '*':
        result= a * b
    
    elif CHOICE == '/': 
        if b != 0:
            result= a / b
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please try again.")
    
    print(f'total: {result}')

    HISTORY.append(f"{a} {CHOICE} {b} : {result}")

    # Display history
    if HISTORY:
        print('----------------------')
        print("History:")
        for item in HISTORY:
            print(item)
            print('----------------------')



while True:
    calculator()
    cont = input('Do you want to continue? (yes/no): ')
    if cont.lower() != 'yes':
        break

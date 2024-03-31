def calculiator(num1, num2, your_action):
    if your_action == '/' and num2 == 0:
        
        return "Sorry, it is not allowed"
   
    if your_action == '+':
        result = num1 + num2

    if your_action == '-':
        result = num1 - num2

    if your_action == '*':
        result = num1 * num2

    if your_action == '/':
        result = num1 / num2

    else:
        return "Your action is invalid"

    return result


num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
your_action = input("Enter your action: ")

print(calculiator(num1, num2, your_action))
HISTORY_FILE= "history.txt"

def show_history():
    file= open(HISTORY_FILE, 'r')
    lines= file.readlines()
    if len(lines)==0:
        print("No history Found!")  # fixed: hostory → history
    else:
        for line in reversed(lines):
            print(line.strip())  # fixed: stript() → strip()
    file.close()

def clear_history():
    file= open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared")

def save_to_history(equation, result):
    file= open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculator(user_input):
    try:
        if '+' in user_input:
            num1, num2 = user_input.split('+')
            op = '+'
        elif '-' in user_input:
            num1, num2 = user_input.split('-')
            op = '-'
        elif '*' in user_input:
            num1, num2 = user_input.split('*')
            op = '*'
        elif '/' in user_input:
            num1, num2 = user_input.split('/')
            op = '/'
        else:
            print("Invalid operator. USE ONLY +,-,*,/")
            return

        num1 = float(num1)
        num2 = float(num2)

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("You cannot divide by 0")
                return
            result = num1 / num2

        if int(result) == result:
            result = int(result)

        print("Result:", result)
        save_to_history(user_input, result)

    except:
        print("Invalid input, Use format: 5+5 or 5 + 5")

def main():
    print("---SIMPLE CALCULATOR (type history, clear or exit)")
    while True:
        user_input= input("Enter calculation(+,-,*,/) or command (history, clear)")
        if user_input=='exit':
            print("Good Bye")
            break
        elif user_input== 'history':
            show_history()
        elif user_input=='clear':
            clear_history()
        else:
            calculator(user_input)

main()

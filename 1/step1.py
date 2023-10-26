def calculate(operator, number_1, number_2):
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == 'x':
        return number_1 * number_2
    if operator == '/':
        return number_1 / number_2
    else:
        return 'invalid operator'

def main():
    operator = input("Enter operator: ")
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second nummber: "))
    calculate_answer = calculate(operator, number_1, number_2)
    print(calculate_answer)

if __name__ == "__main__":
    main()
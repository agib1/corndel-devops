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
    file = open("/workspace/corndel-devops/1/test/input_step2.txt", "r")
    statements = file.read().splitlines()
    sum = 0
    for statement in statements:
        components= statement.split(' ')
        operator, number_1, number_2 = components[-3:]
        calculate_answer = calculate(operator, int(number_1), int(number_2))
        sum += calculate_answer
    
    print(sum)

if __name__ == "__main__":
    main()
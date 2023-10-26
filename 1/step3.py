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
    file = open("/workspace/corndel-devops/1/test/input_step3.txt", "r")
    statements = file.read().splitlines()
    seen_statements = []

    line_number = 0
    statement = statements[line_number]

    while statement not in seen_statements:
        components = statement.split(' ')

        if 'calc' in components:
            operator, number_1, number_2 = components[-3:]
            line_number = int(calculate(operator, int(number_1), int(number_2)))
        else:
            line_number = int(components[-1:][0])

        seen_statements.append(statement)
        statement = statements[line_number]

    print('line number: ' + str(line_number))
    print('statement: ' + statement)

if __name__ == "__main__":
    main()
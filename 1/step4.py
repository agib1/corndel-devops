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
    file = open("/workspace/corndel-devops/1/test/input_step4.txt", "r")
    statements = file.read().splitlines()
    seen_statements = []

    line_number = 0
    statement = statements[line_number]

    while statement not in seen_statements:
        components = statement.split(' ')
        
        if 'replace' in components:
            line_number_1 = int(components[-2:][0])
            line_number_2 = int(components[-2:][1])
            if line_number_1 < len(statements) and line_number_2 < len(statement):
                statements[line_number_1] = statement[line_number_2]
            line_number += 1
        if 'calc' in components:
            operator, number_1, number_2 = components[-3:]
            line_number = int(calculate(operator, int(number_1), int(number_2)))
        else:
            line_number = int(components[-1:][0])
            if 'remove' in components:
                statements.pop(line_number) 

        seen_statements.append(statement)
        statement = statements[line_number]

    print('line number: ' + str(line_number))
    print('statement: ' + statement)

if __name__ == "__main__":
    main()
from random import choice, randint

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    a = randint(1, 20)
    b = randint(1, 20)
    op = choice(['+', '-', '*'])
    match op:
        case '+':
            result = (f'{a} + {b}')
            c = a + b
            return result, str(c)
        case '-':
            result = (f'{a} - {b}')
            c = a - b
            return result, str(c)
        case '*':
            result = (f'{a} * {b}')
            c = a * b
            return result, str(c)

from random import choice, randint

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    a = randint(1, 20) #NOSONAR
    b = randint(1, 20) #NOSONAR
    op = choice(['+', '-', '*']) #NOSONAR
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

from random import randint


RULES = 'Find the greatest common divisor of given numbers.'
def get_question_and_answer():
    a = randint(1, 20)
    b = randint(1, 20)
    numbers = f'{a} {b}'
    while b > 0:
        a, b = b, a % b
    return numbers, str(a)

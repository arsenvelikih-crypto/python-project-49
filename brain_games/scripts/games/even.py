from random import randint



RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
def get_question_and_answer():
    n = randint(1, 100)
    answer = 'yes' if n % 2 == 0 else 'no'
    return str(n), answer


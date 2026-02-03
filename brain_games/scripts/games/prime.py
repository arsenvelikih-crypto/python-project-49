from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    num = randint(2, 100)
    item = [2, 3, 5]
    for i in item:
        if num != i and num % i == 0:
            return num, 'no'
    return num, 'yes'

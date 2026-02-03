from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def get_question_and_answer():
    num = randint(2, 100)
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer

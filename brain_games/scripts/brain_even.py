import prompt
from random import randint
from brain_games.scripts.cli import welcome_user


def is_even(n):
    return n % 2 == 0


def question(some):
    return (f'Question: {some}')


def answer_q():
    return prompt.string('Your answer: ')

def main():


    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 100)
        quest = question(num)
        print(quest)
        answer = answer_q()

        if answer == "yes" and is_even(num):
            print('Correct!')
        elif answer == "no" and not is_even(num):
            print('Correct')
        i += 1

        if i == 3:
            print(f'Congratulations! {name}')

        if answer == "yes" and not is_even(num):
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
            break
        elif answer == "no" and is_even(num):
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()


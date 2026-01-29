import prompt
from random import randint
from brain_games.scripts.cli import welcome_user


def main():
    welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 100)
        quest = (f'Question: {num}')
        print(quest)
        answer = prompt.string('Your answer: ')

        if answer == "yes" and num % 2 == 0:
            print('Correct!')
        if answer == "no" and num % 2 != 0:
            print('Correct')
        i += 1
        if i == 3:
            print('Congratulations!')

        if answer == "yes" and num % 2 != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again!")
            break
        if answer == "no" and num % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again!")
            break


if __name__ == "__main__":
    main()


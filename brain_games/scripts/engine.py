import prompt
from .cli import welcome_user


def run_game(game):

    name = welcome_user()
    print(game.RULES)
    correct_answers = 0
    while correct_answers < 3:
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer == user_answer:
            print('Correct')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f" Correct answer was '{answer}'. Let's try again, {name}!")
            break

        if correct_answers == 3 and answer == user_answer:
            print(f'Congratulations, {name}!')

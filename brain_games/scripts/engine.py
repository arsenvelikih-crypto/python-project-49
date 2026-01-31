from .cli import welcome_user
import prompt



def run_game(game):


    name = welcome_user()
    print(game.RULES)
    correct = 0
    while correct < 3:
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer == user_answer:
            print('Correct')
        correct += 1

        if correct == 3 and answer == user_answer:
            print(f'Congratulations! {name}')
        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'. Let's try again, {name}!")
            break

from random import randint


def find_current_element():
    start = randint(1, 20)
    step = randint(1, 10)
    index = 0
    num_list = []
    while index <= 10:
        num_list.append(start + index * step)
        index += 1
    return num_list


RULES = 'What number is missing in the progression?'
def get_question_and_answer():
    num_list = find_current_element()
    index = randint(0, 9)
    hided_num = str(num_list[index])
    num_list[index] = '..'
    return ' '.join(map(str, num_list)), hided_num

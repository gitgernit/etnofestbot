import random
import string


def input_field():
    return 'выберите ответ'


def greet():
    return 'привет котан ответь на вопросы получи приз'


def accepted():
    return 'bono'


def not_accepted():
    return 'malo'


def attempting_start_again():
    return 'ты уже стартанул оло'


def end():
    return (f'ура ты выграл вот твой кот: '
            f'{"".join([random.choice(string.ascii_letters) for i in range(5)])}')


def alreadly_won():
    return 'ты уже победил, смирись'


def question1_1():
    return 'вопрос 1_1 (ответ: ответ 1_1)'


def question1_1_answer_1():
    return 'ответ 1_1'


def question1_1_answer_2():
    return 'ответ ыыыеэыу'


def question1_2():
    return 'вопрос 1_2 (ответ: ответ 1_2)'


def question1_2_answer_1():
    return 'ответ 1_2'


def question1_2_answer_2():
    return 'ответ ыыыеэыу'


def question2_1():
    return 'вопрос 2_1 (ответ: ответ 2_1)'


def question2_1_answer_1():
    return 'ответ 2_1'


def question2_1_answer_2():
    return 'ответ ыыыеэыу'


def question2_2():
    return 'вопрос 2_2 (ответ: ответ 2_2)'


def question2_2_answer_1():
    return 'ответ 2_2'


def question2_2_answer_2():
    return 'ответ ыыыеэыу'


def question3():
    return 'вопрос 3 иди найди код и напиши мне ево (ответ: kotik)'


def question3_answer_1():
    return 'kotik'


def question3_answer_2():
    return 'ответ ыыеуыэ'

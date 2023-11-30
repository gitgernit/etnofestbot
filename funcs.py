import random
import string


def greet():
    return 'привет котан ответь на вопросы получи приз'


def accepted():
    return 'bono'


def not_accepted():
    return 'malo'


def attempting_start_again():
    return 'ты уже стартанул оло'


def question1_1():
    return 'вопрос 1_1'


def question1_2():
    return 'вопрос 1_2'


def question2_1():
    return 'вопрос 2_1'


def question2_2():
    return 'вопрос 2_2'


def question3():
    return 'вопрос 3 иди найди код и напиши мне ево'


def end():
    return (f'ура ты выграл вот твой кот: '
            f'{"".join([random.choice(string.ascii_letters) for i in range(5)])}')

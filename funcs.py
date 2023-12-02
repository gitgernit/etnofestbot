import random
import string


def input_field():
    return 'Выбери ответ'


def greet():
    return ('Salut, amicus! Labor gravis habeo. Quaese veritatem. Будешь отвечать правильно - '
            'помогу найти конфеты!')


def accepted():
    return 'Хм, хм... Согласен.'


def not_accepted():
    return 'Не соглашусь! Попробуй еще раз.'


def attempting_start_again():
    return 'Куда же ты меня еще раз запускаешь?'


def end():
    return (f'Кодовое слово проверено: теперь мне осталось лишь его расшифровать, и я скажу, куда тебе идти.'
            f'Ну-ка, ну-ка...')


def end2():
    return (f'"Все дороги ведут в кафе 47 кабинета"! Отлично. Иди туда и забери свой приз. Твой код: '
            f'{"".join([random.choice(string.ascii_letters) for i in range(5)])}')


def checking():
    return f'Проверяю твое кодовое слово'


def already_won():
    return 'Ты уже победил, смирись.'


def question1_1():
    return 'Кто шёл после homo habilis по теории эволюции?'


def question1_1_answer_1():
    return 'homo erectus'


def question1_1_answer_2():
    return 'Это уже последняя ступень'


def question1_1_answer_3():
    return 'Иисус'


def question1_2():
    return ('Какая личность после своей смерти повлияла на европейскую историю и литературу так, '
            'что даже Данте восхвалял его в «Божественной комедии»?')


def question1_2_answer_1():
    return 'Гитлер'


def question1_2_answer_2():
    return 'Тит Ливий'


def question1_2_answer_3():
    return 'Радищев'


def question2_1():
    return ('А вот тебе загадка: встретились инопланетяне и французы, поссорились, '
            'началась схватка. Кто победил?')


def question2_1_answer_1():
    return 'Французы!'


def question2_1_answer_2():
    return 'Инопланетяне!'


def question2_1_answer_3():
    return 'Яванцы!'


def question2_2():
    return 'Вот тебе еще вопрос: отчего в народе пошла сказка про избушку на курьих ножках?'


def question2_2_answer_1():
    return 'Гробы славян были похожи на нее'


def question2_2_answer_2():
    return 'Она существовала'


def question2_2_answer_3():
    return 'Так сказал Денис Звянко'


def question3():
    return ('Хорошо, хорошо отвечаешь. Я укажу тебе путь к конфетам, '
            'но мне понадобится твоя помощь: для этого мне нужно узнать кодовое слово '
            'и расшифровать его. Направляйся в 47 кабинет, ищи листки с отрывками слова, '
            'ищи хорошенько, а первую и пятую букву спроси у шамана: скажи ему '
            '"Дай мне загадку", ответь ему на нее и он тебе обязательно поможет, как узнаешь '
            'слово - напиши его мне.')


def question3_answer_1():
    return 'котик'

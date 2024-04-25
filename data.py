import json

DICT_DATA = 'data/quiz_data.json'

quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
        {
        'question': 'Какой тип данных используется для хранения чисел с плавающей точкой?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 1
    },
        {
        'question': 'Какая команда в Python используется для вывода данных?',
        'options': ['print', 'input', 'def', 'sum'],
        'correct_option': 0
    },
        {
        'question': 'Основатель языка програмиирования Python считается?',
        'options': ['Гвидо ван Россум', 'Илон Маск', 'Павел Дуров', 'Джордж Клуни'],
        'correct_option': 0
    },
        {
        'question': 'Является ли Python высокоуровневым языком?',
        'options': ['Да', 'Нет'],
        'correct_option': 0
    },
        {
        'question': 'Является ли Python компилируемым языком?',
        'options': ['Да', 'Нет'],
        'correct_option': 1
    },
    {
        'question': 'Какая библиотека в Python используется для машинного обучения?',
        'options': ['Django', 'Pygame', 'TensorFlow', 'Turtle'],
        'correct_option': 2
    },
    {
        'question': 'Какая библиотека в Python используется для Web - разработки ?',
        'options': ['Django', 'Pygame', 'TensorFlow', 'Turtle'],
        'correct_option': 0
    },
    {
        'question': 'Год основания языка Python',
        'options': ['1990', '1979', '2005', '1989'],
        'correct_option': 3
    }
    # Добавьте другие вопросы
]
with open(DICT_DATA, 'w') as file:
    json.dump(quiz_data, file)
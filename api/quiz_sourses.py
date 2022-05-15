import requests
from django.contrib import messages

class JServiceQuiz():
    """ Класс обрабатывает получение данных для викторины с сайта https://jservice.io"""

    def __init__(self):
        self.url = 'https://jservice.io/api/random'

    def get_quiz(self, count: int):
        """ Метод принимает количество требуемых вопросов викторины и возвращает список
         словарей с данными викторин"""

        quiz_data = []
        try:
            prefics = '?count=' + str(count)
            url = self.url + prefics
            data = requests.get(url).json()
            for data_item in data:
                quiz = {}
                quiz['question'] = data_item['question']
                quiz['answer'] = data_item['answer']
                quiz['created_at'] = data_item['created_at']
                quiz['category'] = data_item['category']['title']
                quiz_data.append(quiz)

        except requests.exceptions:
            print('Ошибка работы с сервисом по http')

        return quiz_data


from django.shortcuts import render
from .quiz_sourses import JServiceQuiz
from api.models import Quiz
from rest_framework.decorators import api_view
from .serializers import QuizSerializer
from rest_framework.response import Response

def index_view(request):

    return render(request, 'main_page.html')


@api_view(['POST'])
def quiz_view(request):
    """ Метод принимает в теле запроса параметр количества получаемых запросов.
    Получает с внешнего ресурса указанное количество вопросов викторины. Проверяет их на актуальность
    и 'добирает' вопросы, если указанный вопрос уже есть в базе и возвращает последний вопрос из базы"""

    # Получаем последний вопрос викторины из базы
    try:
        last_question = Quiz.get_last_record().question
    except:
        last_question = ''

    # Добавляем новые запросы
    count = request.data['question_num']
    quiz_parser = JServiceQuiz()
    quiz_data = quiz_parser.get_quiz(count)
    if len(quiz_data) > 0:
        for data_item in quiz_data:
            if not Quiz.check_for_record_existence(data_item['question']):
                data_set = QuizSerializer(data=data_item)
                if data_set.is_valid():
                    data_set.save()
            else:
                data_item = quiz_parser.get_quiz(1)
                while Quiz.check_for_record_existence(data_item['question']):
                    data_item = quiz_parser.get_quiz(1)
                data_set = QuizSerializer(data=data_item)
                if data_set.is_valid():
                    data_set.save()

    return Response(last_question)


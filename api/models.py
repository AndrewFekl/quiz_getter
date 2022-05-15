from django.db import models


class Quiz(models.Model):

    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    category = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


    @classmethod
    def get_last_record(self):
        """ Метод возвращает последнюю запись из базы """

        last_record = Quiz.objects.latest('id')
        return last_record


    @classmethod
    def check_for_record_existence(self, question):
        """ Метод проверяет наличие записи с указанным вопросом в базе"""

        check_question = Quiz.objects.filter(question=question).exists()
        return check_question


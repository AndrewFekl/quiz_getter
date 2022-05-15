# quiz_getter
Rest API сервис, получающий из интернета запрвшиваемое количество вопросов викторины и ответы к ним и возвращаюший последний сохраненный в базе данных вопрос.

Инструкция по разворачиванию проекта:
Для разворачивания проекта должен быть установлен и запущен Docker

# Создать директорию проекта
mkdir QuizGetter
cd QuizGetter

# Скачать файлы с репозитория
git clone https://github.com/AndrewFekl/quiz_getter.git .

# Построить и запистить контейнеры
docker-compose up -d --build

В файле конфигурации установлены значения для связи с БД
POSTGRES_NAME=quiz
POSTGRES_USER=postgres
POSTGRES_PASSWORD=coder74
они могут быть изменены на настройки пользователя
и
# Создаем базу данных quiz внутри контейнера
docker-compose exec db psql --username=postgres
CREATE DATABASE quiz;
quit;

# Выполняем миграции
docker-compose exec web python manage.py migrate --noinput

# Останавливаем контейнеры и запускаем снова
docker-compose down
docker-compose up -d

# Открываем стартовую страницу, чтобы убедиться, что проект работает
http://localhost:8000

Отправление POST запросов:
Отправляем POST запрос на адрес http://localhost/api
используя любой удобный сервис (postman, js, curl, requests python)
В теле запроса передать данные в виде json {"question_num": int}
или данных формы.

Сервис скачает неповторяющиеся вопросы и ответы викторины в количестве
question_num, сохранит из в базе и вернет предыдущий сохраненный вопрос
или пустую строку, если в базе еще нет записей.





import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


friend_name = 'друг'
my_name = 'Лиля'
text_mail = '''
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу.
→ Подготовишь крепкое резюме.

Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

text_mail = text_mail.replace('%website%', 'dvmn.org').replace('%friend_name%', friend_name).replace('%my_name%', my_name)

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')

login = os.getenv("login")
password = os.getenv("password")

server.login(login, password)



email_from = login
email_to = login

message = '''From: {}
To: {}
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

{}'''.format(login, login, text_mail)
message = message.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()
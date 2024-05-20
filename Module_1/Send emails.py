import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_name = input("Введите ваше имя: ")
friend_name = input("Введите имя друга,которому хотите отправить письмо: ")
website = "https://dvmn.org/referrals/95a50mjpBRDy09w91rgx9IjTZcr3Ldp3I46QGNEo/"

my_mail = input("Введите ваш имейл: ")
recipient_email = input("Введите имейл получателя: ")
letter_header = input("Введите заголовок письма: ")

letter = """\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о 
релизе сразу на имейл.""".format(my_mail, recipient_email, letter_header)

letter = letter.replace("%my_name%", my_name)
letter = letter.replace("%friend_name%", friend_name)
letter = letter.replace("%website%", website)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')

my_var_value = os.getenv('EM_LOGIN')
my_var_password = os.getenv('EM_PASSWORD')
server.login(my_var_value, my_var_password)

server.sendmail(my_mail, recipient_email, letter)
server.quit()

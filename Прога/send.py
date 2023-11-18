#!/usr/bin/env python3

import smtplib as smtp
from getpass import getpass
from email.mime.text import MIMEText
import csv
import sys


# Чтение учетных данных из файла
with open('/home/user/Документы/Keys/my_email.txt', 'r') as file:
    credentials = file.read().splitlines()

email = credentials[0]
password = credentials[1]

# Тема письма
subject = ''


# Открываем файл для записи с автоматическим сбросом буфера
with open('output.txt', 'w', buffering=1, encoding='utf-8') as file:
    # Перенаправляем стандартный поток вывода и ошибок
    sys.stdout = file
    sys.stderr = file

    # Ваш код Python с выводом
    # Откройте файл с таблицей и считайте данные
    with open('таблица.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')  # Используем ; в качестве разделителя

        for row in reader:
            dest_email, email_text = row
            
            message = MIMEText(email_text, 'plain', 'utf-8')
            message['From'] = email
            message['To'] = dest_email
            message['Subject'] = subject

            server = smtp.SMTP_SSL('smtp.yandex.com')
            server.set_debuglevel(1)
            server.login(email, password)
            server.send_message(message)


            print("----------------------------------")
            print(f"Sender: {message['From']}")
            print("----------------------------------")
            print(f"Recipient: {message['To']}")
            print("----------------------------------")
            print(f"Email Content: {email_text}")
            print("##################################")


sys.stderr = sys.__stderr__   
server.quit()

# Возвращаем стандартные потоки вывода и ошибок
sys.stdout = sys.__stdout__

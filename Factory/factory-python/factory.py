#-*- coding: utf-8 -*-
import smtplib

# exemple fonction d'envoyer d'Email
def send_ssl_mail(author, dest, msg, server, port, login, pwd):
    try:
        with smtplib.SMTP_SSL(f'{server}', port) as server:
            server.login(login, pwd)
            server.sendmail(author, dest, msg.as_string())
            print("Email envoyé avec succès.")
    except smtplip.SMTPAuthenticationError as e:
        print("Erreur d'authentification : Vérifiez votre nom d'utilisateur et mot de passe.")
        print(f"Code d'erreur : {e.smtp_code}, Message : {e.smtp_error}")
    except Exceptions as e:
        print(f"Une erreur est survenue : {e}")


from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

def make_message(author, dest, subject, body):
    msg = MIMEMultipart()
    msg['From'] = author
    msg['To'] = dest
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))

    return msg


auth = 'mouhamadou2.fall@gmail.com'
dest = 'client@yopmail.com'
subj = 'Test envoie'
body = 'BonSoir Tous Le Monde!'
msg = make_message(auth, dest, subj, body)

server = 'smtp.gmail.com'
send_ssl_mail(auth, dest, msg, server, 465, auth, 'hurqtcsqyasccwkx')


import pdb; pdb.set_trace()

import random
import collections

def random_number():
    return random.randint(0, 20)

d = collections.defaultdict(random_number)
d['a'] = 'Baba'
print(d['a'])







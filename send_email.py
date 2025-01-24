import smtplib as smtp
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "your_email"
    password = "your_password"

    receiver = "reciever_email"
    context = ssl.create_default_context()


    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
import smtplib as smtp
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ashwin.bckup@gmail.com"
    password = "tmcz pnwi cdwv rpsj"

    receiver = "nmashwin145@gmail.com"
    context = ssl.create_default_context()


    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
import smtplib, ssl
import os
from email.message import EmailMessage
import imghdr

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get("USER_EMAIL")
PASSWORD = os.environ.get("USER_PASSWORD")

# msg = EmailMessage()
# msg["Subject"] = "Teste do github actions"
# msg["From"] = USERNAME
# msg["To"] = USERNAME
# msg.set_content("report em forma de email teste do github actions")

# attachments
# files = ["image.png"]
# for file in files:
#     with open(file, "rb") as f:
#         file_data = f.read()
#         file_name = f.name()
#         file_type = imghdr.what(file_name) # se for arquivo não precisa

#     msg.add_attachment(
#         file_data, maintype="image", subtype=file_type, filename=file_name
#     )  # para imagens
#     msg.add_attachment(
#         file_data, maintype="application", subtype="octet-stream", filename=file_name
#     )  # para arquivos

message = """\
Subject: Teste do github actions

report em forma de email teste do github actions
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, USERNAME, message)  # from , to, mensagem
    # server.send_message(msg) # no lugar do sendmail

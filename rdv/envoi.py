import smtplib
from email.message import EmailMessage
# essai
# mervcodemerveille
def send_mail_for_doctor(user_name,email,date,rdv_name,heure):
    gmail_cfg =  {
        "server" : "smtp.gmail.com",
        "port" : "465",
        "email": "intimia805@gmail.com",
        "pwd":"cazhydtdafoknqxe"
    }

    msg = EmailMessage()
    msg["to"] = email
    msg["from"] = gmail_cfg["email"]
    msg["subject"] = "Rendez-vous medical"
    msg.set_content(f"{rdv_name} un rendez-vous avec {user_name} a ete enregistre pour le : {date} a {heure}")

    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
        smtp.send_message(msg)
        # print("Email envoyé !")


def send_mail_for_user(doctor_name,email,date):
    gmail_cfg =  {
        "server" : "smtp.gmail.com",
        "port" : "465",
        "email": "intimia805@gmail.com",
        "pwd":"cazhydtdafoknqxe"
    }

    msg = EmailMessage()
    msg["to"] = email
    msg["from"] = gmail_cfg["email"]
    msg["subject"] = "Rendez-vous medical"
    msg.set_content(f"Vous avez rendez le {date} avec : {doctor_name}")

    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
        smtp.send_message(msg)
        # print("Email envoyé !")
    

def send_password(email,password):
    gmail_cfg =  {
        "server" : "smtp.gmail.com",
        "port" : "465",
        "email": "intimia805@gmail.com",
        "pwd":"cazhydtdafoknqxe"
    }

    msg = EmailMessage()
    msg["to"] = email
    msg["from"] = gmail_cfg["email"]
    msg["subject"] = "Password"
    msg.set_content(f"Votre mot de passe est: {password}")

    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
        smtp.send_message(msg)
        # print("Email envoyé !")
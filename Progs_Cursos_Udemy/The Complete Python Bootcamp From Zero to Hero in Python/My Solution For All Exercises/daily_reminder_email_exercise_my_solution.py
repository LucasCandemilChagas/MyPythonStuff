import smtplib
import getpass
import schedule
import os
import time

log_in = ''

subject = ''
message = ''

def limpar_console():
    print(os.name)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def send_email():
    global log_in
    from_address = log_in
    to_address = log_in
    global subject, message
    msg = 'Subject: '+subject+'\n'+message
    smtp_object.sendmail(from_address, to_address, msg)
    
def login():
    email = getpass.getpass('Type your email: ')
    password = getpass.getpass('Type your password: ')
    smtp_object.login(email, password)
    return email

def escolher_provedor():
    while True:
        provedor = input('Type your provider (Gmail, Yahoo, Outlook/Hotmail, AT&T, Verizon or Comcast): ')
        if provedor.lower() == 'gmail':
            return smtplib.SMTP('smtp.gmail.com', 587)
        elif provedor.lower() == 'hotmail' or provedor.lower() == 'outlook':
            return smtplib.SMTP('smtp-mail.outlook.com', 587)
        elif provedor.lower() == 'yahoo':
            return smtplib.SMTP('smtp.mail.yahoo.com', 587)
        elif provedor.lower() == 'att' or provedor.lower() == 'at&t':
            return smtplib.SMTP('smtp.mail.att.net', 465)
        elif provedor.lower() == 'verizon':
            return smtplib.SMTP('smtp.verizon.net', 465)
        elif provedor.lower() == 'comcast':
            return smtplib.SMTP('smtp.comcast.net', 587)


smtp_object = escolher_provedor()
            
smtp_object.ehlo()

smtp_object.starttls()           

while True:
    try:
        log_in = login()
    except smtplib.SMTPAuthenticationError:
        limpar_console()
        print('Invalid email or password!')
    finally:
        break

subject = input('Enter the subject line: ')
message = input('Enter the body message: ')

schedule.every().day.at("08:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
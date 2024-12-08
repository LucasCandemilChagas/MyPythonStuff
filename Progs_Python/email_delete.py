import smtplib
import imaplib
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

    
def login():
    email = getpass.getpass('Type your email: ')
    password = getpass.getpass('Type your password: ')
    imap_object.login(email, password)
    return email

def escolher_provedor():
    while True:
        provedor = input('Type your provider (Gmail, Yahoo, Outlook/Hotmail, AT&T): ')
        if provedor.lower() == 'gmail':
            return imaplib.IMAP4_SSL('imap.gmail.com', 587)
        elif provedor.lower() == 'hotmail' or provedor.lower() == 'outlook':
            return imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)
        elif provedor.lower() == 'yahoo':
            return imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)
        elif provedor.lower() == 'att' or provedor.lower() == 'at&t':
            return imaplib.IMAP4_SSL('imap.mail.att.net', 993)


imap_object = escolher_provedor()     

while True:
    try:
        log_in = login()
    except smtplib.SMTPAuthenticationError:
        limpar_console()
        print('Invalid email or password!')
    finally:
        break


limpar_console()





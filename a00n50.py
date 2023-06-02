from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import yaml
from colorama import Fore, Style
import functions
import time


def A00N50(email, smtp_acc, a00n_setup, body, server: SMTP):
    smtpserver = smtp_acc['host']
    smtpport = smtp_acc['port']
    smtpuser = smtp_acc['username']
    smtppass = smtp_acc['password']
    sleeptime = a00n_setup['sleeptime']
    userremoveline = a00n_setup['userremoveline']
    fromname = a00n_setup['fromname']
    frommail = a00n_setup['frommail']
    subject = a00n_setup['subject']
    msgfile = a00n_setup['msgfile']
    attachfile = a00n_setup['attachfile']
    filepdf = a00n_setup['filepdf']
    message = MIMEMultipart()
    message["From"] = f'{fromname} <{frommail}>'
    message["To"] = email
    message["Subject"] = subject
    if attachfile:
        with open(filepdf, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filepdf}",
        )
        message.attach(part)
    message.attach(MIMEText(body, "html"))
    text = message.as_string()
    server.sendmail(smtpuser, email, text)
    functions.render_success(f'Send To : {email} | Send From : {smtpuser}')
    time.sleep(sleeptime)


def main():
    functions.banner()
    with open('./assets/maillist/hot.txt', 'r') as file:
        mail_list = functions.filter_emails(file.readlines())
    if (mail_list):
        with open("config/email-config.yaml", "r") as file:
            config = yaml.safe_load(file)
        with open('./assets/letter/index.html', 'r') as file:
            body = file.read()
        print("\033[91m                     =============================[\033[0m \033[1;4mA00N50 SENDER READY\033[0m \033[91m]==============================\033[0m")
        print("\r\n")
        print("\n")
        a00n_setup = config['a00n_setup']
        for account in config['smtp_acc']:
            try:
                server = SMTP(account['host'], account['port'])
                server.starttls()
                server.login(account['username'], account['password'])
                functions.render_success(
                    f'Start Sending Emails for : {account["username"]} ...')
                for email in mail_list:
                    A00N50(email, account, a00n_setup, body, server)
                server.quit()
            except Exception as ex:
                functions.render_error(ex)
    else:
        functions.render_error('Please give a valid email list')


if __name__ == "__main__":
    main()
    print(
        f'\n{Fore.BLUE}{Style.BRIGHT}\033[4mDone!\nBy : A00N{Style.RESET_ALL}')

import os
import smtplib
from email.message import EmailMessage


def send_email_message(from_addr, my_type, subj, body, rec_addr, passw):
    msg = EmailMessage()
    msg['From'] = rec_addr
    msg['To'] = from_addr
    msg['Subject'] = subj
    
    if my_type == 'text':
        msg.set_content(body)
    else:
        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <p style="color:SlateGray;">{text}</p>
            </body>
        </html>
        """.format(text=body), subtype='html')

    with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as smtp:
        smtp.login(rec_addr, passw)
        smtp.send_message(msg)
        print('The message was sent!')


if __name__ == '__main__':
    from_addr = input('Input your email: ')
    passw = input('Input email password: ')
    rec_addr = input('Input receiver email: ')
    my_type = input('Input text or html: ')
    subj = input('Input subject: ')
    body = input('Input message text: ')
    send_email_message(from_addr, my_type, subj, body, rec_addr, passw)
    

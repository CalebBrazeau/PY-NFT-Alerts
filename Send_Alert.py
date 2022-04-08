import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import creds

def sendAlert(subject, content, receiver):
    #The mail addresses and password
    sender_address = creds.s_email
    sender_pass = creds.s_pass
    receiver_address = receiver
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Alert Sent')
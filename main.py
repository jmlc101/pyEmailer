# import smtplib for sending function
import smtplib
# import email modules needed
from email.message import EmailMessage
# import module to read text file and assign it to Template
# TODO - do I still need this?
from string import Template

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

# Open plain text file whose name is in textfile for reading?
# me == the sender's email address
# you == the recipient's email address
def form_email_msg(textfile, me, you):
    with open(textfile) as fp:
        # create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = me # == the sender's email address
    msg['To'] = you # == the recipient's email address
    return msg

def send_email(msg):
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

# NOTE - format for mycontacts.txt, first email is me, second email is you.
def main():
    names, emails = get_contacts('mycontacts.txt')
    msg = form_email_msg('message.txt', emails[0], emails[1])
    send_email(msg)
    return "Email Sent?"



"""
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
"""

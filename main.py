# import smtplib for sending function
import smtplib
# import email modules needed
from email.message import EmailMessage
# import module to read text file and assign it to Template
# TODO - do I still need this?
from string import Template

# TODO - Create function that pulls email/password/host-address/port from a text file locally.
myAddress = 'myAddress@example.com' # TODO - Replace with email address that will be doing the sending.
password = 'mypassword' # TODO - Replace with said email address' password.
hostAddress = 'example.example.com' # TODO - Replace with host address for email service provider.
''' 
Host address and a port number,
both depend on the SMPT settings of your particular email service provider. 
For instance, in the case of Outlook, line 12 above would instead be:
hostAddress = 'smtp-mail.outlook.com' 
'''
hostPort = 'xxx' # TODO - Replace with email service provider's port # according to their SMPT settings.

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

def send_email(msg, host_address, host_port, my_address, my_pass):
    s = smtplib.SMTP(host=host_address, port=host_port)
    s.starttls() # TODO - Read up on smtplib documentation about this. There is a closing command needed?
    s.login(my_address, my_pass)
    s.send_message(msg)
    s.quit()

# NOTE - format for mycontacts.txt, first email is me, second email is you.
def main():
    names, emails = get_contacts('mycontacts.txt')
    msg = form_email_msg('message.txt', emails[0], emails[1])
    send_email(msg)
    print('Email Sent??')
    return print("Email Sent?")

if __name__ == '__main__':
    main()

"""
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
"""

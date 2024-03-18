import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password, image_path):

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the MIME and also encode it with utf-8 to display german "Umlaute".
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # Reads the PDF file and attaches it to the mail
    with open(image_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()
        pdf_attachment = MIMEApplication(pdf_data, Name='The_SCL_Times-Volume_19.pdf')
        # Add header to make it downloadable; you might want to change the filename
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename='The_SCL_Times-Volume_19.pdf')
        msg.attach(pdf_attachment)



    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, msg.as_string())



if __name__ == "__main__":

    # Set your email credentials and SMTP server details
    smtp_server = 'smtp.strato.de'
    smtp_port = 587  # Change the port accordingly
    smtp_username = 'yourEmail'
    smtp_password = 'yourSecretPassword'

    # Email content, utf-8 encoding to also send german "Umlaute"
    with open('email_text.txt', 'r', encoding='utf-8') as file:
        message = file.read()
    
    # Sets the subject of the Mail
    subject = 'The SCL Times'


    # Read the list of email addresses from a file
    with open('email_addresses.txt', 'r', encoding='utf-8') as file:
        email_addresses = [line.split(",") for line in file]

    # Deletes all the line breaks at the end of the file
    while email_addresses and email_addresses[-1] == ['\n']:
        email_addresses.pop()

    # Strip the mail addresses and the names
    for i in range(len(email_addresses)):
        for j in range(len(email_addresses[0])):
            email_addresses[i][j] = email_addresses[i][j].strip()

    #####  This part eliminates duplicates. If a person registers twice with the same Mail the mail will only be sent once. 
    mail_addresses = set()
    result = []


    for person in email_addresses:
        mail = person[0]
        if mail not in mail_addresses:
            result.append(person)
            mail_addresses.add(mail)

    email_addresses = result
    #####
    
    #Default greeting if the name of the person is unknown
    default_greeting = "Dear Valued SCL Times Subscriber,"

    #path to the image file
    image_path = 'The_SCL_Times-Volume_19.pdf'  

    
    # Send emails to each address in the list
    for person in email_addresses:
        if person[1] == "-":
            #if there is no name for the person (this means that there is a hyphon) then the default greeting will be sent
            greeting = default_greeting
        else: 
            #if there is a name the name will be sent. The name will automatically be capitalized
            greeting = f"Dear {person[1].capitalize()},"

        # the greeting is combined with the rest of the mail text
        finalMessage = f"{greeting}\n\n{message}"

        # Sends the mail
        send_email(subject, finalMessage, person[0], smtp_server, smtp_port, smtp_username, smtp_password, image_path)

        # prints all the greetings for which the mail has been sent. If there is a mistake you will be able to see the final greeting and thereby you'll know for which mail the error occured
        print(greeting)

    print("Emails sent successfully.")

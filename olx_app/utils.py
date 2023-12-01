import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


def generate_random_password():
    # Define characters for the password (you can adjust this based on your requirements)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of length 6
    random_password = ''.join(random.choice(characters) for _ in range(6))
    return random_password





def human_alert_email():
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'human.alert.project@gmail.com'
    msg['To'] = 'smohammedshafeeqhameed@gmail.com'
    msg['Subject'] = 'Registration Confirmation*'
    # Get the current date and time
    now = datetime.datetime.now()

    message = f'Hello {user.name}, your password is: {generated_password}. Please use this password to log in.'
    msg.attach(MIMEText(message))
    image = MIMEImage(img_data, name=os.path.basename(image_name))
    msg.attach(image)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('human.alert.project@gmail.com', 'dkjunvczirnedgjq')

    # Send the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
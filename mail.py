import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email_with_two_messages_two_pngs(sender_email, sender_password, receiver_email, subject, message1, message2, png_file_path1, png_file_path2):
    """
    Sends an email with two separate messages, two PNG file attachments, and a body message.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        receiver_email (str): The recipient's email address.
        subject (str): The subject of the email.
        message1 (str): The first message to include in the email body.
        message2 (str): The second message to include in the email body.
        png_file_path1 (str): The path to the first PNG file to attach.
        png_file_path2 (str): The path to the second PNG file to attach.
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Create the combined message with two separate parts
    body = MIMEMultipart('alternative')

    # Attach the first message
    body.attach(MIMEText(message1, 'plain'))

    # Attach the second message
    body.attach(MIMEText(message2, 'plain'))

    # Attach the combined message to the main email
    msg.attach(body)
    

    # Attach the first PNG file
    with open(png_file_path1, 'rb') as f:
        image1 = MIMEImage(f.read(), name=os.path.basename(png))
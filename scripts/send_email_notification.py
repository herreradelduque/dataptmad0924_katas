import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get environment variables
student_username = os.getenv('STUDENT_USERNAME')
pr_link = os.getenv('PR_LINK')
lessons_url = os.getenv('LESSONS_URL')
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

# Get the student's email (GitHub API does not expose the user's email directly)
# Optionally, you could maintain a map of usernames to emails or use a custom field.
student_email = f"{student_username}@example.com"  # Replace with actual method of getting student's email

# Create the email message
subject = "Notificación: Pull Request Recibida"
body = f"""
Hola @{student_username},

Tu Pull Request ha sido recibida.

*Link de la PR:* {pr_link}
Por favor, sube el link de la PR a la plataforma de lessons: {lessons_url}

Gracias,
El equipo de revisión
"""

# Set up the email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = student_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    # Set up the server (using Gmail as example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(email_address, email_password)
    
    # Send the email
    server.sendmail(email_address, student_email, msg.as_string())
    server.quit()

    print(f"Email notification sent to {student_email}")

except Exception as e:
    print(f"Failed to send email: {e}")

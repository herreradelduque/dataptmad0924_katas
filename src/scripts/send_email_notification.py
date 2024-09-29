import os
import smtplib
import json
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

# Function to retrieve student's email based on their GitHub username
def get_student_info_from_username(username):
    # Load the student email map from an environment variable (as JSON)
    student_email_map_json = os.getenv('STUDENT_EMAIL_MAP')
    if not student_email_map_json:
        raise ValueError("Student email map not found in environment variables")
    
    # Parse the JSON string to a dictionary
    student_email_map = json.loads(student_email_map_json)
    return student_email_map.get(username)

# Function to send email using SMTP
def send_email(to_email, subject, message):
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')

    if not email_address or not email_password:
        raise ValueError("Email credentials not found in environment variables")

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, to_email, msg.as_string())
        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    
    finally:
        server.quit()

# Function to generate email content based on the event
def generate_email_content(event, student_name, pr_link, lessons_url):
    if event == "pr_created":
        subject = f"[🥋 Katas Team] {student_name}, tu Pull Request ha sido recibida"
        message = (
            f"Hola {student_name},\n\n"
            f"¡Hemos recibido tu pull request! 🛠️.\n\n🚨 RECUERDA 🚨: No olvides añadir el link de tu PR en el Student Portal para que todo quede en orden.\n\n"
            f"BONUS EXTRA: Si eres el más rápido en enviar la respuesta correcta... ¡mergearé tu rama con main y serás el campeón de esta ronda! 🏆⏱️ \n\n¿Quién se anima a ser el próximo en conseguirlo?\n\n"
            f"🔗 Aquí tienes el link a tu Pull Request: {pr_link}\n\n"
            #f"Student Portal: {lessons_url}\n\n"
            f"¡A por todas!\nYour Teaching Team"
        )
    elif event == "pr_merged":
        subject = f"[🥋 Katas Team]🏆 {student_name}, ¡¡tu Pull Request ha sido mergeada!!"
        message = (
            f"Hola {student_name},\n\n"
            f"Tu solución ha sido la más rápida de esta semana!! Asi que tu pull request ha sido mergeada en la main branch.\n\n"
            f"Link a tu Pull Request: {pr_link}\n\n"
            f"Gracias por tu contribución a 'katas_winners'!!\n\n"
            f"Best regards,\nYour Teaching Team"
        )
    else:
        raise ValueError(f"Unknown event type: {event}")

    return subject, message

# Main function
def main():
    # Parse the event type (either "pr_created" or "pr_merged")
    parser = argparse.ArgumentParser(description="Send PR notification email")
    parser.add_argument("--event", required=True, help="Event type (pr_created or pr_merged)")
    args = parser.parse_args()

    # Fetch data from environment variables
    student_username = os.getenv('STUDENT_USERNAME')
    pr_link = os.getenv('PR_LINK')
    lessons_url = os.getenv('LESSONS_URL')

    if not student_username or not pr_link or not lessons_url:
        raise ValueError("Missing required environment variables")

    # Get the student's email
    student_email = get_student_info_from_username(student_username)[0]
    # Get the student's name
    student_name = get_student_info_from_username(student_username)[1]

    if student_email:
        # Generate the email content based on the event
        subject, message = generate_email_content(args.event, student_name, pr_link, lessons_url)
        
        # Send the email
        send_email(student_email, subject, message)
    else:
        print(f"Email for student {student_username} not found. Cannot send notification.")

if __name__ == "__main__":
    main()
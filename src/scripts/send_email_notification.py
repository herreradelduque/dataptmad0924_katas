import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to retrieve student's email based on their GitHub username
def get_student_email_from_username(username):
    # Load the student email map from an environment variable
    student_email_map_json = os.getenv('STUDENT_EMAIL_MAP')
    if not student_email_map_json:
        raise ValueError("Student email map not found in environment variables")
    
    # Parse the JSON string to a dictionary
    student_email_map = json.loads(student_email_map_json)
    return student_email_map.get(username)

# Function to send email using SMTP
def send_email(to_email, subject, message):
    # Fetch email credentials from environment variables (set as secrets in GitHub Actions)
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')

    if not email_address or not email_password:
        raise ValueError("Email credentials not found in environment variables")

    # Setting up the email
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the Gmail server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
        server.starttls()  # Start TLS encryption
        server.login(email_address, email_password)
        
        # Send the email
        server.sendmail(email_address, to_email, msg.as_string())
        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    finally:
        server.quit()

# Fetch required data from environment variables
student_username = os.getenv('STUDENT_USERNAME')
pr_link = os.getenv('PR_LINK')
lessons_url = os.getenv('LESSONS_URL')

# Validate that necessary information is present
if not student_username or not pr_link or not lessons_url:
    raise ValueError("Missing required environment variables")

# Get student's email from their GitHub username
student_email = get_student_email_from_username(student_username)

# If student email is found, send the email
if student_email:
    subject = f"Your Pull Request has been received"
    message = (
        f"Hello {student_username},\n\n"
        f"Your pull request has been received. Please submit the pull request link on the lessons platform.\n"
        f"Pull Request Link: {pr_link}\n"
        f"Submit the link here: {lessons_url}\n\n"
        f"Best regards,\nYour Teaching Team"
    )
    
    # Send the email
    send_email(student_email, subject, message)
else:
    print(f"Email for student {student_username} not found. Cannot send notification.")

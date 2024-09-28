import os
import smtplib
from email.mime.text import MIMEText
import logging

# Habilitar el registro de depuración
logging.basicConfig(level=logging.DEBUG)

def send_email(to_email, pr_link):
    # Obtener credenciales del entorno
    email_address = os.getenv('EMAIL_ADDRESS')  # Correo electrónico desde GitHub Secrets
    email_password = os.getenv('EMAIL_PASSWORD')  # Contraseña desde GitHub Secrets

    subject = "Notificación de Nueva PR"
    body = f"Se ha recibido una nueva PR: {pr_link}. Por favor, recuérdale que la suba a la plataforma."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)  # Habilitar el nivel de depuración
            server.starttls()  # Inicia TLS para mayor seguridad
            server.login(email_address, email_password)  # Inicia sesión en el servidor
            server.sendmail(email_address, to_email, msg.as_string())  # Envía el correo
        print("¡Correo enviado con éxito!")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    student_email = os.getenv('STUDENT_EMAIL')  # Correo del estudiante desde GitHub Secrets
    pr_link = os.getenv('PR_LINK')  # Enlace a la PR desde el entorno del flujo de trabajo
    send_email(student_email, pr_link)

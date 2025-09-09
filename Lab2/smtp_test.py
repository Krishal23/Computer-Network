import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv  

# Load environment variables from .env file
load_dotenv()
# Function to log messages into a file
def log_message(message):
    with open("email_log.txt", "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

# Main function to send email
def send_test_email():
    smtp_server = "smtp.gmail.com"
    port = 587  # TLS port
    sender_email = os.getenv("SENDERS_MAIL") 
    password = os.getenv("APP_PASSWORD")
    recipient_email = input("Enter recipient email address: ")

    msg = EmailMessage()
    msg.set_content("SMTP Connection Successful!")
    msg["Subject"] = "Test Email"
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        # creates SMTP session
        server = smtplib.SMTP(smtp_server, port)
        log_message("Connected to SMTP server.")
        
        server.starttls()  # Secure the connection
        log_message("Started TLS .")
        
        # Authentication
        server.login(sender_email, password)
        log_message("Logged in ....yayy.")
        
        server.send_message(msg)
        log_message(f"Email sent to {recipient_email}.")
        
        print("Email sent successfully!")
        
    except Exception as e:
        log_message(f"Error: {e}")
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
        log_message("Disconnected from SMTP server.")

if __name__ == "__main__":
    send_test_email()

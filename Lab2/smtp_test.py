import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def log_activity(entry):
    with open("email_activity_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {entry}\n")

# Function to send email to multiple recipients
def send_email():
    smtp_host = "smtp.gmail.com"
    smtp_port = 587  # TLS port
    sender_addr = os.getenv("SENDER_MAIL")
    app_pass = os.getenv("APP_PASS")

    # Example recipient list (can also take input from user or a file)
    recipients = ["kavyaa1706@gmail.com", "kanhakesharwani23@gmail.com"]

    for recipient in recipients:
        email_msg = EmailMessage()
        email_msg.set_content("Hehe. Congratulations. We made an SMTP server work for multiple recipients!")
        email_msg["Subject"] = "Test Email"
        email_msg["From"] = sender_addr
        email_msg["To"] = recipient

        try:
            server_connection = smtplib.SMTP(smtp_host, smtp_port)
            log_activity(f"Connected to SMTP server for {recipient}.")
            
            server_connection.starttls()
            log_activity("Started TLS.")
            
            server_connection.login(sender_addr, app_pass)
            log_activity(f"Logged in as {sender_addr}.")
            
            server_connection.send_message(email_msg)
            log_activity(f"Email sent to {recipient}.")
            
            print(f"Email successfully sent to {recipient}!")
        
        except Exception as err:
            log_activity(f"Error sending to {recipient}: {err}")
            print(f"Failed to send email to {recipient}: {err}")
        
        finally:
            server_connection.quit()
            log_activity(f"Disconnected from SMTP server for {recipient}.")

if __name__ == "__main__":
    send_email()

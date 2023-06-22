import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate
def send_email(subject, message, recipients):
    # Set up the SMTP server
    smtp_server = "mail.nt.com.pk"
    smtp_port = 26
    smtp_username = "admin@nt.com.pk"
    smtp_password = "ahiesto_yam420*"

    # Create the email message
    email = MIMEMultipart()
    email["Subject"] = subject
    email["From"] = smtp_username
    email["To"] = ", ".join(recipients)

    # Attach the message to the email
    email.attach(MIMEText(message, "plain"))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email)

# List of recipients
recipients = ["imrandawntv@gmail.com", "admin@nt.com.pk"]

# Subject and message
subject = "Arr/Dep Rpt ABY G9-562/3 29 May 23 Station"



message = " decor * (len(message) + 4) The Aircraft Engineer and Aircraft Technician successfully " \
          "handled the responsibilities of Flight 2111, which included managing an" \
          " A320 aircraft with ATA and ATD. They dealt with any defects, delays or rectifications that arose " \
          "while on standby mode and Flight status is.\n\n  Thanks and Regards \n\n   NT Station Team"

# Send the email
send_email(subject, message, recipients)

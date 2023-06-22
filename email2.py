import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Email details
sender_email = "admin@nt.com.pk"
receiver_email = ["imrandawntv@gmail.com", "admin@nt.com.pk"]
subject = 'Arrival/Departure Report ABY G9-558/559'

message = '''
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
  <body>
    <p style="font-size:18px; color:blue;">Hello!</p>
    <table>
  <tr>
    <th style="font-size:18px; color:blue;">Company</th>
    <th style="font-size:18px; color:blue;">Contact</th>
    <th style="font-size:18px; color:blue;">Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  
  </table>
    <p style="font-size:16px;" color:blue;">This is a fancy email message.</p>
    
  </body>
</html>
'''

# Connect to the SMTP server
smtp_server = "mail.nt.com.pk"
smtp_port = 26
username = "admin@nt.com.pk"
password = "ahiesto_yam420*"
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)

    # Create a multi-part message container
    message_container = MIMEMultipart('related')
    message_container['Subject'] = subject
    message_container['From'] = sender_email
    message_container['To'] = ', '.join(receiver_email)

    # Add HTML content to the message
    html_content = MIMEText(message, 'html')
    message_container.attach(html_content)


    # Send the email
    server.sendmail(sender_email, receiver_email, message_container.as_string())
    print('Email sent successfully!')

except Exception as e:
    print(f'Error: {str(e)}')

finally:
    # Disconnect from the server
    server.quit()

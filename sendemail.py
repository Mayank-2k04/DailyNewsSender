import smtplib, ssl

# SMTP Server Details
host = "smtp.gmail.com"
port = 465

user = "mayank.kapoor2607@gmail.com"
 #take user input
pa = "jwot zgaz ewxq vvhf"
# Create SSL Context
context = ssl.create_default_context()

# Send Email
def sendmail(message,receiver,username = user,password=pa):
    message = f"From: Mayank <{user}>\nTo: {receiver.split('@')[0]} <{receiver}>\nSubject: Today's news\n{message}"
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.encode('utf-8'))
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)



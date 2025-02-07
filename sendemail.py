import smtplib, ssl

# SMTP Server Details
host = "smtp.gmail.com"
port = 465

user = "mayank.kapoor2607@gmail.com"
rec = "samshokeen04@gmail.com" #take user input
pa = "jwot zgaz ewxq vvhf"
# Create SSL Context
context = ssl.create_default_context()

# Email Content (Include headers)
headers = """\
From: Mayank <mayank.kapoor2607@gmail.com>
To: """
# Send Email
def sendmail(message,receiver,username = user,password=pa):
    message = headers + receiver.split('@')[0] + " <" + receiver + ">\n" + message
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)



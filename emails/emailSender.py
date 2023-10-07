from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText


class EmailSender:
    """Class sends email with feeds"""

    def __init__(self, sender, receiver, smtp_host, smtp_port, smtp_user, smtp_password) -> None:
        self.sender = sender
        self.receiver = receiver
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def sendFeedsEmail(self, feeds) -> None:
        body = self.createEmailBody(feeds)

        mail = MIMEMultipart('alternative')
        mail['From'] = self.sender
        mail['To'] = self.receiver
        mail['Subject'] = "You latest feeds!"
        mail.attach(MIMEText("Switch to html", 'text'))
        mail.attach(MIMEText(body, 'html'))

        with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as smtp_server:
            smtp_server.login(self.smtp_user, self.smtp_password)
            smtp_server.sendmail(self.sender, self.receiver, mail.as_string())
            smtp_server.quit()

    def createEmailBody(self, feeds) -> str:
        body = """
        <!doctype html><html>
          <head></head>
          <body style="font-family: sans-serif;"><p><h1>Hello</h1><p>I think that you should read below articles ;-)</p>
         """
        for feed in feeds:
            body = body + f'<h2>{feed.name}</h2><ul>'
            for entry in feed.entries:
                body = body + \
                    f'<li><a href="{entry.url}">{entry.title}</a><br />{entry.summary}</li>'
            body = body + '</ul>'

        return body + "</p></body></html>"

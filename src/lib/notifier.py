import smtplib
from twilio.rest import Client
from lib.constants import *


class Notifier:

    def __init__(self, email, mobile, log, gmail_user, gmail_pass, twilio_number, twilio_asid, twilio_token):
        self.email = email
        self.mobile = mobile
        self.log = log
        self.gmail_user = gmail_user
        self.gmail_pass = gmail_pass
        self.twilio_number = twilio_number
        self.twilio_asid = twilio_asid
        self.twilio_token = twilio_token

    def notify(self, webpage):

        try:
            server = smtplib.SMTP_SSL(SMTP_SERVER, smtplib.SMTP_SSL_PORT)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_pass)
            text = EMAIL_TEXT % (self.gmail_user, self.email, webpage, webpage)
            server.sendmail(self.gmail_user, self.email, text)
            self.log.succ("Sent an email to the user")
        except Exception as e:
            self.log.fail("Could not send email: " + str(e))

        try:
            client = Client(self.twilio_asid, self.twilio_token)
            client.messages.create(body=(SMS_TEXT % webpage), from_=self.twilio_number, to=self.mobile)
            self.log.succ("Sent a text message to the user")
        except Exception as e:
            self.log.fail("Could not send text: " + str(e))

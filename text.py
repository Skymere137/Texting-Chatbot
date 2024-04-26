
import os
from flask import Flask
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

class Text:
    def __init__(self):
# establish variables and instance of client class
        self.sid = os.environ["tw_sid"]
        self.token = os.environ["twToken"]
        self.client = Client(self.sid, self.token)
   
# Create method for sending a message
    def send_text(self, msg, number):        
        message = self.client.messages \
            .create(
                body=msg,
                from_=os.environ["botNumberOne"],
                to=number
            )
        





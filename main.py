from flask import Flask, request
from text import Text
from twilio.twiml.messaging_response import MessagingResponse

phone = Text()

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():

    number = request.values.get("From", None)
    body = request.values.get("Body", None)

    resp = Text()
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
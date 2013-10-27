from random import choice
import flask
import config
from twilio.rest import TwilioRestClient
import twilio.twiml

app = flask.Flask(__name__)

client = TwilioRestClient(config.account_sid, config.auth_token)

mp3s = [ "http://audiour.com/iljqj2wh.mp3?download=1"
       , "http://audiour.com/c3wpozj4.mp3?download=1"
       , "http://audiour.com/fxwzbxes.mp3?download=1"
       , "http://audiour.com/3sx1orup.mp3?download=1"
       , "http://cylinders.library.ucsb.edu/mp3s/10000/10898/cusb-cyl10898d.mp3"
       , "http://cylinders.library.ucsb.edu/mp3s/4000/4749/cusb-cyl4749d.mp3"
       , "http://cylinders.library.ucsb.edu/mp3s/6000/6599/cusb-cyl6599d.mp3"
       , "http://cylinders.library.ucsb.edu/mp3s/3000/3524/cusb-cyl3524d.mp3"
]

# Make the call
@app.route("/make_call")
def make_call():
    call = client.calls.create(to=config.to,  # Any phone number
                            from_=config.from_, # Must be a valid Twilio number
                               url="http://localhost:5000/play")
                            #url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    print call.sid
    return "Call made!"

@app.route("/play", methods=['GET', 'POST'])
def play():
    resp = twilio.twiml.Response()
    resp.say("I've been waiting for you.")
    resp.play(choice(mp3s))

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


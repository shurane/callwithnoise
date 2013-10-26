import config
from twilio.rest import TwilioRestClient
import twilio.twiml

client = TwilioRestClient(config.account_sid, config.auth_token)

# Make the call
def make_call():
    #call = client.calls.create(to=config.to,  # Any phone number
                            #from_=config.from_, # Must be a valid Twilio number
                            #url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    #print call.sid
    resp = twilio.twiml.Response()
    resp.say("I've been waiting for you.")

if __name__ == "__main__":
    make_call()


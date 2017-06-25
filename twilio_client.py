from twilio.rest import Client
from twilio.twiml.voice_response import Dial, VoiceResponse, Say

sid = "AC2b050502f7bd74175c2d3d66865f585e"
auth = "2a32ff0c0045ba6d37b581c7bd500d89"

client = Client(sid, auth)

def send_sms(num,msg):
    client.messages.create(
    to="+1"+num,
    from_="+19172318588",
    body=msg)

def call_num(num,msg):

    client.calls.create(to="+1"+num,
                           from_="+19172318588",
                           url="http://40.71.189.185:5000/voice/?msg="+msg)

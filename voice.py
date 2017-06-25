from flask import Blueprint, render_template, request, session, redirect, Response, make_response
from twilio.twiml.voice_response import Dial, VoiceResponse, Say
from twilio_client import sid, auth

voice = Blueprint("voice", __name__, template_folder="templates", static_folder="static")

@voice.route("/voice/", methods=['GET', 'POST'])
def _voice():
    msg = request.args.get("msg")
    response = VoiceResponse()
    response.say(msg, voice='alice', language='en')

    print(response)
    return str(response)

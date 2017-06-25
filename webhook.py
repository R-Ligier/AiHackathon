
from flask import Blueprint, render_template, request, session, redirect

from twilio_client import send_sms, call_num
import json

webhook = Blueprint("webhook", __name__, template_folder="templates", static_folder="static")

@webhook.route("/webhook/", methods=['GET', 'POST'])
def _webhook():
    if request.method == "GET":
        msg = request.args.get("msg")
        num = request.args.get("num")
        send_sms(num,msg)
        return '1'
    if request.method == "POST":
        data = request.get_json()
        msg = data['msg']
        num = data['num']

        call_num(num,msg)

    

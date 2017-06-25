from flask import Flask, request, render_template, session, redirect
from index import index
from webhook import webhook
from voice import voice
from realtime_mta import realtime
from station import station

app = Flask(__name__, template_folder='templates')
app.secret_key = "bpV 2Q/sF&[D`2a1Z2-85q/{13X(RQZgWj3_q)P,=K2O9`B*RKjWiDp9P{F%WK7C"

app.register_blueprint(index)
app.register_blueprint(webhook)
app.register_blueprint(voice)
app.register_blueprint(realtime)
app.register_blueprint(station)

'''
@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
	return '1', 200
    else:
	return '0', 200
'''
app.debug = True
port = 5001
if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=port)

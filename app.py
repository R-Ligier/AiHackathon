from flask import Flask, request, render_template, session, redirect
from index import index
from webhook import webhook
from voice import voice

app = Flask(__name__)
app.secret_key = "bpV 2Q/sF&[D`2a1Z2-85q/{13X(RQZgWj3_q)P,=K2O9`B*RKjWiDp9P{F%WK7C"

app.register_blueprint(index)
app.register_blueprint(webhook)
app.register_blueprint(voice)

'''
@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
	return '1', 200
    else:
	return '0', 200
'''
app.debug = False
port = 5000
if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=port)

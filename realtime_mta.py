from flask import Blueprint, render_template, request, session, redirect, Response, make_response
import urllib2
import transitfeed
realtime = Blueprint("realtime", __name__, template_folder="templates", static_folder="static")

@realtime.route("/realtime/", methods=['GET', 'POST'])
def _realtime():

    numberline="http://datamine.mta.info/mta_esi.php?key=067b7c2881d68b0b6e7b0ca67a26c664&feed_id=1"

    response = urllib2.urlopen(numberline)
    html = response.read()

    return html

from flask import Blueprint, render_template, request, session, redirect, Response, make_response, jsonify
import urllib2
import json
station = Blueprint("station", __name__, template_folder="templates", static_folder="static")

@station.route("/station/<line>", methods=['GET', 'POST'])
def _station(line):

    station_api="http://40.71.189.185:5000/by-route/" + line
    response = urllib2.urlopen(station_api)

    stations=[]
    data=[]

    html = response.read()
    dump = json.loads(html)
    for station in dump['data']:
        data.append(station['name'])
        data.append(station['stops'])
        stations.append(data)
        data = []

    resp = make_response(json.dumps(stations))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

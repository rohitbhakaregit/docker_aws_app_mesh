from flask import Flask
import os
import requests
import urllib.request



app = Flask(__name__)

@app.route('/ping')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'pong'

@app.route('/ready')
def healthcheck():
    """Print 'Hello, world!' as the response body."""
    return 'yes'

@app.route('/isding')
def isding():
    dingHost= os.getenv("DING_HOST","pingpong-service")        # virtual node name 
    dingPort = os.getenv("DING_PORT", "8090")                     # virtual port for dingdong 
    dingURL = "http://%s:%s/ding"%(dingHost,dingPort)
    ding_server_response = requests.get(url=dingURL)
    with urllib.request.urlopen(dingURL) as url:
        s = url.read()


    if ding_server_response.status_code == 200:
        return " yes dong "+" from "+str(s)
    else:
        return "no dong"


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", port= 8080)


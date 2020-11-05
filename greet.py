from flask import Flask
import datetime

import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/healthz')
def health_check():
    d = {
    }
    with open('manifest.json') as f:
        data = json.load(f)

    d['status'] = data['status']
    d['version'] = data['version']
    d['uptime'] = datetime.datetime.now()
    return (json.dumps(d, default = myconverter))

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")

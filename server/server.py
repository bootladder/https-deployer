from __future__ import print_function
import sys
import simplejson as json
import flask
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug import secure_filename
import subprocess
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)
CORS(app)

@app.route('/plainjanegray', methods = ['POST','GET'])
def hello_worldzz():
    p = Popen(['sh','/opt/deployer/plainjanegray.sh'],
                      stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data,stderr_data  = p.communicate(input='\n')
    flaskprint('[UseCase Output] '+stdout_data)

    # Check Exit Code of the boundary
    if p.returncode != 0:
        flaskprint("[UseCase Return Code != 0]: /"
                      +": Failed, stderr: "+stderr_data)
        return flask.Response('The Use Case Failed, Brah', status=500)
    return 'blah2'

@app.route('/bootladder-blog', methods = ['POST','GET'])
def hello_worldz():
    p = Popen(['sh','/opt/deployer/bootladder-blog-deploy.sh'],
                      stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data,stderr_data  = p.communicate(input='\n')
    flaskprint('[UseCase Output] '+stdout_data)

    # Check Exit Code of the boundary
    if p.returncode != 0:
        flaskprint("[UseCase Return Code != 0]: /"
                      +": Failed, stderr: "+stderr_data)
        return flask.Response('The Use Case Failed, Brah', status=500)
    return 'blah2'

@app.route('/ccram', methods = ['POST','GET'])
def hello_world():
    p = Popen(['sh','/opt/deployer/ccram.sh'],
                      stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data,stderr_data  = p.communicate(input='\n')
    flaskprint('[UseCase Output] '+stdout_data)

    # Check Exit Code of the boundary
    if p.returncode != 0:
        flaskprint("[UseCase Return Code != 0]: /"
                      +": Failed, stderr: "+stderr_data)
        return flask.Response('The Use Case Failed, Brah', status=500)
    return 'blah2'

def flaskprint(stupid):
    print(stupid, file=sys.stderr)

if __name__ == '__main__':
    print("hello")
    context = ('cert.crt', 'key.key')
    app.run(debug = True,host='0.0.0.0', ssl_context=context, threaded=True, port=5000)




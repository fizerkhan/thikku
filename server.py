import os
from flask import Flask, render_template, request, redirect
import sms
import direction

app = Flask(__name__, static_folder='client', static_url_path='')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/direction', methods=['POST'])
def send_sms():
  try:
    text = request.form.get('message')
    if text is not None:
      origin,destination = text.split(":")
    else:
      origin = request.form.get('origin'),
      destination = request.form.get('destination')

    if origin == None or destination == None:
      return 'Message does not satify the schema', 404
    return direction.getDirection(origin, destination)

  except Exception as e:
    print e.message
    return e.message, 404

@app.route("/receive-sms", methods=['GET'])
def receive_sms():
  text = request.args.get('Text')
  _from = request.args.get('From')
  origin,destination = text.split(":")
  if origin == None or destination == None:
    return 'Message does not satify the schema', 404

  response = direction.getDirection(origin, destination)
  sms.send(_from, response)
  return 'Direction sent to ' + _from + '!'

if __name__ == '__main__':
  app.run()

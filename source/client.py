import os
import yaml
from flask import Flask, request, Response
from utils import process_keys, resolve_config_property
from slackclient import SlackClient


app = Flask(__name__)


keys_config_file =os.path.join(os.path.dirname(__file__), 'config.yml')
config_head = 'environment_keys'
with open(keys_config_file) as stream:
    config = yaml.load(stream)

SLACK_WEBHOOK_SECRET = resolve_config_property(config, config_head, 'SLACK_WEBHOOK_SECRET')
SHEET_ID = resolve_config_property(config, config_head, 'SHEET_ID')
SLACK_TOKEN = resolve_config_property(config, config_head, 'SLACK_TOKEN')

if SLACK_WEBHOOK_SECRET is None:
    raise Exception('No SLACK_WEBHOOK_SECRET set')
if SHEET_ID is None:
    raise Exception('No SHEET ID set')
if SLACK_TOKEN is None:
    raise Exception('No SLACK_TOKEN ID set')


slack_client = SlackClient(SLACK_TOKEN)


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        process_keys(request, SHEET_ID, slack_client)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    print ' * Running Slack Client'
    app.run(debug=True)

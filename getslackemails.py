#!/usr/bin/env python3

import json
import requests
import argparse

SLACK_API_URI='https://slack.com/api/'

parser = argparse.ArgumentParser()
parser.add_argument('-t', help="Slack API Token", dest="token", required=True)
parser.add_argument('-c', help="Slack channel name (no #)", dest="channel", required=True)

args = parser.parse_args()

# Get members
resp = requests.get(SLACK_API_URI + "channels.list?token=" + args.token)
respj = json.loads(resp.content.decode('utf8'))

for channel in respj['channels']:
    if channel['name'] == args.channel:
        # Found the correct channel
        members_of_channel = channel["members"]

# Get emails of members
resp = requests.get(SLACK_API_URI + "users.list?token=" + args.token)
respj = json.loads(resp.content.decode('utf8'))

for member in respj['members']:
    if member['id'] in members_of_channel:
        print(member['profile']['email'])
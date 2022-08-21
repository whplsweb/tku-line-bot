import requests
import json
from mylinebot.config import line

def getUserName(uid):
    url = f"https://api.line.me/v2/bot/profile/{uid}"

    payload={}
    headers = {
      'Authorization': f'Bearer {line["LINE_CHANNEL_ACCESS_TOKEN"]}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    return data['displayName']
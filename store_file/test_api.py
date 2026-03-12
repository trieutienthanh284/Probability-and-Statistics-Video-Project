import urllib.request
import json
import os

key = "AIzaSyDHwIaZfjnBMuifAFnChOhlYP-8ZnIHKpo"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print("Status code:", response.status)
        data = json.loads(response.read().decode('utf-8'))
        print("Success! Models accessible.")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")

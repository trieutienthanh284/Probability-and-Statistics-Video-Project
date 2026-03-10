import urllib.request
import json

API_KEY = "AIzaSyDHwIaZfjnBMuifAFnChOhlYP-8ZnIHKpo"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        for model in result.get('models', []):
            if 'generateContent' in model.get('supportedGenerationMethods', []):
                print(model['name'])
except Exception as e:
    print(f"Error: {e}")

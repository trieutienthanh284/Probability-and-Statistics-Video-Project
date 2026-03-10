import os
import json
import time
import sys

# Windows console fix for Vietnamese prints
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    import urllib.request
    
    API_KEY = "AIzaSyDHwIaZfjnBMuifAFnChOhlYP-8ZnIHKpo"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"

    print("1. Reading prompt template...")
    prompt_path = "scriptwriting/prompt.txt"
    if not os.path.exists(prompt_path):
        print(f"Error: {prompt_path} not found.")
        return
    with open(prompt_path, "r", encoding="utf-8") as f:
        base_prompt = f.read().strip()

    print("2. Reading topics...")
    topic_path = "scriptwriting/topic.txt"
    if not os.path.exists(topic_path):
        print(f"Error: {topic_path} not found.")
        return
    
    with open(topic_path, "r", encoding="utf-8") as f:
        topics = [line.strip() for line in f.readlines() if line.strip()]

    print(f"Found {len(topics)} topics.")
    
    script_bank = []
    
    print("3. Generating scripts using Gemini...")
    for idx, topic in enumerate(topics):
        print(f"Processing topic {idx+1}/{len(topics)}: {topic}")
        prompt = base_prompt.replace("{topic}", topic)
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseMimeType": "application/json"
            }
        }
        
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                script_text = result['candidates'][0]['content']['parts'][0]['text']
                script_data = json.loads(script_text)
                script_bank.append(script_data)
                print("  Successfully generated script.")
        except urllib.error.HTTPError as e:
            print(f"  Error generating script for topic '{topic}': {e.code}")
            print(e.read().decode('utf-8'))
            try:
                time.sleep(2)
                fallback_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={API_KEY}"
                req = urllib.request.Request(fallback_url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
                with urllib.request.urlopen(req) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    script_text = result['candidates'][0]['content']['parts'][0]['text']
                    script_data = json.loads(script_text)
                    script_bank.append(script_data)
                    print("  Successfully generated script on retry.")
            except urllib.error.HTTPError as e2:
                print(f"  Retry HTTP Error for topic '{topic}': {e2.code}")
                print(e2.read().decode('utf-8'))
            except Exception as e2:
                print(f"  Retry failed for topic '{topic}': {e2}")
        except Exception as e:
            print(f"  Error: {e}")

        time.sleep(1) # prevent rate limit
        
    print(f"\n4. Saving {len(script_bank)} scripts to script_bank.json...")
    with open("script_bank.json", "w", encoding="utf-8") as f:
        json.dump(script_bank, f, ensure_ascii=False, indent=2)
        
    print("Done! script_bank.json created successfully.")

if __name__ == "__main__":
    main()

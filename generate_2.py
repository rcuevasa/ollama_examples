import requests
import json

# Define the URL API
url = "http://localhost:11434/api/generate"

# Define the prompt

prompt = """
### System
You are an expert software engineer, and expert in ollama.

### User
Explain the duration fields that are part of the response json from /api/generate/ endpoint from ollama api and indicate 
what are the units used. The model is deepseek-r1:latest
"""

# Define the payload

payload = {
	"model": "deepseek-r1:latest",
	"prompt": prompt,
	"stream": False,
}

# Sending the request
response = requests.post(url, json=payload)

# Print the response
json_resp = response.json()
#print(json.dumps(json_resp,indent=2))
print(json.dumps(json_resp))
#print(30*"-")
#print(json_resp['response'])

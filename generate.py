import requests
import json

# Define the URL API
url = "http://localhost:11434/api/generate"

# Define the prompt

prompt = """
### System
You are an expert software engineer

### User
Explain the simplest hello world program in python
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
print(30*"-")
print(json_resp['response'])

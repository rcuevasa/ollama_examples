import requests
import json

# Define the URL API
url = "http://localhost:11434/api/chat"

# Define the payload

payload = {
	"model": "deepseek-r1:latest",
	"messages": [
 	   {
	 	"role": "system",
		"content": "You are an expert software engineer"
  	   },
	   {
		"role": "user",
		"content": "Explain a basic python hello world program"
	   }
	],
	"stream": False,
}

# Sending the request
response = requests.post(url, json=payload)

# Print the response
json_resp = response.json()
print(json.dumps(json_resp, indent=2))
print(30*"-")
print(json_resp['message']['content'])

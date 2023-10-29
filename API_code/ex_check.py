import requests
import json
payload = {
    "source_language": 1,
    "content": "मेरा नाम गर्वित है",
    "target_language": 6
}

response = requests.post('http://127.0.0.1:8000/scaler/translate', json=payload)
print(response.json())


// this script is for Twi, check out the GhanaNLP website for more language options

import json
import requests

file_name = "FILE NAME WITH PREFERRED AUDIO FORAMAT"

try:
    url = "https://translation-api.ghananlp.org/tts/v1/tts"

    hdr = {
        # Request headers
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': 'YOUR API KEY HERE',
    }

    # Request body
    text = input("Enter the text you want to convert to speech: ")
    data = json.dumps({"text": text, "language": "tw"})

    req = requests.post(url, headers=hdr, data=bytes(data.encode("utf-8")))

    req.get_method = lambda: 'POST'
    response = req

    if response.status_code == 200:        
        audio_data = response.content

        with open(file_name, "wb") as file:
          file.write(audio_data)
        
    else:
        print("Failed to create audio file")

except Exception as e:
    print(e)

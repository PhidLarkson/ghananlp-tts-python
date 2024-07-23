// this script is for Twi, check out the GhanaNLP website for more language options

import json
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

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
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
        play(audio)
        
    else:
        print("Failed to play audio data")

except Exception as e:
    print(e)

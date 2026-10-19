# py tts.py

import requests
import csv
import os

# ===== CONFIGURE =====
API_KEY = "sk_c2ff71b896113a4f74e0c1ccdfc74e7a7130a5caf9da9f83"

# Assign a voice ID to each character

# You (Will AI voice)
VOICE_Y = "bIHbv24MWmeRgasZH58o"

# Person D (Jessica AI voice)
VOICE_D = "cgSgspJ2msm6clMCkdW9"

# Narrator (Sarah AI voice)
VOICE_N = "FGY2WhTYpPnrIDTdsKH5"

CSV_FILE = "dialogue.csv"
OUTPUT_DIR = "voice_lines"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== FUNCTION TO GENERATE AUDIO =====
def generate_voice(text, filename, voice_id):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)

            print(f"Saved: {filename}")
        else:
            print(
                f"Failed to generate audio for '{text}': "
                f"{response.status_code} - {response.text}"
            )

    except requests.RequestException as error:
        print(f"Request error: {error}")


# ===== READ CSV AND GENERATE FILES =====
if not API_KEY:
    raise ValueError(
        "Missing API key. Set ELEVENLABS_API_KEY in PowerShell first."
    )

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)

    for row in reader:
        # Skip empty or incomplete rows
        if len(row) < 3:
            continue

        character = row[0].strip().lower()
        text = row[1].strip()
        line_id = row[2].strip()

        # Skip blank dialogue or missing IDs
        if not text or not line_id:
            continue

        # Select the voice based on the character
        if character == "d":
            voice_id = VOICE_D

        elif character == "y":
            voice_id = VOICE_Y

        elif character == "":
            voice_id = VOICE_N
            
        else:
            print(f"Unknown character '{character}'. Skipping.")
            continue

        # Set the output filename
        # ElevenLabs returns MP3 by default
        output_file = os.path.join(
            OUTPUT_DIR,
            f"{line_id}.mp3"
        )

        # Skip files that have already been generated
        if os.path.exists(output_file):
            print(f"Already exists, skipping: {output_file}")
            continue

        # Generate audio using the selected character voice
        generate_voice(text, output_file, voice_id)

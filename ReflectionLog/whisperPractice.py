import speech_recognition as sr
import whisper
import wave
import os

# Step 1: Record from mic
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK NOW")
    audio = r.listen(source)

# Step 2: Save to temp.wav
with open("temp.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Step 3: Transcribe using Whisper
model = whisper.load_model("base")
result = model.transcribe("temp.wav")
print(result["text"])

# Step 4: Delete the file
os.remove("temp.wav")

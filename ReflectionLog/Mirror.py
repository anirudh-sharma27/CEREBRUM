import json
from LLM import mirror
import asyncio
import edge_tts
from playsound import playsound

with open("trends.json", "r") as f:
    data = json.load(f)

reflections = [entry["reflection"] for entry in data]
sentiment = [entry["sentiment"] for entry in data]
fog_score = [entry["fog_score"] for entry in data]
compound_score = [entry["compound_score"] for entry in data]
date = [entry["date"] for entry in data]


prompt = "Here are recent reflections and scores:\n\n"
for i in range(-7, 0):  # last 7 entries
    prompt += f"{i+8}. \"{reflections[i]}\"\n"
    prompt += f"   Sentiment: {sentiment[i]}, Compound: {compound_score[i]}, Fog Score: {fog_score[i]}\n\n"

prompt += "Based on these entries, give a brief but emotionally intelligent summary of the user's current cognitive and emotional state. Focus on clarity, emotional tone, patterns, and recovery signs. Avoid exaggeration. Be calm and compassionate."
prompt+="\n\n also this is the history of some previous chats.please dont overuse it"
with open("ChatMemory.json","r") as f:
    data = json.load(f)
    last_prompt=data[-1][0]["content"]
prompt +="\n last_prompt"

print("cerebrum says-","\n")

x = mirror(prompt)
print(x)
async def main():
    tts = edge_tts.Communicate(x,"en-US-AndrewNeural")
    await tts.save("reflection.mp3")

asyncio.run(main())

playsound("reflection.mp3")

print("\n Anymore questions dear?(type 'no more questions' to terminate the session.)")
extra ="(Before answering the question remember the last prompt)" + last_prompt
while True:
    Sent=input("Type-")
    x=mirror(extra + Sent)
    if Sent=="no more questions":
        
        print("Thank you and i wish you well for the future")
        break
    else:
        
        print(x)
        
        async def main():
            tts = edge_tts.Communicate(x,"en-US-AndrewNeural")
            await tts.save("reflection.mp3")
        asyncio.run(main())
        playsound("reflection.mp3")
    


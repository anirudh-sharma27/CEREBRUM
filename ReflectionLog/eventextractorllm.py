# LLM.py

import openai
import json
from dotenv import load_dotenv
import os

'''client id = 553073383699-8bi3j47pq8b60sp71fm0pp5ln8458kl0.apps.googleusercontent.com

client secret = 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'''

load_dotenv()
api = os.getenv("Event_Key")


client = openai.OpenAI(
    api_key=api,
    base_url="https://api.groq.com/openai/v1"
)

'''"title": "...",
      "date": "YYYY-MM-DD",
      "start_time": "HH:MM",
      "end_time": "HH:MM",
      "location": null or "place"'''

def event_extractor(reflection):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are event extractor.You will read a paragraph of text and extract all the events with their dates,purpose,start time ,end time in different columns(if not mentioned just take 9 am to 9 pm or something like that).This has to be output in such a way that it can be easily read and the event can be added to the google calendar.Kust write in the tabular format.(events,starttime,deadline,date,location(if any else null)).DO NOT  WRITE ANYTHING ELSE.You can check the date today and tell me exact days.Just write date no today tomorrow ok.This is the format"},
            {"role": "user", "content": reflection}
        ],
        temperature=0.7
    )
    summary = response.choices[0].message.content
    return summary

reflection = "buy bread tomorrow and bury the living at 6pm at the gravestone crypt"
x = event_extractor(reflection)
print(x)

x = x.split("\n")
events = []
timestart = []
timeend= []
date = []
location = []

for i in range(2,len(x)):
    l = x[i].split("|")
    l.remove("")
    l.pop()
    events.append(l[0])
    timestart.append(l[1])
    timeend.append(l[2])
    date.append(l[3])
    location.append(l[4])
    entry = {
    "event":l[0],
    "starttime": l[1],
    "endtime":l[2],
    "date":l[3],
    "location":l[4]
    }


    file = "events.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    print("Entry saved")

    

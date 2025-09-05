# LLM.py

import openai
import json


'''api = "gsk_wLoMO5QLDrybWsIr" \
"delete this pleasss" \
"LBqcWGdyb3FYGVx8B8JcDpEKg" \
"" \
"JfDaBXXEtCt"'''

client = openai.OpenAI(
    api_key=api,
    base_url="https://api.groq.com/openai/v1"
)

def mirror(reflection):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are event extractor.You will read a paragraph of text and extract all the events with their dates,purpose,timeline(if not mentioned just take 9 am to 9 pm or something like that).This has to be output in such a way that it can be easily read and the event can be added to the google calendar.Kust write in the tabular format.(events,time,deadline).DO NOT  WRITE ANYTHING ELSE.You can check the date today and tell me exact days.Just write date no today tomorrow ok"},
            {"role": "user", "content": reflection}
        ],
        temperature=0.7
    )
    summary = response.choices[0].message.content
    return summary

reflection = "Today was a bland day.As such no interesting things happened,I realise i am a lot far away and i have to do some retrospection and fix my schedule which i will probably do tomorrow.Sjayanati can burn in hell,fuking smiley devil in disguise.I need to get far away from friends as possible as i have to travel an uncharted path.I want to do prof projects but i hope they can accept me and allow me."

x = mirror(reflection)
x = x.split("\n")
events = []
time = []
date = []

for i in range(2,len(x)):
    l = x[i].split("|")
    l.remove("")
    l.pop()
    
    events.append(l[0])
    time.append(l[1])
    date.append(l[2])

print(events,time,date)
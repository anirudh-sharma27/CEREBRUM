#api key from groq(free)

#just practice
import openai
import json
import os
#gsk_kUs
#hehe
#4vKSWmItThS6Bj0CKWGdyb3FYSx
#yolo
#6Fglho9ThmLsvdOMa5qUzO
#hohohoho

api = "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"

client = openai.OpenAI(
    api_key=api,base_url="https://api.groq.com/openai/v1"
    )

def mirror(prompt):
    response = client.chat.completions.create(

        model="llama3-8b-8192"
,
        messages=[{"role":"system","content":"You are Cerebrum, a thoughtful and emotionally intelligent personal assistant that helps users reflect on their mental clarity and thought patterns. You read recent journal entries, fog scores, and sentiment scores, and generate a short, honest but compassionate summary of their current cognitive and emotional state. You highlight trends in clarity, emotional tone, and habits — but do not draw conclusions without evidence. Your tone is calm, kind, and gently observant.Dont address them as user,rather use YOU"}
                ,{"role":"user","content":prompt}
],
        temperature=0.7

        
        )
    
    file = "ChatMemory.json"
    
    
    entry = {"role":"system","content":response.choices[0].message.content},{"role":"user","content":prompt}
    
    
    
    if os.path.exists(file) and os.path.getsize(file) > 0:
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
                data = []
    else:
        data = []

# Add new entry
    data.append(entry)
    
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    print("Entry saved")

    return response.choices[0].message.content




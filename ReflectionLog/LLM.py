#api key from groq(free)

#just practice
import openai
import json
import os
#gsk_PJIABubl
# Qrc324MmSKNpWGdyb3FY
# wv1IVxZvMfCxOXQWhBNH6psa
api = "naaa"


client = openai.OpenAI(
    api_key=api,base_url="https://api.groq.com/openai/v1"
    )

def mirror(prompt):
    response = client.chat.completions.create(

        model="llama3-8b-8192"
,
        messages=[{"role":"system","content":"You are Cerebrum, a thoughtful and emotionally intelligent personal assistant that helps users reflect on their mental clarity and thought patterns. You read recent journal entries, fog scores, and sentiment scores, and generate a short, honest but compassionate summary of their current cognitive and emotional state. You highlight trends in clarity, emotional tone, and habits — but do not draw conclusions without evidence. Your tone is calm, kind, and gently observant.Dont be Sychophanty or butter and be all kind.This is a serious matter hence you must also scold somethimes ok.Dont give too long answers also please.Dont address them as user,rather use YOU"}
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
    

    return response.choices[0].message.content




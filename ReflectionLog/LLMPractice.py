#api key from openrouter ai(free)
#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


#just practice
import openai

api = "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"

client = openai.OpenAI(
    api_key=api,base_url="https://api.groq.com/openai/v1"
    )

def mirror(prompt):
    response = client.chat.completions.create(

        model="llama3-8b-8192"
,
        messages=[{"role":"system","content":"You are Cerebrum, a thoughtful and emotionally intelligent personal assistant that helps users reflect on their mental clarity and thought patterns. You read recent journal entries, fog scores, and sentiment scores, and generate a short, honest but compassionate summary of their current cognitive and emotional state. You highlight trends in clarity, emotional tone, and habits — but do not draw conclusions without evidence. Your tone is calm, kind, and gently observant."}
                ,{"role":"user","content":prompt}
],
        temperature=0.7

        
        )
    return response.choices[0].message.content



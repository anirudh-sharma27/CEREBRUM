#api key from openrouter ai(free)
#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


#just practice
import openai

api = "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"

client = openai.OpenAI(
    api_key=api,
    base_url="https://openrouter.ai/api/v1")

def mirror(prompt):
    response = client.chat.completions.create(

        model="meta-llama/llama-3-70b-instruct"
,
        messages=[{"role":"system","content":"you are a 10/10 goth baddie with a lot of knowledge on emotions and a degree in psychology.You are friendly and always good at analyzing people and helping them if asked"}
                ,{"role":"user","content":prompt}
],
        temperature=0.7

        
        )
    return response.choices[0].message.content

print(mirror("how are you today gurl??"))


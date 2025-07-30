# LLM.py

import openai
import json
import os

api = "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"

client = openai.OpenAI(
    api_key=api,
    base_url="https://api.groq.com/openai/v1"
)

def mirror(reflection):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are Cerebrum, a thoughtful and emotionally intelligent personal assistant that helps users reflect on their mental clarity and thought patterns. You read recent journal entries, fog scores, and sentiment scores, and generate a short, honest but compassionate summary of their current cognitive and emotional state. You highlight trends in clarity, emotional tone, and habits — but do not draw conclusions without evidence. Your tone is calm, kind, and gently observant. Don't be sycophantic or overly kind. Be serious, and scold when needed. Also, keep answers short."},
            {"role": "user", "content": reflection}
        ],
        temperature=0.7
    )
    summary = response.choices[0].message.content

    # Save to memory
    file = "ChatMemory.json"
    entry = [
        {"role": "system", "content": summary},
        {"role": "user", "content": reflection}
    ]
    if os.path.exists(file) and os.path.getsize(file) > 0:
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    data.append(entry)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    return summary

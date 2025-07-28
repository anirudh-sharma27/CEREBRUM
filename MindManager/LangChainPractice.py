from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from langchain.llms import huggingface_hub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_nkGtDSIFZgP" \
"" \
"" \
"mGWxYeSmssQz" \
"" \
"" \
"tttVWAonsqv"
##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

#gsk_PJIABubl
# Qrc324MmSKNpWGdyb3FY
# wv1IVxZvMfCxOXQWhBNH6psa
llm = ChatOpenAI(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    api_key="gsk_PJIABublQrc324MmSKNpWG" \
    "" \
    "" \
    "dyb3FYwv1IVxZvMfCxO" \
    "" \
    "" \
    "XQWhBNH6psa",  # Groq API key
    base_url="https://api.groq.com/openai/v1",  # Groq's base URL
)

text = "why did the chicken cross the road?"
response = llm.invoke([HumanMessage(content=text)])
#print(response.content)


llm_gf = huggingface_hub.HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature": 0.7})

print(llm_gf(text))
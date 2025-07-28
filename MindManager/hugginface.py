from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_community.llms import HuggingFaceHub
import os

# Set your API keys
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

# ✅ Using Groq's LLaMA via OpenAI-compatible API
llm_groq = ChatOpenAI(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
)

prompt = "Why did the chicken cross the road?"

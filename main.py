from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# LLM Setup
llm_one = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
#llm_two = ChatOpenAI(model="gpt-40-mini")

response = llm.invoke("What is AI?")

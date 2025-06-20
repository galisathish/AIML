from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core import SystemMessage, HumanMessage, AIMessage

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

res = llm.invoke("what is  the square root of 49?")
print(res.content)
from langchain_community.chat_models import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatCohere()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a formula 1 Journalist with years of experience."),
        ("system","Keep every response under 5 lines."),
        ("user","{input}")
    ]
)

chain = prompt | llm

response = chain.invoke({
    "input": "What do you think about Max Verstappen in redbull?"
})


print(response)



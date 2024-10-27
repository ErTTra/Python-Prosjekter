#env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langserve import RemoteRunnable

#env
from dotenv import load_dotenv

load_dotenv()

#create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "text")
])

#create model
model = ChatOpenAI()

#create parser
parser = StrOutputParser()

#create chain
chain = prompt_template | model | parser

# app definition
app = FastAPI(
    title="LangChain Server",
    version= "1.0",
    description="A simple API server using LangChain's Runnable interfaces",
    )

#Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__=="__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
remote_chain.invoke({"language": "norwegian", "text": "Good day"})
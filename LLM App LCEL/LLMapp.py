from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4")

#messages = [
#    SystemMessage(content="translate the following from English to Norwegian"),
#    HumanMessage(content="hi"),
#]

#result = model.invoke(messages)
#parser.invoke(result)

#chain = model|parser
#chain.invoke(messages)

system_template="Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

#result = prompt_template.invoke({"language": "Norwegian", "text": "car"})

#result.to_messages()

chain = prompt_template| model | parser 
chain.invoke({"language": "Norwegian", "text": "car"})
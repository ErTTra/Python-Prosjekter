from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

# hent .env variabler
load_dotenv()

# Oprett ChatOpenAI model
model=ChatOpenAI(model="gpt-4o")


# Lage en liste for å lagre chat historie

chat_history = []

# Opprett systemmelding 
system_message = SystemMessage("Hei, spør meg om hva som helst!")
#legge så systemmeldingen til på lista
chat_history.append(system_message)

# Chat loop
while True:
    query = input("Ditt spørsmål:")
    if query.lower() == "exit":
        break
    #Legg brukerspørsmålet i lista
    chat_history.append(HumanMessage(content=query))

    # AI respons ved bruk av chat historie
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI svar: {response}")
    

# Load datas
from langchain.document_loaders import TextLoader

# Prompt
from langchain.prompts import PromptTemplate

# Vector database
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

# Llm
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.schema import SystemMessage

#agents
from langchain.agents.types import AgentType
from langchain.agents import initialize_agent
from langchain.tools import Tool

# Environment
from dotenv import load_dotenv, dotenv_values
import os
os.environ.clear()
load_dotenv()
    
def createStudentPrompt(name):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../templates/student.txt")
    loader = TextLoader(file_path=path)
    data = loader.load()[0].page_content
    
    return data.replace("<name>",name)

def initVectorDatabase():
    # initialize pinecone
    pinecone.init(
        api_key= os.getenv('PINECONE_API_KEY'),  # find at app.pinecone.io
        environment= os.getenv('PINECONE_ENVIRONMENT')   # next to api key in console
    )

def createVectorStore():
    
    initVectorDatabase()
    
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
    index = 'digital-twin'

    idx = pinecone.Index(index)
    text_field = "text"

    vectorstore = Pinecone(
        idx,
        embeddings,
        text_field
    )
    
    return vectorstore

def createQAagent(vectorstore, studentPrompt):
    # completion llm
    print(os.getenv('OPENAI_API_KEY'))
    llm = ChatOpenAI(
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        model_name='gpt-3.5-turbo',
        temperature=1
    )

    conversational_memory = ConversationBufferWindowMemory(
        memory_key="chat_history", return_messages=True
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
    )
    
    tools = [
        Tool(
            name="qa-student",
            func=qa.run,
            description="Answer questions related to the student",
        )
    ]
    
    student = initialize_agent(
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        tools= tools,
        llm=llm,
        memory=conversational_memory,
        system_message=studentPrompt,
        agent_kwargs={
            "system_message": studentPrompt
        },
        verbose=True,
    )
    
    return student


import chainlit as cl
import TWIN
import SBAGENT

from langchain.chat_models import ChatOpenAI

@cl.on_chat_start
async def on_chat_start():
    TWIN.setup()
    TWIN.initVectorDatabase()
    
    name = "Ruy Guzman"
    pinecone = TWIN.createVectorStore()
    prompt = TWIN.createStudentPrompt(name)

    student = TWIN.createQAagent(
        vectorstore=pinecone, 
        studentPrompt= prompt
    )
    
    cl.user_session.set("student", student)
    
    await cl.Message(
        content=f"Welcome to {name}'s Digital Twin. How can I assist you today?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    
    student = cl.user_session.get("student")    

    llm = ChatOpenAI(
        model_name='gpt-4',
    )
    
    sb_question = llm.invoke(f"Simplify this question for step back prompting: {message.content}")
    
    res = student.run(sb_question)

    await cl.Message(content=res).send()
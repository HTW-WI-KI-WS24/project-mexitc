import chainlit as cl
import TWIN
import SBAGENT

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
    
    initial_question = SBAGENT.chain.invoke({"question":message.content})
    print(initial_question)
    print(student.run(initial_question))

    res = student.run(message.content)

    await cl.Message(content=res).send()
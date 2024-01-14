"""
Notes for the profesor:

This module is an implementation for a step-back prompting chain.
Its original purpose was to simpliy prompts and beeing able to achieve a greater precision  within the responses.

The outcome wasn't as expected so we decided to go for a simpler approach within the app.py file.
"""

from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain import hub
from langchain.schema.output_parser import StrOutputParser
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

response_prompt = hub.pull("langchain-ai/stepback-answer")

# Few_shots examples and promtps
few_shot_examples = [
    {
        "input": "What programming languages are you proficient in?",
        "output": "List the programming languages you are proficient in."
    },
    {
        "input": "Tell me about a project where you worked collaboratively with a team.",
        "output": "Describe a project where you collaborated with a team, including your role and contributions."
    },
    {
        "input": "How do you stay updated with the latest technologies in the field?",
        "output": "Explain how you stay informed about the latest technologies and industry trends."
    },
    {
        "input": "Tell me about a challenging problem you encountered during a project and how you solved it.",
        "output": "Describe a challenging problem you faced during a project and the steps you took to solve it."
    },
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=few_shot_examples,
)

# Step-back prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Simplify the following questions to one that is easier to answer."),
    few_shot_prompt,  # Include the few-shot examples
    ("user", "Simplify the following question: {question}"),
])

question_gen = prompt | ChatOpenAI(temperature=0,model_name='gpt-4',openai_api_key=os.getenv('OPENAI_API_KEY')) | StrOutputParser()

def retriever(question):
    question_gen = prompt | ChatOpenAI(temperature=0,model_name='gpt-4',openai_api_key=os.getenv('OPENAI_API_KEY')) | StrOutputParser()
    question_gen.invoke({"question": question})
# Chain definition


chain = {
    # Retrieve context using the normal question
    "normal_context": RunnableLambda(lambda x: x['question']) | retriever,
    # Retrieve context using the step-back question
    "step_back_context": prompt | ChatOpenAI(temperature=0,model_name='gpt-4',openai_api_key=os.getenv('OPENAI_API_KEY')) | StrOutputParser(),
    "question": lambda x: x["question"]
} | response_prompt | ChatOpenAI(temperature=0) | StrOutputParser()
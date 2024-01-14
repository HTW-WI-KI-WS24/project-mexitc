# Vector database
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

import pinecone
import json
from dotenv import load_dotenv
import os
import uuid

os.environ.clear()
load_dotenv()

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))

# initialize pinecone
pinecone.init(
    api_key= os.getenv('PINECONE_API_KEY'),  # find at app.pinecone.io
    environment= os.getenv('PINECONE_ENVIRONMENT')   # next to api key in console
)
index_name = "digital-twin"
index = pinecone.Index(index_name=index_name)

vectorstore = Pinecone(
    index,
    embeddings,
    ""
)

file_path = "scripts/account_details_Ruy-GC.txt"
f = open(file_path)
data = json.load(f)

docs = []
texts = []
metadatas = []
ids = [str(uuid.uuid4()) for _ in data]
embeded = embeddings.embed_documents(data)

for i, (text, embedding) in enumerate(zip(data.items(), embeded)):

    texts.append(f'{text[0]}:{text[1]}')
    metadatas.append({"text":f'{text[0]}:{text[1]}'})
    

try:
    vectorstore.add_texts(ids=ids,metadatas=metadatas,texts=texts)
    print("Data successfully uploaded to db")
except:
    print("Fail")




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

file_path = "scripts/github/account_details_Ruy-GC.txt"
f = open(file_path)
data = json.load(f)
#data = json.dumps(data)

docs = []
texts = []
metadatas = []
ids = [str(uuid.uuid4()) for _ in data]
embeded = embeddings.embed_documents(data)
fields_list = []


fields_list.append(str({
    "gh_login": data['login'],
    "id": data['id'],
    "location": data['location'],
    "email": data['email'],
    "public_repos": data['public_repos'],
    "linkedin": data['blog'],
}))

print(". ".join(fields_list))

metadatas.append({"text":". ".join(fields_list)})
    
vectorstore.add_texts(ids=[str(uuid.uuid4())],metadatas=metadatas,texts=". ".join(fields_list),)
print("Data successfully uploaded to db")




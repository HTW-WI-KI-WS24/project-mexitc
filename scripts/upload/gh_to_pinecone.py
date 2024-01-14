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

f = open("scripts/github/account_details_Ruy-GC.txt","r")
data = json.load(f)

f = open("scripts\deepgit\codeReview\strong.txt", "r")
data2 = f.read()

f = open("scripts\deepgit\codeReview\weak.txt", "r")
data3 = f.read()


texts = []
metadatas = []
ids = []
fields_list = []

#######################################################################   
 
fields_list.append(str({
    "gh_login": data['login'],
    "id": data['id'],
    "location": data['location'],
    "email": data['email'],
    "public_repos": data['public_repos'],
    "linkedin": data['blog'],
}))

texts.append(". ".join(fields_list))
ids.append(str(uuid.uuid4()))
metadatas.append({"text":". ".join(fields_list)})

texts.append(data2)
ids.append(str(uuid.uuid4()))
metadatas.append({"text":data2})

texts.append(data3)
ids.append(str(uuid.uuid4()))
metadatas.append({"text":data3})

#######################################################################    
#Pinecone.from_texts([t for t in texts], embeddings, index_name=index)
vectorstore.add_texts(ids=ids,metadatas=metadatas,texts=texts)
print("Data successfully uploaded to db")

#######################################################################



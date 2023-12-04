import os
import sys

# Contains the API key for OpenAI
import constants as constants

# Import modules we need from the langchain package
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

# Set the API key as an environment variable
os.environ['OPENAI_API_KEY'] = constants.OPENAI_API_KEY

# Get the input from the command line
prompt = sys.argv[1]

# Load the data from all txt files in the data directory
loader = DirectoryLoader("data", glob="*.txt")
# Create a Vector DB from the data
index = VectorstoreIndexCreator().from_loaders([loader])

# Generate the response using the prompt and the ChatOpenAI model 
gpt3 = ChatOpenAI(model_name='gpt-3.5-turbo')
response = index.query(prompt, llm=gpt3);

# Print the response
print(response)
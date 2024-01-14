from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
        model_name='gpt-4',
        openai_api_key=os.getenv('OPENAI_API_KEY')
    )

f = open("scripts/deepgit/git_log_export.json", "r")
text = f.read()

weaknesses = llm.invoke(f"Analize the following github commits and give me coding weaknesses: {text}")
with open("scripts/deepgit/codeReview/weak.txt", 'w') as txt_file:
            txt_file.writelines(weaknesses.content)
            
strengths = llm.invoke(f"Analize the following github commits and give me coding strengths: {text}")
with open("scripts/deepgit/codeReview/strong.txt", 'w') as txt_file:
            txt_file.writelines(strengths.content)

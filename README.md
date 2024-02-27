[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cVeImKGm)

![image](https://github.com/HTW-WI-KI-WS24/project-mexitc/assets/78885738/5ece6703-0383-4a2a-89e8-9fbb861f06ed)
![image](https://github.com/HTW-WI-KI-WS24/project-mexitc/assets/78885738/2fb17e8d-13ab-450b-8e82-dae6f0d69048)



# Authors:
- Ruy Guzmán Camacho 
- Fernanda de León
- Karla Mondragón

# Digital-Twin
Welcome to your digital twin. This project is your digital persona, aimed to impress the recruiters and make it easier for them to know about your technical skills, projects and experience.

# Instructions
## Virtual Environment Setup
Create a virtual environment to avoid problems with package incompatibilities and not interfere with other projects you may have.

```bash
python3 -m venv digital-twin  
source digital-twin/bin/activate 
python3 -m pip install -r requirements.txt 
# When you want to leave virtual environment 
deactivate 
```

## Environment variables
Create a `.env` file with the structure presented in `example.env`

```.env
OPENAI_API_KEY = 
PINECONE_API_KEY =
PINECONE_ENVIRONMENT =
GIT_TOKEN =
```

## How to run
This projects relies on 3 main sections

1. App: contains the main part of the project, UI, modules for our agents and vector database retrievals and logic for the chat workflow.
  
3. Notebooks: jupyter notebooks used during the development to test new features in an ordered way. Contains the logic to upload a pdf to a pinecone vector database.
- `notebooks/StudentPrompt.txt` : Initial Prompt defining OpenAi behaviour during interaction.
- `notebooks/pinecone.ipynb`: Practice with pinecone environment.
   
3. Scripts: python scripts used to fetch & process data from APIs and further upload to pinecone

   3.1: Deepgit : Deep analysis to github stats
     - `scripts/deepgit/deepGitHub` : extracts github commits and code additions from a repository and a user
     - `scripts/deepgit/test.py`: filters extracted commits to OpenAi to identify code strengths and weaknesses
   
     3.1.1: codeReview: txt with strengths and weaknesses
         - `scripts/deepgit/codeReview/strong.txt` : Strengths obtained from OpenAi Github anaylsis
         - `scripts/deepgit/codeReview/weak.txt`: Weaknesses obtained from OpenAi Github analysis

   3.2: Github
     - `scripts/github/account_details_Ruy-GC.txt`: github main rofile data
     - `scripts/github/github_account.py`: script to extract gitub main profile data
   
   3.3: Upload
     - `scripts/upload/gh_to_pinecone.py` : save github main profile data into pincone


### Run chainlit app
```bash
cd app/src/
chainlit run app.py -w
#opens the app in the port 8000 by default
```

### Run python scripts
```bash
#cd into the folder where the script is 
python3 script_name.py 
```

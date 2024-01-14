[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cVeImKGm)

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
2. Notebooks: jupyter notebooks used during the development to test new features in an ordered way. Use freely if something is not clear. Also contains the logic to upload a pdf to a pinecone vector database
3. Scipts: python scripts used to fetch & process data from APIs and further upload to pinecone

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

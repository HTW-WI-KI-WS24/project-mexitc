[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cVeImKGm)


# Test instructions
1. pip3 install langchain openai chromadb pymupdf tiktoken
2. python3 app.py "What is my name?"

# Linkedn scraper
1. Create a new account on LinkedIn, or use one you already have
2. Login to that account using your browser
3. Open your browser's Dev Tools to find the cookie with the name li_at. Use that value for sessionCookieValue when setting up the scraper.
4. Install: npm install linkedin-profile-scraper

# Virtual Environment Setup

$ python3 -m virtualenv venv  
$ source venv/bin/activate
$ (my_venv)$ python3 -m pip install -r ./requirements.txt  
$ (my_venv)$ deactivate # When you want to leave virtual environment

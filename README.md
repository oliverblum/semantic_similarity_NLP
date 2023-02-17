# Semantic similarity (NLP Project)
### movies.py: 
This project uses an NLP model to calculate the similarity of words and sentences

### watch_next.py:
The similarity between words and sentences can be used to make a suggestion of what
a user might want to watch next (out of a list of movies) based what movies he watched in the past

## Installation
### spaCy
You need to have spaCy installed, as well as its English language model (en_core_web_md).

Type the following commands in command line (start: type "cmd" and a black window opens)
pip3 install spacy
python3 -m spacy download en_core_web_md  
----------------OR----------------------
pip install spacy
python -m spacy download en_core_web_md

Once installed, import spacy and load the English language model
import spacy
nlp = spacy.load('en_core_web_md')

### tabulate
Make sure you have the tabulate library installed by doing the following:
- Type CMD in the search bar and open the Command Prompt application.
- Type "pip install tabulate --user" and press Enter

If installation does not work, follow steps in https://www.youtube.com/watch?v=I6-_W-SuSG4


## Usage

![image](https://user-images.githubusercontent.com/123483224/219683644-7409dad7-76d6-484e-a0bc-3e7bc8dcc5d3.png)

"""
The task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
"""

# ************************** INSTALLATION **************************************
# You need to have spaCy installed, as well as its English language model (en_core_web_md).

# Type the following commands in command line (start: type "cmd" and a black window opens)
# pip3 install spacy
# python3 -m spacy download en_core_web_md  
# ----------------OR----------------------
# pip install spacy
# python -m spacy download en_core_web_md

# once installed, import spacy and load the English language model
import spacy
nlp = spacy.load('en_core_web_md')

# make sure you have the tabulate library installed by doing the following:
# - Type CMD in the search bar and open the Command Prompt application.
# - Type "pip install tabulate --user" and press Enter
# if installation does not work, follow steps in https://www.youtube.com/watch?v=I6-_W-SuSG4
from tabulate import tabulate

def next_movie(watched_des):
    """
    The function takes in the description as a parameter and returns the
    title of the most similar movie to watch next.
    """

    # === list of next movies ===
    # Each separate line is a description of a different movie
    in_file = open("movies.txt","r")
    contents = in_file.read()
    in_file.close()

    # create list of movies
    names        = []
    descriptions = []

    for line in contents.split("\n"):
        # splitting by : as a line looks like "Movie X : A description ..."
        if line.split(" :", 1)[0] != "": # ignores empty lines in text file
            names.append(line.split(" :", 1)[0].strip())
            descriptions.append(line.split(" :", 1)[1].strip())

    # === calculate similarities ===
    # nlp model of watched movie
    watched_nlp  = nlp(watched_des)

    similarities = []
    print_table  = []

    for i, next_des in enumerate(descriptions):
        #nlp model of next movie
        next_nlp = nlp(next_des)

        # calculate similarity
        sim = next_nlp.similarity(watched_nlp)
        similarities.append(sim)

        # oragnise results in a table for print out to console
        print_table.append([names[i], round(sim,4)])

    # print results to console
    print(f"Similarity to watched movie:")
    print(tabulate(print_table, headers=["Next movies", "Similarity"]))

    # get index of movie with highest similarity
    for i, sim in enumerate(similarities):
        if sim == max(similarities):
            max_sim      = sim
            max_sim_name = names[i]

    # print to console
    print(f"{max_sim_name} has max similarity of {round(max_sim,4)}")
    return max_sim_name

# test the function
watched_des  = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(next_movie(watched_des))
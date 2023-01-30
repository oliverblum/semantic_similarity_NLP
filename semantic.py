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


# === Similarity of Words ===
# Example 1
words = "cat apple monkey banana"
print(f"Similarity of \"{words}\":")
results = []
doc = nlp(words)
for token1 in doc:
    for token2 in doc:
        # calculate similarity
        similarity = token1.similarity(token2)

        # orth_ method returns a string representation of the token
        results.append([token1.orth_, token2.orth_, round(similarity,3)])

# print results
print(tabulate(results, headers=["Word 1", "Word 2", "Similarity"]))

"""
Output:

Similarity of "cat apple monkey banana":
Word 1    Word 2      Similarity
--------  --------  ------------
cat       cat              1
cat       apple            0.204
cat       monkey           0.593
cat       banana           0.224
apple     cat              0.204
apple     apple            1
apple     monkey           0.234
apple     banana           0.665
monkey    cat              0.593
monkey    apple            0.234
monkey    monkey           1
monkey    banana           0.404
banana    cat              0.224
banana    apple            0.665
banana    monkey           0.404
banana    banana           1

Note: the two animals have a higher similarity between each other compared to the two fruits
"""

# Example 2
# compare words
words = "money bank rob jail"
print(f"Similarity of \"{words}\":")
results = []
doc = nlp(words)
for token1 in doc:
    for token2 in doc:
        # calculate similarity
        similarity = token1.similarity(token2)

        # orth_ method returns a string representation of the token
        results.append([token1.orth_, token2.orth_, round(similarity,3)])

# print results
print(tabulate(results, headers=["Word 1", "Word 2", "Similarity"]))

"""
Output:
Similarity of "money bank rob jail":
Word 1    Word 2      Similarity
--------  --------  ------------
money     money            1
money     bank             0.463
money     rob              0.114
money     jail             0.261
bank      money            0.463
bank      bank             1
bank      rob              0.21
bank      jail             0.238
rob       money            0.114
rob       bank             0.21
rob       rob              1
rob       jail             0.183
jail      money            0.261
jail      bank             0.238
jail      rob              0.183
jail      jail             1

Note: 
rob and money have lowest similarity (not very good prediction)
rob and jail also do quite poorly (not very good prediction)
money and jail has higher similarity (but one first needs to rob it to get into jail)
"""

# Example 2 (with a different model)
# try using different model (also need to have this installed)
nlp = spacy.load('en_core_web_sm')
# compare words
words = "money bank rob jail"
print(f"Similarity of \"{words}\" using 'en_core_web_sm' model:")
results = []
doc = nlp(words)
for token1 in doc:
    for token2 in doc:
        # calculate similarity
        similarity = token1.similarity(token2)

        # orth_ method returns a string representation of the token
        results.append([token1.orth_, token2.orth_, round(similarity,3)])

# print results
print(tabulate(results, headers=["Word 1", "Word 2", "Similarity"]))


"""
Output:
[W007] The model you're using has no word vectors loaded, so the result of the Token.similarity 
method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship 
with word vectors and only use context-sensitive tensors. You can always add your own word vectors, 
or use one of the larger models instead if available. similarity = token1.similarity(token2)
Word 1    Word 2      Similarity
--------  --------  ------------
money     money            1
money     bank             0.594
money     rob              0.525
money     jail             0.267
bank      money            0.594
bank      bank             1
bank      rob              0.584
bank      jail             0.484
rob       money            0.525
rob       bank             0.584
rob       rob              1
rob       jail             0.416
jail      money            0.267
jail      bank             0.484
jail      rob              0.416
jail      jail             1

Note: Compared to the attempt in Example 2 above, we get higher similarities.
Hence seems like looking at the context improves similarities.
"""

# === Similarity of Sentences ===
sentence_to_compare = "Why is my cat on the car"
print(f"\nSimilarity to \"{sentence_to_compare}\":")
sentences = [
"where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
results = []
nlp = spacy.load('en_core_web_md')
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    results.append([sentence, round(similarity,3)])
print(tabulate(results, headers=["Comparison", "Similarity"]))

"""
Output:

Similarity to "Why is my cat on the car":
Comparison                    Similarity
--------------------------  ------------
where did my dog go                0.63
Hello, there is my car             0.803
I've lost my car in my car         0.679
I'd like my boat back              0.562
I will name my dog Diana           0.649
"""
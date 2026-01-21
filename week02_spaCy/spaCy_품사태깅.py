#%%
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("I was reading the paper.")

#추출
for token in doc:
    print(token.text, token.pos_)
#%%
#NER 개채명 인식
import spacy
nlp = spacy.load("en_core_web_sm")
text = """The day after I went on a trip to Seoul, I exchanged 70% of 300 yuan and 200 yen int dollars at 9 am."""
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
# %%
import spacy
nlp = spacy.load("en_core_web_sm")
text = "This is an example sentence with some stopwords that we want to remove."
doc = nlp(text)
filterd_tokens = [token.text for token in doc if not token.is_stop]

filterd_sentece = " ".join(filterd_tokens)
print(filterd_sentece)

# %%
import spacy
nlp = spacy.load("en_core_web_sm")
text ="Opportunity did not knock until I built a door."
doc = nlp(text)

for token in doc:
    print(f"{token.text} --> {token.dep_} --> {token.head.text}")

# %%

#NER using spacy
import spacy
from pprint import pprint
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')

#entity level
pprint([(X.text, X.label_) for X in doc.ents])

#token level
pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

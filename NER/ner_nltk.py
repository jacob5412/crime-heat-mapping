#NLTK
import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

#information extraction
ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

#tokenization and POS tagging
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
print(sent)

#chunking
def chunking(pattern, sentence):
    cp = nltk.RegexpParser(pattern)
    cs = cp.parse(sentence)
    return cs

pat = 'NP: {<DT>?<JJ>*<NN>}'  # noun phrase = optional determiner DT, any number of adjectives JJ, noun nominal NN
cs = chunking(pattern = pat, sentence = sent)
print(cs)

#inside-outside-beginning tagging
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

#tagger and classifier
ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)



# extracting noun phrases and verb phrases from text
from __future__ import unicode_literals
import spacy
import en_core_web_sm
import textacy

def verb_phrase(sentence):
    verb_clause_pattern = r'(<VERB>?<ADV>*<VERB>+)'
    doc = textacy.make_spacy_doc(sentence, lang='en_core_web_sm')
    verb_phrases = textacy.extract.pos_regex_matches(doc, verb_clause_pattern)

    # Print all Verb Phrase
    for chunk in verb_phrases:
        print(chunk.text)
    print("\n")
    # Extract Noun Phrase to explain what nouns are involved
    for chunk in doc.noun_chunks:
        print(chunk)

if __name__=="__main__":
    sentence = 'MAN BURNS WOMAN TAX OFFICER ALIVE IN HER OFFICE IN TELANGANA'
    verb_phrase(sentence)

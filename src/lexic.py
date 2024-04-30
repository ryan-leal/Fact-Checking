import spacy

nlp = spacy.load("pt_core_news_sm")

def tokenize(inputText):
    doc = nlp(inputText)
    for token in doc:
         print(f"{token.text}: {token.pos_}")
         
def lexic(inputText):
    print('[LEX] Returning token table')
    tokenize(inputText)

    
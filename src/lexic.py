import spacy
from tabulate import tabulate

nlp = spacy.load("pt_core_news_sm")

def tokenize(inputText):
    doc = nlp(inputText)

    tokens = []

    for token in doc:
        tokens.append((token.text, token.pos_))
    
    print('[LEX] Tokens classified, generating table...')

    printTable(tokens)
    return tokens

def printTable(tokens):
    headers=['TOKEN ', 'CLASSIFICATION']
    table = tabulate(tokens ,headers=headers, tablefmt='grid')
    print(table)
         
def lexic(inputText):
    tokens = tokenize(inputText)
    print('[LEX] Returning token table')
    return tokens

    
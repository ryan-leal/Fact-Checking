import requests
from bs4 import BeautifulSoup

def get_sinonimo(palavra):
    try:
        url = f"http://www.sinonimos.com.br/{palavra}/"
        print(f"Obtendo sinonimos da URL: {url}")
        resposta = requests.get(url)
        soup = BeautifulSoup(resposta.text, 'html.parser')
        a_tag = soup.find('a', class_='sinonimo')
        texto=a_tag.get_text()
        print(texto)
        return texto
    except Exception as e:
        print(f"Error fetching sinonimos for {palavra}: {e}")
        return [palavra]  # Returns the original word in case of an error
    
def reescreeve_verb(sinonimo,sintagmaVerbal):
    verbList=[]    #conversão de tupla pra lista pra fazer atribuição
    for token in sintagmaVerbal:
        if token[1] == "VERB":
            new_token=list(token)
            new_token[0] = sinonimo
            verbList.append(tuple(new_token))
        else:
            verbList.append(token)
    sintagmaVerbal[:] = verbList
def reescreeve_noun(sinonimo,sintagmaNominal):
    nominalList=[]    #conversão de tupla pra lista pra fazer atribuição
    for token in sintagmaNominal:
        if token[1] == "NOUN":
            new_token=list(token)
            new_token[0] = sinonimo
            nominalList.append(tuple(new_token))
        else:
            nominalList.append(token)
    sintagmaNominal[:] = nominalList

def semantic(sintagmaNominal, sintagmaVerbal,verbList,nounList):
    print('[SEM] Sintagma Nominal: ')
    print(sintagmaNominal)
    print('[SEM] Sintagma Verbal: ')
    print(sintagmaVerbal)
    print('[SEM] Returning Semantic Analysis')
    subst= get_sinonimo(nounList[0])
    reescreeve_noun(subst, sintagmaNominal)
    print(sintagmaNominal)
    palavra=get_sinonimo(verbList[0])
    reescreeve_verb(palavra,sintagmaVerbal)
    print(sintagmaVerbal)
    


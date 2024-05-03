import sys

# tokenList class, return next token
class tokenAnalyzer:
    def __init__(self, tokenList):
        self.tokens = tokenList
        self.posicao_atual = 0  # Inicializa a posição atual como 0

    def next(self):
        if self.posicao_atual < len(self.tokens):
            token = self.tokens[self.posicao_atual]
            self.posicao_atual += 1
            return token
        else:
            return None  # Retorna None se não houver mais tokens

def sintagmaPreposicional():
    global analyzer, token
    

    if token[1] == 'ADP':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaPreposicional')
        token = analyzer.next()
        sintagmaNominal() 
        sintagmaAdjetival() 
        sintagmaAdverbial()
        return
    else:
        print('[SYN] Dont found ADP, found ' + token[0] + ': ' + token[1] + ' in sintagmaPreposicional')

def sintagmaAdjetival():
    global analyzer, token
    

    if token[1] == 'ADJ':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaAdjetival')
        token = analyzer.next()
        sintagmaPreposicional()
        return
    else:
        print('[SYN] Dont found ADJ, found ' + token[0] + ': ' + token[1] + ' in sintagmaAdjetival')

def sintagmaAdverbial():
    global analyzer, token
    

    if token[1] == 'ADV':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaAdverbial')
        token = analyzer.next()
        sintagmaPreposicional()
        return
    else:
        print('[SYN] Dont found ADV, found ' + token[0] + ': ' + token[1] + ' in sintagmaAdverbial')

def complementoNominal():
    global analyzer, token

    sintagmaPreposicional()
    sintagmaAdjetival()
    sintagmaNominal()

def nucleoNominal():
    global analyzer, token

    nucleo = ['NOUN', 'PROPN', 'PRON']

    if token[1] in nucleo:
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in nucleoNominal')
        token = analyzer.next()
        return
    else:
        print('[SYN] ERROR: Expecting NON, PROPN or PRON, found ' + token[0] + ': ' + token[1])

def sintagmaNominal():
    global analyzer, token

    if token[1] == 'DET':
        print('[SYN] found DET ' + token[0] + ': ' + token[1] + ' in sintagmaNominal')
        token = analyzer.next()
        nucleoNominal()
        complementoNominal()
    elif token[1] in ['NOUN', 'PROPN', 'PRON']:
        print('[SYN] Dont found DET, but found ' + token[0] + ': ' + token[1] + ' in sintagmaNominal')
        token = analyzer.next()
        complementoNominal()
    else:
        print('[SYN] In sintagmaNominal, dont match anything')
    
        

def complementoVerbal():
    global analyzer, token

    sintagmaNominal()
    sintagmaAdjetival()
    sintagmaAdverbial()
    sintagmaPreposicional()
    sintagmaVerbal()
    
    

def sintagmaVerbal():
    global analyzer, token, sintVList, sintNList

    if token[1] == 'VERB' or token[1] == 'AUX':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaVerbal')
        token = analyzer.next()
        complementoVerbal()
    else:
        print('[SYN] Expecting VERB or AUX, found ' + token[0] + ': ' + token[1])
        

def sentenca():
    global analyzer, token, sintagmaVList, sintagmaNList

    sinV = []
    sinN = []

    print('===================== SINTAGMA NOMINAL ======================')
    posicaoInicial = analyzer.posicao_atual-1
    sintagmaNominal()
    posicaoFinal = analyzer.posicao_atual-1
    for tokens in analyzer.tokens[posicaoInicial: posicaoFinal]:
        sinN.append(tokens)
    print('===================== SINTAGMA VERBAL ======================')
    posicaoInicial = analyzer.posicao_atual-1
    sintagmaVerbal()
    posicaoFinal = analyzer.posicao_atual-1
    for tokens in analyzer.tokens[posicaoInicial: posicaoFinal]:
        sinV.append(tokens)
    
    sintagmaVList = sinV
    sintagmaNList = sinN

    
def texto():
    global analyzer, token
    token = analyzer.next()
    
    while(token != None):
        sentenca()
        if token[1] == 'PUNCT':
            print('[SYN] Sentence found correctly')
            token = analyzer.next()
            if token == None:
                print("[SYN] Text Found, returning...")
                return
            else:
                texto()
        else:
            print('[SYN] ERROR: Expecting PUNCT, found ' + token[0] + ': ' + token[1])
            sys.exit()

def syntatic(tokenList):
    # Instance of tokenAnalyzer to return next token using token list from lexer
    global analyzer, token, sintagmaVList, sintagmaNList
    analyzer = tokenAnalyzer(tokenList)
    sintagmaVList = []
    sintagmaNList = []
    
    texto()

    print('[SYN] Exiting Syntatic with Sintagma Nominal and Sintagma Verbal...')
    return sintagmaNList, sintagmaVList
    

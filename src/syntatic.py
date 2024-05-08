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

class Sintagma:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f'-{self.tipo}'


class SintagmaNominal(Sintagma):
    def __init__(self):
        super().__init__('Sintagma Nominal')
        self.determinante = None
        self.nucleo = None
        self.complemento = None

    def __str__(self):
        return f'{super().__str__()} ---> Determinante: {self.determinante} | Núcleo: {self.nucleo}'


class SintagmaVerbal(Sintagma):
    def __init__(self):
        super().__init__('Sintagma Verbal')
        self.verbo = None
        self.complemento = None

    def __str__(self):
        return f'{super().__str__()} ---> Verbo: {self.verbo}'


class SintagmaAdjetival(Sintagma):
    def __init__(self):
        super().__init__('Sintagma Adjetival')
        self.adjetivo = None
        self.complemento = None

    def __str__(self):
        return f'{super().__str__()} ---> Adjetivo: {self.adjetivo}'

class SintagmaAdverbial(Sintagma):
    def __init__(self):
        super().__init__('Sintagma Adverbial')
        self.adverbio = None
        self.complemento = None

    def __str__(self):
        return f'{super().__str__()} ---> Advérbio: {self.adverbio}'
    
class SintagmaPreposicional(Sintagma):
    def __init__(self):
        super().__init__('Sintagma Preposicional')
        self.preposicao = None
        self.complemento = None

    def __str__(self):
        return f'{super().__str__()} ---> Preposição: {self.preposicao}'

def imprimir_sintagma(sintagma, nivel=0):
    tabs = '\t' * nivel
    print(f'{tabs}{sintagma}')
    if sintagma.complemento != None:
        for items in sintagma.complemento:
            if isinstance(items, Sintagma):
                print(f'{tabs}Complemento:')
                imprimir_sintagma(items, nivel + 1)

def sintagmaPreposicional():
    global analyzer, token
    sinPrep = SintagmaPreposicional()

    if token[1] == 'ADP':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaPreposicional')
        sinPrep.preposicao = token[0]
        token = analyzer.next()
        temp = []
        temp.append(sintagmaNominal()) 
        temp.append(sintagmaAdjetival()) 
        temp.append(sintagmaAdverbial())
        sinPrep.complemento = temp
        return sinPrep
    else:
        print('[SYN] Dont found ADP, found ' + token[0] + ': ' + token[1] + ' in sintagmaPreposicional')

def sintagmaAdjetival():
    global analyzer, token
    sinAdj = SintagmaAdjetival()

    if token[1] == 'ADJ':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaAdjetival')
        sinAdj.adjetivo = token[0]
        token = analyzer.next()
        sinAdj.complemento = sintagmaPreposicional()
        return sinAdj
    else:
        print('[SYN] Dont found ADJ, found ' + token[0] + ': ' + token[1] + ' in sintagmaAdjetival')

def sintagmaAdverbial():
    global analyzer, token
    sinAdv = SintagmaAdverbial()

    if token[1] == 'ADV':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaAdverbial')
        sinAdv.adverbio = token[0]
        token = analyzer.next()
        sinAdv.complemento = sintagmaPreposicional()
        return sinAdv
    else:
        print('[SYN] Dont found ADV, found ' + token[0] + ': ' + token[1] + ' in sintagmaAdverbial')
        return

def complementoNominal():
    global analyzer, token
    temp = []
    temp.append(sintagmaPreposicional())
    temp.append(sintagmaAdjetival())
    temp.append(sintagmaNominal())
    return temp

def nucleoNominal():
    global analyzer, token

    nucleo = ['NOUN', 'PROPN', 'PRON']
    temp = None
    if token[1] in nucleo:
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in nucleoNominal')
        temp = token[0]
        if token[1] == 'NOUN':
            nounList.append(token[0])
            print(nounList[0])
        token = analyzer.next()
    else:
        print('[SYN] ERROR: Expecting NON, PROPN or PRON, found ' + token[0] + ': ' + token[1])

    return temp

def sintagmaNominal():
    global analyzer, token, nounList
    sintagmaNom = SintagmaNominal()
    if token[1] == 'DET':
        print('[SYN] found DET ' + token[0] + ': ' + token[1] + ' in sintagmaNominal')
        sintagmaNom.determinante = token[0]
        token = analyzer.next()
        sintagmaNom.nucleo = nucleoNominal()
        sintagmaNom.complemento = complementoNominal()
        return sintagmaNom
    elif token[1] in ['NOUN', 'PROPN', 'PRON']:
        print('[SYN] Dont found DET, but found ' + token[0] + ': ' + token[1] + ' in sintagmaNominal')
        sintagmaNom.nucleo = token[0]
        token = analyzer.next()
        sintagmaNom.complemento = complementoNominal()
        return sintagmaNom
    else:
        print('[SYN] In sintagmaNominal, dont match anything')
        return None
    
        

def complementoVerbal():
    global analyzer, token
    temp = []
    temp.append(sintagmaNominal())
    temp.append(sintagmaAdjetival())
    temp.append(sintagmaAdverbial())
    temp.append(sintagmaPreposicional())
    temp.append(sintagmaVerbal())
    return temp
    
    

def sintagmaVerbal():
    global analyzer, token, sintVList, sintNList, verbList
    sinVerb = SintagmaVerbal()
    if token[1] == 'VERB' or token[1] == 'AUX':
        print('[SYN] found ' + token[0] + ': ' + token[1] + ' in sintagmaVerbal')
        sinVerb.verbo = token[0]
        if(token[1]=='VERB'):
            verbList.append(token[0])
        token = analyzer.next()
        sinVerb.complemento = complementoVerbal()
        return sinVerb
    else:
        print('[SYN] Expecting VERB or AUX, found ' + token[0] + ': ' + token[1])
        return None
        

def sentenca():
    global analyzer, token, sintagmaVList, sintagmaNList, structure

    sinV = []
    sinN = []

    print('===================== SINTAGMA NOMINAL ======================')
    posicaoInicial = analyzer.posicao_atual-1
    structure.append(sintagmaNominal())
    posicaoFinal = analyzer.posicao_atual-1
    for tokens in analyzer.tokens[posicaoInicial: posicaoFinal]:
        sinN.append(tokens)
    print('===================== SINTAGMA VERBAL ======================')
    posicaoInicial = analyzer.posicao_atual-1
    structure.append(sintagmaVerbal())
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
        if token[0] == '.':
            print('[SYN] Sentence found correctly')
            token = analyzer.next()
            if token == None:
                print("[SYN] Text Found, returning...")
                return
            else:
                texto()
        else:
            print('[SYN] ERROR: Expecting \".\", found ' + token[0] + ': ' + token[1])
            sys.exit()

def syntatic(tokenList):
    # Instance of tokenAnalyzer to return next token using token list from lexer
    global analyzer, token, sintagmaVList, sintagmaNList, verbList, nounList, structure
    analyzer = tokenAnalyzer(tokenList)
    sintagmaVList = []
    sintagmaNList = []
    verbList= []
    nounList = []
    structure = []
    texto()
    for items in structure:
        imprimir_sintagma(items)
    print('[SYN] Exiting Syntatic with Sintagma Nominal and Sintagma Verbal...')
    return sintagmaNList, sintagmaVList, verbList, nounList
    

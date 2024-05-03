import lexic
import syntatic
import semantic

def main():
    inputText = 'A paraíba é o estado do Nordeste que mais ampliou sua rede obstetrícia.' 
    print('[MAIN] Calling Lexic...')
    tokens = lexic.lexic(inputText)
    print('[MAIN] Calling Syntatic...')
    sintagmaNominal, sintagmaVerbal  = syntatic.syntatic(tokens)
    print('[MAIN] Calling Semantic...')
    semantic.semantic(sintagmaNominal, sintagmaVerbal)
    

if __name__ == "__main__":
    main()
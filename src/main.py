import lexic
import syntatic
import semantic


def main():
    inputText = 'A gasolina acabou no meio da viagem.' 
    print('[MAIN] Calling Lexic...')
    tokens = lexic.lexic(inputText)
    print('[MAIN] Calling Syntatic...')
    sintagmaNominal, sintagmaVerbal, verbList, nounList  = syntatic.syntatic(tokens)
    print('[MAIN] Calling Semantic...')
    semantic.semantic(sintagmaNominal, sintagmaVerbal,verbList, nounList)
    

if __name__ == "__main__":
    main()
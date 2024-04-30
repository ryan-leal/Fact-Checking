import lexic
import syntatic
import semantic

def main():
    inputText = 'A paraíba é o estado do Nordeste que mais ampliou sua rede obstetrícia' 
    print('[MAIN] Calling Lexic...')
    lexic.lexic(inputText)
    print('[MAIN] Calling Syntatic...')
    syntatic.syntatic()
    print('[MAIN] Calling Semantic...')
    semantic.semantic()
    

if __name__ == "__main__":
    main()
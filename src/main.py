import lexic
import syntatic
import semantic

def main():
    print('[MAIN] Calling Lexic...')
    lexic.lexic()
    print('[MAIN] Calling Syntatic...')
    syntatic.syntatic()
    print('[MAIN] Calling Semantic...')
    semantic.semantic()
    

if __name__ == "__main__":
    main()

def palavras(path: str):
    with open(path) as arquivo:
        qtd_words = 0
        for linha in arquivo:
            qtd_words += len(linha.split(' '))
            
    return qtd_words

    
def letras(path: str):
    with open(path) as arquivo:
        qtd_letters = 0
        for linha in arquivo:
            qtd_letters += len(linha.replace(' ','').replace('\n',''))

    return qtd_letters

def letra(path: str):

    qtd_letter = 0
    letra = input("Digite uma letra: ")
    with open(path) as arquivo:
        for linha in arquivo:
            qtd_letter += linha.count(letra)

    return qtd_letter

print("Bem-vindo ao leitor de arquivos .txt!\n\n")


path = input("Digite o caminho do arquivo que deseja acessar: ")

print("\n1 - Qtd. Palavras\n" \
    "2 - Qtd. Letras\n" \
   "3 - Qtd. letra específica\n".center())

escolha = int(input("Digite o número corresnpondente à sua escolha: "))

match escolha:
    
    case 1:
        print(palavras(path))
    
    case 2:
        print(letras(path))
    
    case 3:
        print(letra(path))

    case _:
        print("Escolha errada. Tente novamente.")



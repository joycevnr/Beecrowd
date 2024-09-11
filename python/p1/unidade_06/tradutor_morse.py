# Dicionário de mapeamento de morse para letras
morse_dict = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', 
    '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', 
    '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', 
    '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'
}

# Função tradutor Morse

#A função join() é usada para concatenar (ou "juntar") elementos de uma lista (ou qualquer sequência) 
# em uma única string, com um separador definido entre os elementos.

def tradutor_morse(morse_code_list):
    return ''.join([morse_dict[code] for code in morse_code_list])

# Exemplo de uso
assert tradutor_morse(['.--.', '-.--', '-',' ....', '---', '-.']) == 'python'


# Estrutura do join():
# separador.join(iterável)
# separador: É a string que será usada como separador entre os itens. No nosso caso, é uma string vazia '', o que significa que os elementos serão concatenados sem nenhum separador.
# iterável: Pode ser uma lista, tupla, ou qualquer sequência de strings que você quer juntar


#QUESTÃO CHATA, SÓ TEM O TAMANHO DE DIGITAR ISSO, SE NÃO FOR USAR JOIN E DICTIONARY, VAI TER QUE COLOCAR IF E ELIF PARA CADA CÓDIGO E DEPOIS CONCATENAR. 
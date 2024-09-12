def remove_espacos(palavra):
    new_palavra = ''
    for car in palavra:
        if car != ' ':
            new_palavra += car
    return new_palavra

def eh_palindromo(palavra):
    for i in range(len(palavra)//2):
        if palavra[i] != palavra[-i-1]:
            return False
    return True


def palindromos(strings):
    p = []
    for palavra in strings:
        if eh_palindromo(remove_espacos(palavra)):
            p.append(palavra)
    return p


palavras = ['anilina', 'vira copo', 'mirim']
print(palindromos(palavras))

assert palindromos(palavras) == ['anilina', 'mirim']
assert palavras == ['anilina', 'vira copo', 'mirim']



# # Palíndromos!

# Uma string é uma palíndromo se é igual a ela própria invertida.
# Por exemplo, são palíndromos: `arara`, `anilina`, `mussum`, etc.
# Também dizemos que frases inteiras são palíndromas. Neste caso,
# contudo, ignoramos os espaços. Por exemplo, a frase `subi no
# onibus` é um exemplo de frase palíndroma.

# Escreva a função `palindromos(strings)` que recebe uma lista de
# strings e identifica quais delas são palíndromas.  Você pode
# assumir que todas as strings da lista são formadas apenas por
# letras e espaços (e que nenhuma string é vazia). Para
# simplificar, você também pode assumir que todas as letras das
# strings da lista são minúsculas e não têm acentos.

# A função não deve ter efeito colateral e deve retornar uma lista
# de todas as strings que são palíndromas, mantendo a ordem
# relativa da lista original.

# Leia o arquivo de testes fornecido para ver exemplos de uso da
# função e compreender melhor como deve funcionar.

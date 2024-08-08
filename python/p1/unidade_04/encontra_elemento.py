numero = int(input())
sequencia = input()
lista = list(map(int, sequencia.split()))
encontrado = False

for i in range(len(lista)):
    if numero == lista[i]:
        encontrado = True
        break
    else:
        encontrado = False

if encontrado == True:
    print("sim")
else:
    print("não")

# def verifica_numero_na_lista(numero, lista):
#     #Variável de controle como False
#     encontrado = False
#     for num in lista:
#         if numero == num:
#             encontrado = True
#             break
#     return encontrado


# def main():
#     numero = int(input())
#     sequencia = input()
#     lista = list(map(int, sequencia.split()))

#     if verifica_numero_na_lista(numero, lista):
#         print("sim")
#     else:
#         print("não")

# if __name__ == "__main__":
#     main()


# JS
# function verificaNumeroNaLista(numero, lista) {
#   for (let i = 0; i < lista.length; i++) {
#     if (numero === lista[i]) {
#       return true;
#     }
#   }
#   return false;
# }

# function main() {
#   const numero = 7;
#   const lista = [1, 5, 3, 2, 8, 9, 2];
#   /*const numero = parseInt(prompt(""));
#   const sequencia = prompt("");
#   const lista = sequencia.split(' ').map(Number);*/

#   if (verificaNumeroNaLista(numero, lista)) {
#     console.log("sim");
#   } else {
#     console.log("não");
#   }
# }

# main();


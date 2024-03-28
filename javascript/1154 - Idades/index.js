let  input = require('fs').readFileSync('stdin', 'utf8');
let valores = input.split('\n').map(Number);
class LSE {

    constructor() {
        this.cabeca = null;
    }

    inserir(valor) {
        let novoNo = new No(valor);
        if (this.cabeca == null) {
            // 1ª variação
            this.cabeca = novoNo;
        } else {
            // 2ª variação
            let ultimoNo = this.cabeca;
            while(!ultimoNo.ehUltimo()) {
                ultimoNo = ultimoNo.prox;
            }
            ultimoNo.prox = novoNo;
        }
    }
  estaVazia(){
    return this.cabeca == null;
  }
  estahForaDaLista(indice){
    return indice >= this.contagem() 
  }
  indiceInvalido(indice){
    return indice < 0;
  }

    contagem() {
        let contador = 0;
        if (this.estaVazia()) {
            // 1ª variação - Lista vazia
            return contador;
        } else {
            // 2ª variação - Lista NÃO vazia
            contador = 1;
            let ultimoNo = this.cabeca;
            while(!ultimoNo.ehUltimo()) {
                ultimoNo = ultimoNo.prox;
                contador++;
            }
            return contador;
        }
    }
  recuperacao(indice){
        if (this.indiceInvalido(indice) || this.estaVazia() || this.estahForaDaLista(indice)) {
            // 1ª variação - Lista vazia OU índice fora da lista
            return null;
        } else {
            // 2ª variação - Lista NÃO vazia
          let indiceAtual = 0;
          let noAtual = this.cabeca;
          while(indiceAtual != indice) {
            indiceAtual++;
            noAtual = noAtual.prox;
            }
            return noAtual.valor;
        }
    
  }  

}

class No {
    
    constructor(valor) {
        this.valor = valor;
        this.prox = null;
    }

    ehUltimo() {
        return this.prox == null;
    }
}
let soma = 0;
let lista = new LSE();
for (let i in valores){
  if(valores[i] > 0){
    lista.inserir(valores[i]);
    soma += valores[i];   
  }
}
let media = soma / lista.contagem();
console.log(media.toFixed(2));
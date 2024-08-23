while (true) {
    let valor = prompt("Digite uma sequência de 8 bits ou 'fim' para sair:");
    
    if (valor === 'fim') {
        break;
    }

    if (valor.length !== 8) {
        console.log('Tente novamente.');
        continue;
    }

    let primeiroDigito = valor.slice(0, 4); // Pega os primeiros 4 bits
    let segundoDigito = valor.slice(4, 8);  // Pega os últimos 4 bits

    // Convertendo os 4 primeiros bits e os 4 últimos bits para decimal
    let digito1 = parseInt(primeiroDigito, 2);
    let digito2 = parseInt(segundoDigito, 2);

    // Verifica se os valores convertidos estão entre 0 e 9 (números válidos em BCD)
    if (digito1 > 9 || digito2 > 9) {
        console.log('BCD inválido.');
    } else {
        console.log(`${digito1}${digito2}`);
    }
}

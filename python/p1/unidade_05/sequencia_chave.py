




# # Sequência chave

# Um aplicativo que lê uma sequência de valores de um dispositivo de
# medição precisa reconhecer uma sequência específica de valores, chamada
# _sequência chave_. Quando a sequência chave for lida dos dados de
# entrada, a partir de qualquer posição, a leitura de dados deve ser
# interrompida e devem ser impressos a soma dos inteiros lidos antes da
# chave e os índices que os elementos da chave ocupam na sequência de
# inteiros lida. É importante observar que os valores da sequência chave
# só devem ser reconhecidos como sendo da sequência chave se forem lidos
# em verdadeira sequência (um imediatamente depois do outro).

# ## Entrada

# Uma entrada válida  para o programa tem duas partes: i) na primeira
# linha deve constar a sequência chave de inteiros a ser reconhecida (a
# sequência tem tamanho arbitrário); e ii) a partir da segunda linha são
# fornecidos os valores da sequência de inteiros produzidos pelo
# equipamento, sendo um inteiro por linha. Um exemplo de entrada válido é
# dado abaixo, em que a sequência chave é `10 20 30`.

# ```
# 10 20 30
# 8
# 7
# 10
# 20
# 30
# 6
# 12
# ```

# ## Saída

# A saída consiste em duas linhas apenas. Na primeira, deve ser impressa a
# soma dos valores inteiros lidos até antes da sequência chave. Na segunda
# linha devem ser exibidos os índices inicial e final (com início sendo
# zero) dos elementos da chave na sequência de inteiros. Abaixo um exemplo
# de entrada válida que corresponde à entrada acima.

# ```
# soma = 15
# pos_chave = 2 .. 4
# ```

# ## Observações

# Observe que a soma corresponde aos valores lidos antes do início da
# sequência chave. E que os índices `2 .. 4` indicam que a chave foi lida
# no terceiro (índice `2`), quarto e quinto (índice `4`) elementos da
# sequência. Observe ainda que os valores fornecidos na entrada após a
# sequência chave não devem ser lidos, já que são irrelevantes para a
# aplicação.

# A terceira observação é observar que os valores da sequência chave que
# não forem parte efetiva da sequência lida (que não configurarem a
# sequência em si) devem ser tratados como valores normais de entrada.
# Para ver um exemplo disso, veja o segundo exemplo fornecido nos testes
# automáticos.

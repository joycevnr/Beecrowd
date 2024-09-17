def encontros_vocalicos(palavra):
    encontros_vocalicos = []
    encontro = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            encontro += letra
        else:
            if len(encontro) > 1:
                encontros_vocalicos.append(encontro)
            encontro = ''
    if len(encontro) > 1:
        encontros_vocalicos.append(encontro)

    return encontros_vocalicos

assert encontros_vocalicos('poeira') == ['oei']


# # Acha Encontros Vocálicos

# Escreva a função `encontros_vocalicos(palavra)` que retorna uma
# lista que contenha cada um dos encontros vocálicos encontrados em
# `palavra`. Por exemplo, se a palavra for `cadeira`, a função
# deve retornar a lista `["ei"]`. Se a palavra for `poeira`, deve
# retornar `["oei"]`.

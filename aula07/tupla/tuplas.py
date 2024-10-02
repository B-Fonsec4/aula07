# tupla_vazia = ()



# tupla_um_elemento = (10,) #virgula no fim para ser tupla
# # print(tupla_um_elemento)

# tupla_varios_elementos = (5, 4, 10, 11, 15)
# # print(tupla_varios_elementos[0])
# # tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos
# # print(tupla_um_elemento)
# # print(10 in tupla_varios_elementos)

# print(sorted(tupla_varios_elementos))

nome = input('informe o nome: ')
nota1 = input('informe a nota1: ')
nota2 = input('informe a nota2: ')

tupla_notas = (nome, nota1, nota2)
print(f'Dados do usuario: {tupla_notas}')
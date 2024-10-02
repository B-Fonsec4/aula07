

def verifica_par(n):
    resposta = ''
    valor = n % 2

    if valor == 0:
        resposta = 'Par'
    else:
        resposta = 'Impar'
        return resposta
    


n = float(input('Numero: '))

resp = verifica_par(n)

print(f'{n} é {resp}')

def resposta(peso):
    peso_maximo = 50
    if peso > peso_maximo:
        excesso_peso = peso - peso_maximo
        multa = excesso_peso * 4
    else:
        excesso_peso = 0
        multa = 0
    return (excesso_peso, multa)


print(resposta(60))
print(resposta(50))
print(resposta(45))

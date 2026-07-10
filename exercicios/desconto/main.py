def resposta(preco, percentual):
    desconto = preco * (percentual/100)
    preco_final = preco - desconto
    return (desconto, preco_final)


print(resposta(100, 10))
print(resposta(200, 25))

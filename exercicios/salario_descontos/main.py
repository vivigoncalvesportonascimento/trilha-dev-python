def resposta(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (ir + inss + sindicato)
    return (salario_bruto, ir, inss, sindicato, salario_liquido)


print(resposta(10, 160))
print(resposta(20, 100))

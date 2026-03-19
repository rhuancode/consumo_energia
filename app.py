# Entrada
nome_aparelho = input('Digite o nome do aparelho (ex: Geladeira): ')
print()
potencia = float(input('Digite a potência do aparelho em watts (W): '))
print()
horas_dia = float(input('Digite o tempo médio de uso diário em horas: '))
print()

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75

#Saída
print(f". Aparelho: {nome_aparelho}")
print()
print(f". Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print()
print(f". Custo estimado: R$ {custo_estimado:.2f} por mês.")
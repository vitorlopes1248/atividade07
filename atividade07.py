# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
valorprod = int(input("Digite o valor do se produto: "))

calcimposto = (valorprod * 12) /100

valortotal = calcimposto + valorprod

print("Seu valor final é: ", valortotal)


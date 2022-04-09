# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá Mundo")


# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("Digite um número")
print("O número que você digitou foi: ", numero)


# 3. Faça um Programa que peça dois números e imprima a soma.
num1 = input("Digite um número: ")
num2 = input("Digite mais um número: ")
soma = int(num1) + int(num2)
print("A soma dos seus números foi:", soma)


# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = input("Primeira Nota: ")
nota2 = input("Segunda Nota: ")
nota3 = input("Terceira Nota: ")
nota4 = input("Quarta Nota: ")
media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4
print("A média das notas é: ", media)


# 5. Faça um Programa que converta metros para centímetros.
metros = input("Digite o metro: ")
cent = float(metros) * 100
print("Os metros em centímetros são: ", cent)


# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("Digite o raio do círculo: "))
cal = raio * 3.14
print( "A área do cálculo do raio do círculo é: ", "%.2f" % cal)

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
area_q = int(input("Digite a área do quadrado:"))
area = area_q * area_q
print("A área do quadrado é: ", area)
print ("O dobro da área é: ", area * 2)

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Ganho por hora: "))
numero_horas = int(input("Número de horas trabalhadas no mês: "))
salario = ganho_hora * numero_horas
print("Seu salário é de: ", salario)


# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
frt = float(input("Graus Fahrenheit: "))
c = ((frt-32) * 5/9)
print("Temperatura em graus Celsius: ", "%.f" % c,"°C")


# 10. Faça um Programa que peça a tempermatura em graus Celsius, transforme e mostre em graus Fahrenheit
c = float(input("Graus Celsius: "))
frt = ((c * 9/5) + 32)
print("Temperatura em graus Fahrenheit: ", "%.f" % frt,"°F")

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
  # A. o produto do dobro do primeiro com metade do segundo .
  numint1 = int(input("Digite o primeiro número inteiro: "))
  numint2 = int(input("Digite o segundo número inteiro: "))
  numreal = float(input("Digite um número real: "))
  dobro = numint1 * 2 
  metado_segundo = dobro * numint2/2
  print("O valor é: ", "%.2f" % metado_segundo)
  
  # B. a soma do triplo do primeiro com o terceiro.
  numint1 = int(input("Digite o primeiro número inteiro: "))
  numint2 = int(input("Digite o segundo número inteiro: "))
  numreal = float(input("Digite um número real: "))
  triplo = numint1 * 3 
  result = triplo + numreal
  print("O valor é: ", "%.2f" % result)

  #  C. o terceiro elevado ao cubo.
  numint1 = int(input("Digite o primeiro número inteiro: "))
  numint2 = int(input("Digite o segundo número inteiro: "))
  numreal = float(input("Digite um número real: "))
  cubo = numreal * numreal * numreal
  print("O valor é: ", "%.2f" % cubo)

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
peso_ideal
altura = float(input("Digite sua altura: "))
peso_ideal = (72.7 * altura) - 58
print("Seu peso ideal é: ", "%.2f" % peso_ideal)


# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
  # A. Para homens: (72.7*h) - 58
  altura_h = float(input("Digite sua altura: "))
  peso_ideal_h = (72.7 * altura_h) - 58
  print("Seu peso ideal é: ", "%.2f" % peso_ideal_h)
  
  # B. Para mulheres: (62.1*h) - 44.7
  peso_ideal_h
  altura_m = float(input("Digite sua altura: "))
  peso_ideal_m = (62.1 * altura_m) - 44.7
  print("Seu peso ideal é: ", "%.2f" % peso_ideal_m)
  
# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso = int(input("Digite o peso dos peixes: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print("Valor excedido, a multa é de: ", multa)
else:
    print("Valor não excedido")
    
    
# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
# para o INSS e 5% para o sindicato, faça um programa que nos dê:
ganho_hora = float(input("Ganho por hora: "))
numero_horas = int(input("Número de horas trabalhadas no mês: "))
salario = ganho_hora * numero_horas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario  * 0.05
salario_liquido = salario - ir - inss - sindicato
print("+ Salário Bruto : R$", salario)
print("- IR (11%) : R$", ir )
print("- INSS (8%) : R$", inss)
print("- Sindicato ( 5%) : R$", sindicato)
print("= Salário Liquido : R$", salario_liquido)


# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanho_metros = int(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros = tamanho_metros / 3
precol = 80.0
lata_tinta = 18
latas = tamanho_metros / lata_tinta
total = latas * precol
print("A quantidade de latas de tinta a serem compradas são: ","%.1f" % latas, "E o preço total é de: ", "%.1f" % total)

# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arq = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_link = float(input("Digite a velocidade em Mbps: "))
tempo_d = (tamanho_arq / velocidade_link) * 60
print("o tempo de espera é: ","%.0f minutos" % tempo_d)

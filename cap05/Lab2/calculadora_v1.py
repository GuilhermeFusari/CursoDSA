# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 

# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print ("Selecione o número da opção desejada:\n")
print(" 1 - Soma\n","2 - Subtração\n","3 - Multiplicação\n","4 - Divisão")

def soma (v1,v2):
	return print(v1, "+", v2, "=", v1 + v2)
def subtracao (v1,v2):
	return print(v1, "-", v2, "=", v1 - v2)
def multiplicacao(v1,v2):
	return print(v1, "*", v2, "=", v1 * v2)
def divisao(v1,v2):
	return print(v1, "/", v2, "=", v1 / v2)

def calculadora():
	escolha = input("Digite sua opção (1/2/3/4): ")
	v1 = int(input("Digite o primeiro número: "))
	v2 = int(input("Digite o segundo número: "))
	if escolha == '1':
		soma(v1,v2)
	elif escolha == '2':
		subtracao(v1,v2)
	elif escolha == '3':
		multiplicacao(v1,v2)
	elif escolha == '4':
		divisao(v1,v2)
	else:
		return calculadora

calculadora()


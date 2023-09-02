import calculadora

#Criando variaveis
interesse = ""
rodando = True
n1 = 0
n2 = 0

#Texto explicativo:
print("")
print("O intuito desse script é ser uma calculadora simples. Siga as intruções para ultilizá-la:")

#Loop para menu:
while rodando == True:
  #Texto para orientação e input:
  print("")
  print("Digite um dos seguintes comandos: ")
  print("")
  print("Digite 'soma' para somar;")
  print("Digite 'subtrair' para realizar a subtração;")
  print("Digite 'multiplicar' para realizar a multiplicação;")
  print("Digite 'dividir' para realizar a divisão;")
  print("Digite 'sair' para sair.")
  print("")
  interesse = str(input("Digite aqui a ação aqui: "))

  #Calculo:
  if interesse == "sair":
    rodando = False

  elif interesse == "soma":
    n1 = float(input("Digite aqui o primeiro número: "))
    n2 = float(input("Digite aqui o segundo número: "))
    calculadora.somar(n1, n2)

  elif interesse == "subtrair":
    n1 = float(input("Digite aqui o primeiro número: "))
    n2 = float(input("Digite aqui o segundo número: "))
    calculadora.subtrair(n1, n2)

  elif interesse == "multiplicar":
    n1 = float(input("Digite aqui o primeiro número: "))
    n2 = float(input("Digite aqui o segundo número: "))
    calculadora.multiplicar(n1, n2)

  elif interesse == "dividir":
    n1 = float(input("Digite aqui o primeiro número: "))
    n2 = float(input("Digite aqui o segundo número: "))
    calculadora.dividir(n1, n2)

  else:
    print("")
    print("O que você digitou não possuí uma ação, digite novamente outra ação mostrado no menu e para posteriormente realizá-la.")